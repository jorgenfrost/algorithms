# Fitness algorith, 2018
import numpy as np

ITERATIONS = 20
DELTA = 0

# Toy model
M = np.array([[1, 1, 0, 0, 0],
              [0, 1, 0, 1, 1],
              [1, 0, 1, 0, 0]])

# number of countries = C; products = P
C = M.shape[0]
P = M.shape[1]

# Set initial conditions
FN = np.ones((1, C))
QN = np.ones((1, P))


# Set loop
for i in range(ITERATIONS):

    FTILDE = (DELTA ** 2) + np.sum(np.multiply(M, (1 / QN)), axis=1)
    QTILDE = 1 + np.sum(np.multiply(M.T, (1 / FN)), axis=1)
    FN = FTILDE
    QN = QTILDE

print(f"Complexity: {QN}")
print(f"Fitness: {FN}")
# file ends here, l33
