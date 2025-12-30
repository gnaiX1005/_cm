import cmath

def dft(x):
    """
    手寫離散傅立葉正轉換 (DFT)
    """
    N = len(x)
    X = []
    for k in range(N):
        sum_val = complex(0, 0)
        for n in range(N):
            # 指數部分: -2j * pi * k * n / N
            angle = -2j * cmath.pi * k * n / N
            sum_val += x[n] * cmath.exp(angle)
        X.append(sum_val)
    return X

def idft(X):
    """
    手寫離散傅立葉逆轉換 (IDFT)
    """
    N = len(X)
    x = []
    for n in range(N):
        sum_val = complex(0, 0)
        for k in range(N):
            # 指數部分: 2j * pi * k * n / N
            angle = 2j * cmath.pi * k * n / N
            sum_val += X[k] * cmath.exp(angle)
        # 最後需要除以 N
        x.append(sum_val / N)
    return x

# --- 驗證邏輯 ---

# 1. 定義一個測試函數 f(x)，例如一個簡單的組合波形
f_original = [1.0, 2.0, 3.0, 4.0, 3.0, 2.0, 1.0, 0.0]

# 2. 進行正轉換
F_omega = dft(f_original)

# 3. 進行逆轉換
f_recovered = idft(F_omega)

# 4. 印出結果比較
print(f"{'原始數據':<15} | {'逆轉換後數據':<25}")
print("-" * 45)
for org, rec in zip(f_original, f_recovered):
    # 由於浮點數誤差，我們取實部並四捨五入
    print(f"{org:<15.2f} | {rec.real:<25.2f} (複數: {rec:.2f})")

# 5. 檢查兩者是否接近
all_close = all(abs(org - rec) < 1e-10 for org, rec in zip(f_original, f_recovered))
print(f"\n驗證結果：{'成功' if all_close else '失敗'} (兩者誤差極小)")