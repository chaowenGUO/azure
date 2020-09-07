response = []

import galgebra.ga, sympy

base = galgebra.ga.Ga('e*t|x|y|z',g=[1,-1,-1,-1],coords=sympy.symbols('t,x,y,z',real=True))
potential = base.mv('&phi;','vector',f=True).subs(sympy.symbols('t',real=True), sympy.symbols('t',real=True) * sympy.symbols('c',real=True))

response += sympy.mathml(potential.obj, printer='presentation'),

response += sympy.mathml((base.grad*base.grad*potential).obj.subs(sympy.symbols('t',real=True) * sympy.symbols('c',real=True), sympy.symbols('t',real=True)).obj.doit(), printer='presentation'),

import json, pathlib
with open(pathlib.Path(__file__).resolve().parent / 'response.json', 'w') as _: _.write(json.dumps(response))
