import math

# --- 1. 定義基礎物件 ---
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

class Line:
    def __init__(self, A, B, C):
        self.A, self.B, self.C = A, B, C

    @classmethod
    def from_points(cls, p1, p2):
        A = p1.y - p2.y
        B = p2.x - p1.x
        C = p1.x * p2.y - p2.x * p1.y
        return cls(A, B, C)

# --- 2. 核心功能計算 ---

def get_perpendicular_foot(p, line):
    """計算點 p 到直線 line 的垂足"""
    denom = line.A**2 + line.B**2
    dx = line.A * (line.A * p.x + line.B * p.y + line.C) / denom
    dy = line.B * (line.A * p.x + line.B * p.y + line.C) / denom
    return Point(p.x - dx, p.y - dy)

def dist(p1, p2):
    """兩點距離公式"""
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

# --- 3. 執行與驗證 ---

# 設定情境：
# 直線 L 通過 (0,0) 和 (4,0) -> 也就是 X 軸 (y=0)
# 線外一點 P (2, 3)
# 直線上另一點 B (0, 0)
L = Line.from_points(Point(0, 0), Point(4, 0))
P = Point(2, 3)
B = Point(0, 0)

# A. 求垂足 C
C = get_perpendicular_foot(P, L)
print(f"1. 線外一點 P: {P}")
print(f"2. 直線上垂足 C: {C}")

# B. 驗證畢氏定理 (三角形 PBC，其中角 C 是直角)
# a^2 + b^2 = c^2 -> PC^2 + BC^2 = PB^2
side_PC = dist(P, C)
side_BC = dist(B, C)
side_PB = dist(P, B)

print("-" * 30)
print(f"PC 距離: {side_PC:.2f}")
print(f"BC 距離: {side_BC:.2f}")
print(f"PB (斜邊) 距離: {side_PB:.2f}")

pythagorean_check = abs(side_PC**2 + side_BC**2 - side_PB**2) < 1e-9
print(f"3. 畢氏定理驗證結果: {pythagorean_check} (PC² + BC² = PB²)")

# --- 4. 幾何變換示範 (以點 P 為例) ---
def rotate_point(p, angle_deg, center=Point(0,0)):
    rad = math.radians(angle_deg)
    nx = center.x + (p.x - center.x) * math.cos(rad) - (p.y - center.y) * math.sin(rad)
    ny = center.y + (p.x - center.x) * math.sin(rad) + (p.y - center.y) * math.cos(rad)
    return Point(nx, ny)

rotated_P = rotate_point(P, 90)
print("-" * 30)
print(f"4. 將 P 點繞原點旋轉 90 度: {rotated_P}")