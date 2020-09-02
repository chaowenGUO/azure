import sympy, js
x= sympy.symbols('x', real=True)
js.console.log(sympy.latex(sympy.Integral(sympy.sqrt(1/x), x)))
