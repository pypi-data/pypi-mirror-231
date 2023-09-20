import numpy as np
from qiskit import Aer
from qiskit.providers.aer import QasmSimulator
from qiskit_nature.converters.second_quantization import QubitConverter
from qiskit_nature.drivers import Molecule
from qiskit_nature.drivers.second_quantization import ElectronicStructureDriverType, ElectronicStructureMoleculeDriver
from qiskit_nature.mappers.second_quantization import JordanWignerMapper
from qiskit_nature.problems.second_quantization.electronic import ElectronicStructureProblem

import saoovqe

################ METHOD INITIALIZATIONS #################
backend = QasmSimulator(method='matrix_product_state')
backend_state = Aer.get_backend(
    'statevector_simulator')  # Aer: provides access to several simulators that are included with Qiskit and run on
# your local machine.
method = ["SA-VQE", "SA-OO-VQE"][0]
n_states = 2
weights_choice = ["equi", "decreasing"][0]
ansatz_choice = ["TwoLocal", "UCCD", "UCCSD", "GUCCD", "GUCCSD"][3]
repetitions = 2
opt_method = ['L-BFGS-B', 'cma', 'SLSQP'][0]
basinhopping = False
n_hopping = 4
opt_maxiter = 1000  # number of iterations of the classical optimizer
sampling = ["noiseless", "noisy"][0]  # To activate sampling noise or not
n_shots = 1e6
verbose = False
############### MOLECULE INITIALIZATIONS ################
geometry = [['H', [0., 0., 0.]],
            ['H', [1., 0., 0.]]]
charge = 0
multiplicity = 1
basis = "sto3g"
#########################################################

# Weights of the ensemble:
weights = saoovqe.utils.weights_attribution(n_states, weights_choice)

# Define the Molecule and QMolecule objects (using the PYSCF driver):
molecule = Molecule(geometry=geometry, charge=charge, multiplicity=multiplicity)
driver = ElectronicStructureMoleculeDriver(molecule, basis=basis, driver_type=ElectronicStructureDriverType.PYSCF)
problem = ElectronicStructureProblem(driver)
qmolecule = driver.run()

# Extract informations from the QMolecule object:
n_spinor = qmolecule.get_property("ParticleNumber")._num_spin_orbitals
n_alpha = qmolecule.get_property("ParticleNumber")._num_alpha
n_beta = qmolecule.get_property("ParticleNumber")._num_beta
n_elec = n_alpha + n_beta
n_particle = (n_alpha, n_beta)
n_qubits = n_spinor

# Build the second-quantized Hamiltonian:
second_q_ops = problem.second_q_ops()
hamiltonian = second_q_ops['ElectronicEnergy']

# Build the Qubit Hamiltonian using the Jordan-Wigner transformation:
jw_mapper = JordanWignerMapper()
jw_converter = QubitConverter(jw_mapper)
H_qubit = jw_converter.convert(hamiltonian)

# Create the initial circuits (orthonormal states):
initial_circuits = saoovqe.circuits.create_initial_circuits(n_states, n_qubits, n_particle, jw_converter)
print(initial_circuits[0].draw())
print(initial_circuits[1].draw())

# Define the ansatz circuit:
ansatz = saoovqe.ansatz.vqe_ansatz(ansatz_choice, n_qubits, n_particle, n_spinor, repetitions,
                                   qubit_converter=jw_converter)
print(ansatz.draw())

# Perform SA-VQE:
param_values, energies, states = saoovqe.vqe_optimization.sa_vqe_optimization(backend, backend_state, initial_circuits,
                                                                              ansatz, H_qubit, weights, opt_method,
                                                                              basinhopping, n_hopping=n_hopping,
                                                                              maxiter=opt_maxiter, verbose=True)

# Gather all states from the ensemble
states_VQE = np.matrix(states).T

print(f'energies: {energies}')
