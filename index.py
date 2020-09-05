def rayleigh(hamiltonian, wavefunction, limits):
    return sympy.integrate(wavefunction * hamiltonian(wavefunction), (position, *limits)) / sympy.integrate(wavefunction**2,(position, *limits))

#particle in a box
import sympy, js
length, mass, hbar = sympy.symbols('l,m,hbar', positive=True)
position = sympy.symbols('x', real=True)
wavefunction = position * (length - position)
hamiltonian = lambda wavefunction: -hbar**2 / 2 / mass * wavefunction.diff(position, 2)
exact = hbar**2 * sympy.pi**2 / 2 / mass / length**2  #曾谨言volume1 page65 3.2.7
js.document.body.append(sympy.N(rayleigh(hamiltonian, wavefunction, [0, length]) / exact - 1))

#harmonic oscillator
wavefunction = sympy.exp(-length * position**2)
angularFrequency = sympy.symbols('varpi', positive=True)
hamiltonian = lambda wavefunction: -hbar**2 / 2 / mass * wavefunction.diff(position, 2) + mass * angularFrequency**2 / 2 * position**2 * wavefunction
ground = rayleigh(hamiltonian, wavefunction, [-sympy.oo, sympy.oo])
js.document.body.append(js.MathJax.mathml2chtml(''.join(('<math>', sympy.mathml(ground.subs(length, sympy.solveset(ground.diff(length), length).sup), printer='presentation'), '</math>'))))

basis = sympy.Matrix([
    position * (length - position),
    position**2 * (length - position)**2,
    position * (length - position) * (length / 2 - position),
    position**2 * (length - position)**2 * (length / 2 - position)
])
js.document.body.append(js.MathJax.mathml2chtml(''.join(('<math>', sympy.mathml(basis, printer='presentation'), '</math>'))))
