import sympy, js
x= sympy.symbols('x', real=True)
js.console.log(str(sympy.latex(sympy.Integral(sympy.sqrt(1/x), x))))
