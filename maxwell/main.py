import galgebra, sympy

base=galgebra.ga.Ga('e*t|x|y|z',g=[1,-1,-1,-1],coords=sympy.symbols('t,x,y,z',real=True))
potential=base.mv('&phi;','vector',f=True)

potential
