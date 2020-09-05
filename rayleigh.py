out = []

def rayleigh(hamiltonian, wavefunction, limits):
    return sympy.integrate(wavefunction * hamiltonian(wavefunction), (position, *limits)) / sympy.integrate(wavefunction**2,(position, *limits))

#particle in a box
import sympy
length, mass, hbar = sympy.symbols('l,m,hbar', positive=True)
position = sympy.symbols('x', real=True)
wavefunction = position * (length - position)
hamiltonian = lambda wavefunction: -hbar**2 / 2 / mass * wavefunction.diff(position, 2)
exact = hbar**2 * sympy.pi**2 / 2 / mass / length**2  #曾谨言volume1 page65 3.2.7
out += sympy.N(rayleigh(hamiltonian, wavefunction, [0, length]) / exact - 1),

#harmonic oscillator
wavefunction = sympy.exp(-length * position**2)
angularFrequency = sympy.symbols('varpi', positive=True)
hamiltonian = lambda wavefunction: -hbar**2 / 2 / mass * wavefunction.diff(position, 2) + mass * angularFrequency**2 / 2 * position**2 * wavefunction
ground = rayleigh(hamiltonian, wavefunction, [-sympy.oo, sympy.oo])
out += sympy.mathml(ground.subs(length, sympy.solveset(ground.diff(length), length).sup), printer='presentation'),

basis = sympy.Matrix([
    position * (length - position),
    position**2 * (length - position)**2,
    position * (length - position) * (length / 2 - position),
    position**2 * (length - position)**2 * (length / 2 - position)
])
#js.document.body.append(js.MathJax.mathml2chtml(''.join(('<math display="block">', sympy.mathml(basis, printer='presentation'), '</math>'))))

hamiltonian = (basis @ basis.applyfunc(lambda element: -hbar**2 / 2 / mass * element.diff(position, 2)).T).applyfunc(lambda element: sympy.integrate(element, (position, 0, length)))
#js.document.body.append(js.MathJax.mathml2chtml(''.join(('<math display="block">', sympy.mathml(hamiltonian, printer='presentation'), '</math>'))))

overlap = (basis @ basis.T).applyfunc(lambda element: sympy.integrate(element, (position, 0, length)))
#js.document.body.append(js.MathJax.mathml2chtml(''.join(('<math display="block">', sympy.mathml(overlap, printer='presentation'), '</math>'))))

LowerInverse = overlap.cholesky().inv()
coefficient, energy = (LowerInverse @ hamiltonian @ LowerInverse.T).diagonalize()
coefficient = LowerInverse.T @ sympy.Matrix.hstack(*map(
    lambda column: coefficient[:, column] / coefficient[:, column].norm(),
    range(coefficient.shape[-1])))
#js.document.body.append(js.MathJax.mathml2chtml(''.join(('<math display="block">', sympy.mathml(energy, printer='presentation'), '</math>'))))

assert (coefficient.T @ overlap @ coefficient).applyfunc(sympy.cancel) == sympy.eye(len(basis))  
#wavefunction are orthonormal
wavefunction = basis.T @ coefficient
assert ((wavefunction.T @ wavefunction
        ).applyfunc(lambda element: sympy.integrate(element, (position, 0, length)).cancel()) 
        == sympy.eye(len(wavefunction)))  #wavefunction are orthonormal
#js.document.body.append(js.MathJax.mathml2chtml(''.join(('<math display="block">', sympy.mathml(wavefunction.T, printer='presentation'), '</math>'))))

numerical = [(hbar, 1), (length, 1), (mass, 1)]
import scipy.linalg
numericalEnergy, numericalCoefficient = scipy.linalg.eigh(
    sympy.matrix2numpy(hamiltonian.subs(numerical), float),
    sympy.matrix2numpy(overlap.subs(numerical), float))
#js.document.body.append(numericalEnergy)

#js.document.body.append(js.MathJax.mathml2chtml(''.join(('<math display="block">', sympy.mathml(energy.subs(numerical).evalf(), printer='presentation'), '</math>'))))

#js.document.body.append(numericalCoefficient)

#js.document.body.append(js.MathJax.mathml2chtml(''.join(('<math display="block">', sympy.mathml(coefficient.subs(numerical).evalf(), printer='presentation'), '</math>'))))

import json
with open('out.json', 'w') as _: _.write(json.dumps(out, default=str))

import git, pathlib
with git.Repo(pathlib.Path(__file__).resolve().parent) as repository:
    repository.config_writer().set_value('user', 'name', 'Your Name').release()
    repository.config_writer().set_value('user', 'email', 'you@example.com').release()
    repository.index.commit('')#git commit --allow-empty-message -m ''
    repository.remote().push()
