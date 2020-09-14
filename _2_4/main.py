response = []

import sympy
radius, alpha, gravity = sympy.symbols('a,alpha,g', positive=True)
theta = sympy.symbols('theta', real=True)
potentialM = sympy.symbols('M', positive=True) * gravity * radius * sympy.sin(sympy.pi - alpha - theta)
potentialm = sympy.symbols('m', positive=True) * gravity * radius * sympy.sin(theta - alpha)
phi = sympy.symbols('phi', real=True)
curve = sympy.Curve([radius * sympy.cos(phi), radius * sympy.sin(phi)], (phi, theta - alpha, theta + alpha))
y = sympy.symbols('y', real=True)
potentialLamda = sympy.line_integrate(sympy.symbols('lamda', positive=True) * gravity * y, curve, ['x',y])
motion = sympy.diff(potentialM + potentialm + potentialLamda, theta).trigsimp()
response += sympy.mathml(motion, printer='presentation'),

import json, pathlib
with open(pathlib.Path(__file__).resolve().parent / 'response.json', 'w') as _: _.write(json.dumps(response))
