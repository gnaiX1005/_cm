import math

# 1. 選擇兩個質數 (真實 RSA 會選非常大的質數)
p = 61
q = 53

# 2. 計算 n = p * q (這是公鑰的一部分)
n = p * q

# 3. 計算 歐拉函數 phi = (p-1) * (q-1)
phi = (p - 1) * (q - 1)

# 4. 選擇 e (必須與 phi 互質，通常用 65537，這裡選 17)
e = 17

# 5. 計算私鑰 d (滿足 e * d % phi == 1 的數)
def extended_gcd(a, b):
    if a == 0: return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

_, d, _ = extended_gcd(e, phi)
d = d % phi # 確保 d 是正數

print(f"--- 金鑰生成完畢 ---")
print(f"公鑰 (n, e): ({n}, {e})")
print(f"私鑰 (d): {d}")
print("-" * 20)

# 6. 加密過程: C = M^e mod n
message = 42  # 假設我們要加密數字 42
ciphertext = pow(message, e, n)
print(f"原始訊息: {message}")
print(f"加密後的密文: {ciphertext}")

# 7. 解密過程: M = C^d mod n
decrypted_msg = pow(ciphertext, d, n)
print(f"解密後的訊息: {decrypted_msg}")