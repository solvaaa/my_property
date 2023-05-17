import numpy as np
from scipy import sparse

x = np.array([[1, 2, 3], [4, 5, 6]])
print("x:\n{}".format(x))

eye = np.eye(4)
print("Массив NumPy:\n{}".format(eye))

sparse_matrix = sparse.csr_matrix(eye)
print("\nРазреженна матрица SciPy в формате CSR:\n{}".format(sparse_matrix))

