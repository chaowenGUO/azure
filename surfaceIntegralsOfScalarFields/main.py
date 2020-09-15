response = []

import galgebra.ga, sympy
radius, polar, azimuthal = sympy.symbols('r,theta,phi', real=True)
cartesian = galgebra.ga.Ga('\u0411', g=(1,) * 3, coords=sympy.symbols('x:z', real=True))
base = cartesian.sm((radius * sympy.sin(polar) * sympy.cos(azimuthal), radius * sympy.sin(polar) * sympy.sin(azimuthal), radius * sympy.cos(polar)), (polar, azimuthal), root='\u0411')
response += sympy.mathml(sympy.integrate((base.u[0]**2 + base.u[1]**2) * base.E().norm(), (polar, 0, sympy.pi / 2), (azimuthal, 0, sympy.pi / 2)), printer='presentation'),

import json, pathlib
with open(pathlib.Path(__file__).resolve().parent / 'response.json', 'w') as _: _.write(json.dumps(response))
