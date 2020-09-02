def rayleigh(hamiltonian, wavefunction, limits):
    return (sympy.integrate(wavefunction * hamiltonian(wavefunction), (position, *limits)) 
            / sympy.integrate(wavefunction**2,(position, *limits)))

#particle in a box
import sympy, js
length, mass, hbar = sympy.symbols('l,m,hbar', positive=True)
position = sympy.symbols('x', real=True)
wavefunction = position * (length - position)
hamiltonian = lambda wavefunction: -hbar**2 / 2 / mass * wavefunction.diff(position, 2)
exact = hbar**2 * sympy.pi**2 / 2 / mass / length**2  #曾谨言volume1 page65 3.2.7
js.console.log(sympy.N(rayleigh(hamiltonian, wavefunction, [0, length]) / exact - 1))
