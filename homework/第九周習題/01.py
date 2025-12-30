def main():
    p = 0.5
    n = 10000
    
    # 直接計算
    probability = p ** n
    
    print(f"投擲次數: {n}")
    print(f"直接計算結果: {probability}")
    print(f"註：結果為 0.0 是因為數值小於電腦浮點數精確度上限。")

if __name__ == "__main__":
    main()