import galgebra.ga, sympy
base = galgebra.ga.Ga('\u0411', coords=sympy.symbols('x:z', real=True))
for left in range(base.n): assert sum(base.mv()[right] * base.g_inv[left, right] for right in range(base.n)) == base.mvr()[left] # base.g_inv is the inverse matrix of base.g
