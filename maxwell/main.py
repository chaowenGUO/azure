response = []

import galgebra.ga, sympy

base = galgebra.ga.Ga('e',g=[sympy.symbols('c', real=True)**2,-1,-1,-1],coords=sympy.symbols('t,x:z',real=True))
potential = base.mv('&phi;',1,f=True)

response += sympy.mathml(potential.obj, printer='presentation'),

response += sympy.mathml((base.grad*base.grad*potential).obj, printer='presentation'),

import json, pathlib
with open(pathlib.Path(__file__).resolve().parent / 'response.json', 'w') as _: _.write(json.dumps(response))
