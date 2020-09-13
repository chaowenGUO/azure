response = []

import sympy
length,mass1,mass2,gravity,time=sympy.symbols('l,m_1,m_2,g,&tstrok;',positive=True)
x = sympy.Function('x', real=True)(time)
lagrangian = mass1 * x.diff(time)**2 / 2 + mass2 * x.diff(time)**2 / 2 - mass1 * gravity * x - mass2 * gravity * (length - x)
response += sympy.euler_equations(lagrangian),
