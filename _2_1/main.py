response = []

import sympy
theta = sympy.symbols('theta',real=True)
y= (sympy.symbols('l',positive=True) / 2 - sympy.symbols('a',positive=True) * sympy.csc(theta)) * sympy.cos(theta)
motion = sympy.diff(sympy.symbols('m',positive=True) * sympy.symbols('g',positive=True) * y,theta).trigsimp()
response += sympy.mathml(next(_ for _ in sympy.solve(motion, theta) if not _.has(sympy.pi)), printer='presentation'),

import json, pathlib
pathlib.Path(__file__).resolve().parent.joinpath('response.json').write_text(json.dumps(response))
