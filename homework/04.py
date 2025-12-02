import numpy as np

c = [1, 0, -3, 0, 2, -1]  # x^5 - 3x^3 + 2x -1
roots = np.roots(c[::-1])  # numpy 要最高次在前
print(roots)
