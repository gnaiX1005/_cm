import math

def main():
    p = 0.5
    n = 10000
    
    # 使用 log10 計算：log10(0.5^10000) = 10000 * log10(0.5)
    log_p_n = n * math.log10(p)
    
    print(f"log10(0.5^10000) 的計算結果為: {log_p_n:.4f}")
    
    # 解釋結果
    mantissa = 10**(log_p_n - math.floor(log_p_n))
    exponent = math.floor(log_p_n)
    print(f"換算為科學記號: {mantissa:.4f} * 10^{exponent}")

if __name__ == "__main__":
    main()