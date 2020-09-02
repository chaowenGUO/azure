import sympy, js
x= sympy.symbols('x', real=True)
js.console.log(str(sympy.printing.mathml.mathml(sympy.Integral(sympy.sqrt(1/x), x))))
