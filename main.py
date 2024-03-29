import numpy as np

# Означення матриці перехідних ймовірностей P(Y | X)
P = np.array([[0.98, 0.02], [0.22, 0.78]])

# Обчислення ентропії вихідної випадкової величини Y
p_y = np.sum(P, axis=0)  # ймовірності випадкової величини Y
H_y = - np.sum(p_y * np.log2(p_y))  # ентропія випадкової величини Y

# Обчислення умовної ентропії вихідної випадкової величини Y при відомому вхідному символі X
p_x = np.array([0.5, 0.5])  # ймовірності вхідної випадкової величини X
H_y_given_x = np.sum(np.array([np.sum(P[:,i] * np.log2(P[:,i])) for i in range(P.shape[1])]) * p_x)

# Обчислення взаємної інформації між вхідною та вихідною випадковими величинами
I_xy = H_y - H_y_given_x

# Обчислення пропускної здатності каналу
symbol_duration = 1e-3  # середня тривалість кожного символу на виході джерела (в секундах)
channel_capacity = I_xy / symbol_duration  # пропускна здатність каналу (в бітах за секунду)

print("Пропускна здатність каналу:", channel_capacity, "біт/с")

