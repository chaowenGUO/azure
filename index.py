import sympy, js
x= sympy.symbols('x', real=True)
sympy.mathml(sympy.Integral(sympy.sqrt(1/x), x), printer='presentation')
