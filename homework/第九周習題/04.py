import numpy as np

def cross_entropy(p, q):
    return -np.sum(p * np.log2(q + 1e-12))

def verify():
    p = np.array([0.3, 0.7])
    # 隨機產生一個不同於 p 的分佈 q
    qs = [np.array([0.1, 0.9]), np.array([0.5, 0.5]), np.array([0.8, 0.2])]
    
    h_pp = cross_entropy(p, p)
    print(f"基準值 H(p, p): {h_pp:.4f}\n" + "-"*30)
    
    for q in qs:
        h_pq = cross_entropy(p, q)
        print(f"測試分佈 q: {q}")
        print(f"交叉熵 H(p, q): {h_pq:.4f}")
        print(f"驗證 H(p, q) > H(p, p): {h_pq > h_pp}")
        print("-" * 30)

verify()