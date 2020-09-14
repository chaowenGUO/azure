response = []

import sympy
radius,alpha,gravity=sympy.symbols('a,alpha,g',positive=True)
theta=sympy.symbols('theta',real=True)
potentialM=sympy.symbols('M',positive=True)*Gravity*Radius*sympy.sin(sympy.pi-Alpha-theta)
potentialm=sympy.symbols('m',positive=True)*Gravity*Radius*sympy.sin(theta-Alpha)
phi=sympy.symbols('phi',real=True)
curve=sympy.Curve([Radius*sympy.cos(phi),Radius*sympy.sin(phi)],(phi,theta-Alpha,theta+Alpha))
y=sympy.symbols('y',real=True)
potentialLamda=sympy.line_integrate(sympy.symbols('lamda',positive=True)*Gravity*y,curve,['x',y])
motion=sympy.diff(potentialM+potentialm+potentialLamda,theta).trigsimp()
response += sympy.mathml(motion, printer='presentation'),

import json, pathlib
with open(pathlib.Path(__file__).resolve().parent / 'response.json', 'w') as _: _.write(json.dumps(response))
