import galgebra.ga, sympy, operator, numpy
base = galgebra.ga.Ga('\u0411', coords=sympy.symbols('x:z', real=True))
assert base.mvr() == tuple(operator.matmul(*(numpy.array(_) for _ in (base.mv(), base.g_inv)))) # base.g_inv is the inverse matrix of base.g
for down in range(base.n): 
    for up in range(base.n): assert (base.mv()[down] | base.mvr()[up]).simplify() == sympy.KroneckerDelta(down, up)
