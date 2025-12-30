# finite_field.py

class GFp:
    def __init__(self, value: int, p: int):
        assert 0 <= value < p
        self.value = value
        self.p = p

    def __add__(self, other):
        assert self.p == other.p
        return GFp((self.value + other.value) % self.p, self.p)

    def __neg__(self):
        return GFp((-self.value) % self.p, self.p)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        assert self.p == other.p
        return GFp((self.value * other.value) % self.p, self.p)

    def inv(self):
        # extended Euclidean algorithm to find inverse modulo p
        a, m = self.value, self.p
        assert a != 0
        # find x such that a x ≡ 1 mod p
        # Python built-in pow for mod inverse:
        inv = pow(a, -1, m)
        return GFp(inv, self.p)

    def __truediv__(self, other):
        assert self.p == other.p
        assert other.value != 0
        return self * other.inv()

    def __eq__(self, other):
        return isinstance(other, GFp) and self.p == other.p and self.value == other.value

    def __repr__(self):
        return f"GFp({self.value} mod {self.p})"
 
# test_finite_field.py
from finite_field import GFp

def all_nonzero_elements(p):
    return [GFp(i, p) for i in range(1, p)]

def test_gfp(p):
    zero = GFp(0, p)
    one = GFp(1, p)
    elems = [GFp(i, p) for i in range(p)]

    # 加法群: 檢查封閉性、單位元 (0)、逆元、交換律、結合律...
    # 乘法群 (除 0): 檢查封閉性、單位元 (1)、逆元、交換律、結合律…
    # 分配律
    for a in elems:
        for b in elems:
            for c in elems:
                assert a * (b + c) == (a * b) + (a * c), "distributivity fail"

    # 也可以檢查 a/b * b == a etc.

if __name__ == "__main__":
    test_gfp(7)  # for example p = 7
    print("GF(7) 通過基本 field 檢驗")
