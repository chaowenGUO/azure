response = []

import sympy
theta = sympy.symbols('theta',real=True)
y= (sympy.symbols('l',positive=True) / 2 - sympy.symbols('a',positive=True) * sympy.csc(theta)) * sympy.cos(theta)
motion = sympy.diff(sympy.symbols('m',positive=True) * sympy.symbols('g',positive=True) * y,theta).trigsimp()
response += motion,

response = [sympy.mathml(_, printer='presentation') for _ in response]
import json, pathlib
with open(pathlib.Path(__file__).resolve().parent / 'response.json', 'w') as _: _.write(json.dumps(response))
