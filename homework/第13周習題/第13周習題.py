import numpy as np
from collections import Counter

def solve_ode_general(coefficients):
    """
    求解常係數齊次線性常微分方程 (n階)。
    """
    # 1. 使用 numpy 求解特徵多項式的根
    roots = np.roots(coefficients)
    
    # 2. 處理數值誤差：將非常接近的根進行歸一化處理
    # 這是為了處理像 2.00000000001 和 1.99999999999 這種情況
    rounded_roots = []
    for r in roots:
        real = round(r.real, 6)
        imag = round(r.imag, 6)
        # 如果虛部極小，視為實數
        if abs(imag) < 1e-6:
            rounded_roots.append(real + 0j)
        else:
            rounded_roots.append(real + complex(0, imag))
    
    # 3. 統計根的重數
    # 由於複數共軛根（a + bi 和 a - bi）在 ODE 中是成對處理的，
    # 我們只處理虛部 >= 0 的根，之後再統一輸出。
    root_counts = Counter(rounded_roots)
    
    solutions = []
    processed_roots = set()
    term_index = 1

    # 排序根，讓輸出較美觀 (實數優先，虛數其次)
    unique_roots = sorted(root_counts.keys(), key=lambda x: (abs(x.imag) > 1e-5, x.real))

    for r in unique_roots:
        if r in processed_roots:
            continue
            
        multiplicity = root_counts[r]
        alpha = r.real
        beta = r.imag

        if abs(beta) < 1e-6:  # 實根情況
            for m in range(multiplicity):
                x_pow = f"x^{m}" if m > 1 else ("x" if m == 1 else "")
                solutions.append(f"C_{term_index}{x_pow}e^({alpha}x)")
                term_index += 1
            processed_roots.add(r)
            
        else:  # 複數根情況
            conj_r = alpha - complex(0, beta)
            # 取得該對共軛根的重數（通常兩者重數應相同）
            m_pair = root_counts[r]
            
            for m in range(m_pair):
                x_pow = f"x^{m}" if m > 1 else ("x" if m == 1 else "")
                e_part = f"e^({alpha}x)" if abs(alpha) > 1e-6 else ""
                
                # Cosine 部分
                solutions.append(f"C_{term_index}{x_pow}{e_part}cos({abs(beta)}x)")
                term_index += 1
                # Sine 部分
                solutions.append(f"C_{term_index}{x_pow}{e_part}sin({abs(beta)}x)")
                term_index += 1
            
            processed_roots.add(r)
            processed_roots.add(conj_r)

    return "y(x) = " + " + ".join(solutions)

# --- 測試主程式 (同您提供的範例) ---
if __name__ == "__main__":
    print("--- 實數單根範例 ---")
    coeffs1 = [1, -3, 2]
    print(solve_ode_general(coeffs1))

    print("\n--- 實數重根範例 ---")
    coeffs2 = [1, -4, 4]
    print(solve_ode_general(coeffs2))

    print("\n--- 複數共軛根範例 ---")
    coeffs3 = [1, 0, 4]
    print(solve_ode_general(coeffs3))

    print("\n--- 複數重根範例 ---")
    coeffs4 = [1, 0, 2, 0, 1]
    print(solve_ode_general(coeffs4))

    print("\n--- 高階重根範例 ---")
    coeffs5 = [1, -6, 12, -8]
    print(solve_ode_general(coeffs5))