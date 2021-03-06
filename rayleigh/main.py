response = []

import sympy
position = sympy.symbols('x', real=True)
wavefunction = sympy.Function('&psi;', real=True)(position)
response += sympy.Integral(wavefunction * sympy.Function('&Hcirc;', real=True)(wavefunction), position) / sympy.Integral(wavefunction**2, position),

response += wavefunction,

def rayleigh(hamiltonian, wavefunction, limits):
    return sympy.integrate(wavefunction * hamiltonian(wavefunction), (position, *limits)) / sympy.integrate(wavefunction**2, (position, *limits))

#particle in a box
length, mass, hbar = sympy.symbols('l,m,&hbar;', positive=True)
wavefunction = position * (length - position)
hamiltonian = lambda wavefunction: -hbar**2 / 2 / mass * wavefunction.diff(position, 2)
exact = hbar**2 * sympy.pi**2 / 2 / mass / length**2  #曾谨言volume1 page65 3.2.7
response += sympy.N(rayleigh(hamiltonian, wavefunction, (0, length)) / exact - 1),

#harmonic oscillator
wavefunction = sympy.exp(-length * position**2)
angularFrequency = sympy.symbols('&varpi;', positive=True)
hamiltonian = lambda wavefunction: -hbar**2 / 2 / mass * wavefunction.diff(position, 2) + mass * angularFrequency**2 / 2 * position**2 * wavefunction
ground = rayleigh(hamiltonian, wavefunction, (-sympy.oo, sympy.oo))
response += ground.subs(length, sympy.solveset(ground.diff(length), length).sup),

basis = sympy.Matrix((
    position * (length - position),
    position**2 * (length - position)**2,
    position * (length - position) * (length / 2 - position),
    position**2 * (length - position)**2 * (length / 2 - position)
))
response += basis,

hamiltonian = sympy.Matrix.applyfunc(basis @ basis.applyfunc(lambda _: -hbar**2 / 2 / mass * _.diff(position, 2)).T, lambda _: sympy.integrate(_, (position, 0, length)))
response += hamiltonian,

overlap = sympy.Matrix.applyfunc(basis @ basis.T, lambda _: sympy.integrate(_, (position, 0, length)))
response += overlap,

LowerInverse = overlap.cholesky().inv()
coefficient, energy = sympy.Matrix.diagonalize(LowerInverse @ hamiltonian @ LowerInverse.T)
coefficient = LowerInverse.T @ sympy.Matrix.hstack(*map(
    lambda column: coefficient[:, column] / coefficient[:, column].norm(),
    range(coefficient.shape[-1])))
response += energy,

assert sympy.Matrix.applyfunc(coefficient.T @ overlap @ coefficient, sympy.cancel) == sympy.eye(len(basis))#wavefunction are orthonormal
wavefunction = basis.T @ coefficient
assert sympy.Matrix.applyfunc(wavefunction.T @ wavefunction, lambda _: sympy.integrate(_, (position, 0, length)).cancel()) == sympy.eye(len(wavefunction)) #wavefunction are orthonormal
response += wavefunction.T,

numerical = ((hbar, 1), (length, 1), (mass, 1))
import scipy.linalg, numpy
numericalEnergy, numericalCoefficient = scipy.linalg.eigh(*(numpy.array(_.subs(numerical), float) for _ in (hamiltonian, overlap)))

response += sympy.Matrix(numericalEnergy).T,

response += energy.subs(numerical).evalf(),

response += sympy.Matrix(numericalCoefficient),

response += coefficient.subs(numerical).evalf(),

response = [sympy.mathml(_, printer='presentation') for _ in response]

import json, pathlib
pathlib.Path(__file__).resolve().parent.joinpath('response.json').write_text(json.dumps(response))
