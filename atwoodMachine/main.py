response = []

import sympy
length, mass1, mass2, gravity, time=sympy.symbols('l,m_1,m_2,g,&tstrok;',positive=True)
x = sympy.Function('x', negative=True)(time)
lagrangian = mass1 * x.diff(time)**2 / 2 - mass1 * gravity * x + mass2 * x.diff(time)**2 / 2 - mass2 * gravity * (length - x)
solution = sum(key * sympy.factor(value) for key, value in sympy.dsolve(sympy.euler_equations(lagrangian)[0]).rhs.expand().collect(time, evaluate=False).items())
response += solution,

constraint=sympy.Function('V', real=True)(x)
lagrangian = mass1 * x.diff(time)**2 / 2 - mass1 * gravity * x - constraint
force = sympy.cancel(sympy.solveset(sympy.euler_equations(mass1 * x.diff(time)**2 / 2 - mass1 * gravity * x - constraint, x)[0], -constraint.diff(x)).args[0].subs(x, solution).doit())
response += force,

response = [sympy.mathml(_, printer='presentation') for _ in response]

import json, pathlib
pathlib.Path(__file__).resolve().parent.joinpath('response.json').write_text(json.dumps(response))
