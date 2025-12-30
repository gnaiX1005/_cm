import numpy as np

# 定義生成矩陣與檢驗矩陣
G = np.array([[1,1,0,1], [1,0,1,1], [1,0,0,0], [0,1,1,1], [0,1,0,0], [0,0,1,0], [0,0,0,1]])
H = np.array([[1,0,1,0,1,0,1], [0,1,1,0,0,1,1], [0,0,0,1,1,1,1]])

def hamming_74():
    # 1. 原始 4 位元資料
    data = np.array([1, 0, 1, 1])
    print(f"原始資料: {data}")
    
    # 2. 編碼 (7 位元)
    encoded = np.dot(G, data) % 2
    print(f"編碼後 (7-bit): {encoded}")
    
    # 3. 模擬傳輸錯誤 (反轉第 1 位元)
    error_encoded = encoded.copy()
    error_encoded[0] = 1 - error_encoded[0]
    print(f"發生錯誤的資料: {error_encoded}")
    
    # 4. 解碼與糾錯
    syndrome = np.dot(H, error_encoded) % 2
    error_pos = int("".join(map(str, syndrome[::-1])), 2)
    
    if error_pos != 0:
        print(f"偵測到第 {error_pos} 位元錯誤，自動修復中...")
        error_encoded[error_pos - 1] = 1 - error_encoded[error_pos - 1]
    
    # 提取數據位 (第 3, 5, 6, 7 位)
    decoded = error_encoded[[2, 4, 5, 6]]
    print(f"解碼回原始資料: {decoded}")

hamming_74()