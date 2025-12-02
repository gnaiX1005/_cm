import cmath

def root3(a, b, c, d):
    # 確保 a != 0 才是三次方程式
    if a == 0:
        raise ValueError("a 不能為 0，否則不是三次方程式")

    # 歸一化 （讓方程變成 x^3 + A x^2 + B x + C）
    A = b / a
    B = c / a
    C = d / a

    # 降次：x = t - A/3，使消去平方項，變成 t^3 + p t + q
    p = B - A**2 / 3
    q = (2*A**3) / 27 - (A*B) / 3 + C

    # 判別式
    Δ = (q/2)**2 + (p/3)**3

    # Cardano 公式
    sqrt_term = cmath.sqrt(Δ)
    u = (-q/2 + sqrt_term) ** (1/3)
    v = (-q/2 - sqrt_term) ** (1/3)

    # 三個根
    t1 = u + v
    # 三個複數根的 ω, ω²（立方根的三個解）
    omega = -0.5 + cmath.sqrt(3)/2 * 1j
    omega2 = -0.5 - cmath.sqrt(3)/2 * 1j

    t2 = u * omega + v * omega2
    t3 = u * omega2 + v * omega

    # 換回 x = t - A/3
    roots = [
        t1 - A/3,
        t2 - A/3,
        t3 - A/3
    ]

    return roots

print(root3(1, 0, 0, -1))   # x^3 - 1 = 0
