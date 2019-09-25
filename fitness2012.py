# Fitness algorith, 2012
import numpy as np
import pandas as pd

ITERATIONS = 20









###################################

# Toy model
M = np.array([[1, 1, 0, 0, 0],
              [0, 1, 0, 1, 1],
              [1, 0, 1, 0, 0]])

###################################



# number of countries = C; products = P
C = M.shape[0]
P = M.shape[1]

# Set initial conditions
F_N = np.ones((1, C))
Q_N = np.ones((1, P))

# Set loop
for i in range(ITERATIONS):

    F_tilde = np.sum(np.multiply(M, Q_N), axis=1)
    Q_tilde = 1 / (np.sum(np.multiply(M.T, (1 / F_N)), axis=1))

    # normalize
    F_N = F_tilde / np.mean(F_tilde)
    Q_N = Q_tilde / np.mean(Q_tilde)

print(f"Complexity: {Q_N}")
print(f"Fitness: {F_N}")
# file ends here, l34
