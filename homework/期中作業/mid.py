def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    # 如果是解密，位移量要變成負的
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            # 處理大寫或小寫
            start = ord('A') if char.isupper() else ord('a')
            # 核心數學公式：(字元編碼 - 起始點 + 位移) % 26
            new_pos = (ord(char) - start + shift) % 26
            result += chr(start + new_pos)
        else:
            result += char
    return result

# 測試
message = "Math is Beautiful"
secret = caesar_cipher(message, 3, 'encrypt')
print(f"加密後: {secret}")
print(f"解密後: {caesar_cipher(secret, 3, 'decrypt')}")