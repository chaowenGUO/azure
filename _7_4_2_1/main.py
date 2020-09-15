response = []

import galgebra.ga, sympy
radius, polar, azimuthal = sympy.symbols('r,theta,phi', real=True)
cartesian = (radius * sympy.sin(polar) * sympy.cos(azimuthal), radius * sympy.sin(polar) * sympy.sin(azimuthal), radius * sympy.cos(polar))
jacobian = sympy.Matrix(cartesian).jacobian((polar, azimuthal))
base = galgebra.ga.Ga('\u0411',g=sympy.trigsimp(jacobian.T @ jacobian).diagonal(),coords=(polar, azimuthal))
response += sympy.mathml(sympy.integrate((cartesian[0]**2 + cartesian[1]**2) * base.E().norm(), (polar, 0, sympy.pi / 2), (azimuthal, 0, sympy.pi / 2)), printer='presentation'),

import json, pathlib
with open(pathlib.Path(__file__).resolve().parent / 'response.json', 'w') as _: _.write(json.dumps(response))
