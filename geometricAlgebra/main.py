import galgebra.ga, sympy
base = galgebra.ga.Ga('\u0411', coords=sympy.symbols('x:z', real=True))
for up in range(base.n): assert sum(base.mv()[down] * base.g_inv[up, down] for down in range(base.n)) == base.mvr()[up] # base.g_inv is the inverse matrix of base.g
