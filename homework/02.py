import cmath

def root2(a, b, c):
    delta = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(delta)) / (2*a)
    root2 = (-b - cmath.sqrt(delta)) / (2*a)

    f1 = a*root1**2 + b*root1 + c
    f2 = a*root2**2 + b*root2 + c

    print(cmath.isclose(f1, 0, rel_tol=1e-9))
    print(cmath.isclose(f2, 0, rel_tol=1e-9))

    return root1, root2

print(root2(1, -3, 2))
print(root2(1, 2, 5))
