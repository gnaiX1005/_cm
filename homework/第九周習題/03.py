import numpy as np

def entropy(p):
    return -np.sum(p * np.log2(p + 1e-12))

def cross_entropy(p, q):
    return -np.sum(p * np.log2(q + 1e-12))

def kl_divergence(p, q):
    return cross_entropy(p, q) - entropy(p)

def mutual_information(p_xy):
    # p_xy 是聯合機率分布矩陣
    p_x = np.sum(p_xy, axis=1)
    p_y = np.sum(p_xy, axis=0)
    mi = 0
    for i in range(len(p_x)):
        for j in range(len(p_y)):
            if p_xy[i,j] > 0:
                mi += p_xy[i,j] * np.log2(p_xy[i,j] / (p_x[i] * p_y[j]))
    return mi

# 測試資料
p = np.array([0.5, 0.5])
q = np.array([0.1, 0.9])
p_xy = np.array([[0.4, 0.1], [0.1, 0.4]])

print(f"Entropy H(p): {entropy(p):.4f}")
print(f"Cross Entropy H(p,q): {cross_entropy(p, q):.4f}")
print(f"KL Divergence D_KL(p||q): {kl_divergence(p, q):.4f}")
print(f"Mutual Information I(X;Y): {mutual_information(p_xy):.4f}")