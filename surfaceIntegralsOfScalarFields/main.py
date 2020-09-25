response = []

import galgebra.ga, sympy, numpy, operator
radius, polar, azimuthal = sympy.symbols('r,theta,phi', positive=True)
X = (radius * sympy.sin(polar) * sympy.cos(azimuthal), radius * sympy.sin(polar) * sympy.sin(azimuthal), radius * sympy.cos(polar))
base = galgebra.ga.Ga('\u0411', coords=(polar, azimuthal), X=X)
#jacobian = sympy.Matrix(base.u).jacobian(base.coords)
#assert base.mv() == tuple(operator.matmul(*(numpy.array(_) for _ in (cartesian.mv(), jacobian))))
#assert base.g == sympy.trigsimp(jacobian.T @ jacobian)
#assert base.mvr() == tuple(operator.matmul(*(numpy.array(_) for _ in (base.mv(), base.g_inv))))
response += sympy.mathml(sympy.integrate((X[0]**2 + X[1]**2) * base.E().norm(), (polar, 0, sympy.pi / 2), (azimuthal, 0, sympy.pi / 2)), printer='presentation'),

import json, pathlib
with open(pathlib.Path(__file__).resolve().parent / 'response.json', 'w') as _: _.write(json.dumps(response))
