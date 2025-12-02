# finite_field_gf_p.py
# 實作有限體 GF(p)（p 為質數）以及檢驗群/體公理的測試程式。
# 可直接執行此檔案來跑測試。

from typing import Callable, List, Tuple

class FieldElement:
    """代表 GF(p) 中的元素，支援 + - * / 和比較運算子。
    """
    def __init__(self, value: int, p: int):
        if p <= 1:
            raise ValueError("p 必須為大於 1 的整數（且通常為質數）。")
        self.p = int(p)
        self.v = int(value) % self.p

    def __repr__(self):
        return f"FieldElement({self.v}, {self.p})"

    def __eq__(self, other):
        return isinstance(other, FieldElement) and self.p == other.p and self.v == other.v

    def __add__(self, other):
        self._check_field(other)
        return FieldElement(self.v + other.v, self.p)

    def __sub__(self, other):
        self._check_field(other)
        return FieldElement(self.v - other.v, self.p)

    def __neg__(self):
        return FieldElement(-self.v, self.p)

    def __mul__(self, other):
        self._check_field(other)
        return FieldElement(self.v * other.v, self.p)

    def __truediv__(self, other):
        self._check_field(other)
        if other.v == 0:
            raise ZeroDivisionError("除以零（在乘法群中不存在逆元）。")
        inv = other.inverse()
        return self * inv

    def __pow__(self, exponent: int):
        e = int(exponent)
        return FieldElement(pow(self.v, e, self.p), self.p)

    def _check_field(self, other):
        if not isinstance(other, FieldElement) or self.p != other.p:
            raise TypeError("兩個運算元必須屬於相同的 GF(p)。")

    def inverse(self):
        """計算乘法逆元：利用擴展歐幾里得演算法找到 x 使得 v*x ≡ 1 (mod p)"""
        if self.v == 0:
            raise ZeroDivisionError("零沒有乘法逆元。")
        # pow(self.v, -1, self.p) 在 Python 3.8+ 可用，但在某些環境下用擴展歐幾里得以保險。
        inv = pow(self.v, -1, self.p)
        return FieldElement(inv, self.p)

    @property
    def is_zero(self):
        return self.v == 0

# --- 群與體檢查工具（簡單暴力檢驗，小 p 適用） ---

def check_group_axioms(elements: List[FieldElement], op: Callable[[FieldElement, FieldElement], FieldElement]) -> Tuple[bool, dict]:
    """檢查封閉性、結合性、存在單位元、存在逆元。
    elements: 群的元素列表，op: 二元運算。
    回傳 (通過?, details dict)"""
    detail = {"closure": True, "associativity": True, "identity": None, "inverses": True}
    p = elements[0].p if elements else None

    # 封閉性
    for a in elements:
        for b in elements:
            r = op(a, b)
            if not any(r == x for x in elements):
                detail["closure"] = False
                break
        if not detail["closure"]:
            break

    # 結合律 a*(b*c) == (a*b)*c
    for a in elements:
        for b in elements:
            for c in elements:
                if op(a, op(b, c)) != op(op(a, b), c):
                    detail["associativity"] = False
                    break
            if not detail["associativity"]:
                break
        if not detail["associativity"]:
            break

    # 單位元（右左皆可）
    identity = None
    for e in elements:
        if all(op(e, a) == a and op(a, e) == a for a in elements):
            identity = e
            break
    detail["identity"] = identity

    # 逆元
    if identity is None:
        detail["inverses"] = False
    else:
        for a in elements:
            found = False
            for b in elements:
                if op(a, b) == identity and op(b, a) == identity:
                    found = True
                    break
            if not found:
                detail["inverses"] = False
                break

    ok = all([detail["closure"], detail["associativity"], detail["identity"] is not None, detail["inverses"]])
    return ok, detail


def check_distributivity(elements: List[FieldElement], add: Callable, mul: Callable) -> Tuple[bool, dict]:
    """檢查分配律：對所有 a,b,c 檢驗 a*(b+c) == a*b + a*c 及 (b+c)*a == b*a + c*a"""
    detail = {"left": True, "right": True}
    for a in elements:
        for b in elements:
            for c in elements:
                left = mul(a, add(b, c))
                right = add(mul(a, b), mul(a, c))
                if left != right:
                    detail["left"] = False
                left2 = mul(add(b, c), a)
                right2 = add(mul(b, a), mul(c, a))
                if left2 != right2:
                    detail["right"] = False
                if not detail["left"] and not detail["right"]:
                    return False, detail
    return True, detail

# --- 建立 GF(p) 類別，包含方便產生 FieldElement 的方法 ---
class GFp:
    def __init__(self, p: int):
        if p <= 1:
            raise ValueError("p 必須 > 1 且為質數（若非質數則不是域）。")
        self.p = int(p)

    def element(self, value: int) -> FieldElement:
        return FieldElement(value, self.p)

    def all_elements(self) -> List[FieldElement]:
        return [FieldElement(i, self.p) for i in range(self.p)]

    def additive_group_elements(self) -> List[FieldElement]:
        return self.all_elements()

    def multiplicative_group_elements(self) -> List[FieldElement]:
        return [FieldElement(i, self.p) for i in range(1, self.p)]

# --- 範例與自動測試 ---

def run_tests(p: int = 7):
    print(f"Testing GF({p}) ...")
    gf = GFp(p)
    elems = gf.all_elements()

    # 加法群檢查
    add_op = lambda a, b: a + b
    ok_add, detail_add = check_group_axioms(elems, add_op)
    print("Additive group OK:", ok_add)
    print(detail_add)

    # 乘法群（去掉 0）
    mul_elems = gf.multiplicative_group_elements()
    mul_op = lambda a, b: a * b
    ok_mul, detail_mul = check_group_axioms(mul_elems, mul_op)
    print("Multiplicative group (nonzero) OK:", ok_mul)
    print(detail_mul)

    # 分配律
    ok_dist, detail_dist = check_distributivity(elems, add_op, mul_op)
    print("Distributivity OK:", ok_dist)
    print(detail_dist)

    # 示範運算子重載
    a = gf.element(3)
    b = gf.element(5)
    print(f"Examples in GF({p}): a={a}, b={b}")
    print("a+b =", a + b)
    print("a-b =", a - b)
    print("a*b =", a * b)
    print("a/b =", a / b)
    print("a**3 =", a ** 3)

    return {"add_ok": ok_add, "mul_ok": ok_mul, "dist_ok": ok_dist}

if __name__ == '__main__':
    # 測試幾個小質數
    results = {}
    for p in [2, 3, 5, 7, 11]:
        try:
            results[p] = run_tests(p)
        except Exception as e:
            print(f"GF({p}) 測試失敗: {e}")
    print("Summary:", results)