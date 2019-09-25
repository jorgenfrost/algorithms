#!/usr/bin/env python

# Hidalgo Haussman
import numpy as np

ITERATIONS = 20

# Toy model
M = np.array([[1, 1, 0, 0, 0],
              [0, 1, 0, 1, 1],
              [1, 0, 1, 0, 0]])

# number of countries = C; products = P
C = M.shape[0]
P = M.shape[1]

div_0 = np.sum(M, axis=1)  # exported products per country
ubiq_0 = np.sum(M.T, axis=1)  # countries product is eported by

div_N = div_0
ubiq_N = ubiq_0


for i in range(ITERATIONS):
    div_N = (1 / div_0) * np.sum(np.multiply(M, ubiq_N), axis=1)
    ubiq_N = (1 / ubiq_0) * np.sum(np.multiply(M.T, div_N), axis=1)

print(div_N)
print(ubiq_N)
