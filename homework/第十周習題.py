import numpy as np
from scipy.linalg import lu, svd, eig

# --- 1. 遞迴計算行列式 (Laplace Expansion) ---
def get_det_recursive(M):
    M = np.array(M)
    if M.shape == (1, 1): return M[0, 0]
    if M.shape == (2, 2): return M[0,0]*M[1,1] - M[0,1]*M[1,0]
    
    det = 0
    for c in range(M.shape[1]):
        minor = np.delete(np.delete(M, 0, axis=0), c, axis=1)
        det += ((-1)**c) * M[0, c] * get_det_recursive(minor)
    return det

# --- 2. 準備測試資料 ---
# 我們用一個 3x3 矩陣來測試
A = np.array([[3, 2, 1], 
              [1, 0, 2], 
              [4, 1, 3]])

print(f"--- 矩陣 A ---\n{A}\n")

# --- 3. 驗證各種分解 ---

# (A) LU 分解計算行列式
P, L, U = lu(A)
# det(A) = det(P) * det(L) * det(U)
det_A_lu = np.linalg.det(P) * np.prod(np.diag(U))
print(f"1. LU 分解行列式結果: {det_A_lu}")
print(f"   驗證 LU: P*L*U 是否等於 A? {np.allclose(A, P @ L @ U)}\n")

# (B) 特徵值分解 (Eigenvalue Decomposition)
# A = V * D * V_inv (僅限方陣)
eigenvalues, V = eig(A)
D = np.diag(eigenvalues)
print(f"2. 特徵值: {eigenvalues}")
print(f"   驗證 Eigen: V*D*V_inv 是否等於 A? {np.allclose(A, V @ D @ np.linalg.inv(V))}\n")

# (C) SVD 分解
U_s, S_diag, Vh = svd(A)
S = np.diag(S_diag)
print(f"3. SVD 奇異值: {S_diag}")
print(f"   驗證 SVD: U*S*Vh 是否等於 A? {np.allclose(A, U_s @ S @ Vh)}\n")

# (D) 用特徵值分解做 SVD (驗證觀念：A^T A 的特徵值是 SVD 奇異值的平方)
ATA = A.T @ A
eig_vals_ATA, _ = eig(ATA)
print(f"4. 驗證觀念: A^T A 的特徵值開根號 {np.sqrt(np.sort(eig_vals_ATA)[::-1])}")
print(f"   這是否等於 SVD 的奇異值? {np.allclose(np.sqrt(np.sort(eig_vals_ATA)[::-1]), S_diag)}\n")

# (E) PCA 主成分分析
def do_pca(data, k):
    # 1. 中心化 (去均值)
    centered_data = data - np.mean(data, axis=0)
    # 2. SVD 分解
    U, S, Vh = svd(centered_data)
    # 3. 投影到前 k 個主成分
    return centered_data @ Vh[:k].T

sample_data = np.random.rand(5, 3) # 5筆 3維數據
pca_result = do_pca(sample_data, 2)
print(f"5. PCA 原始數據形狀: {sample_data.shape}, 降維後形狀: {pca_result.shape}")