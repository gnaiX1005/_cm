import hashlib

def get_hash(text):
    # 使用 SHA-256 演算法
    return hashlib.sha256(text.encode()).hexdigest()

password = "my_secure_password123"
print(f"原始密碼: {password}")
print(f"雜湊值 (存入資料庫的樣子): {get_hash(password)}")