#!/usr/bin/env python3
"""
Example script for utilization of SA-OO-VQE solver on the computation of formaldimine (methylene imine) molecule
energies for the lowest 2 singlet states, gradients of the potential energy surface and the corresponding non-adiabatic
couplings.
"""
import numpy as np
from icecream import ic
from qiskit import QuantumCircuit
from qiskit.algorithms.optimizers import SciPyOptimizer
from qiskit.primitives import Estimator
from qiskit.quantum_info import Statevector
import psi4

import saoovqe

R_BOHR_ANG = 0.5291772105638411

def gen_formaldimine_geom(alpha, phi):
    """
    Function to generate an .xyz file for formaldimine, aligns N-C bond with
    the z-axis.
    """
    variables = [1.498047, 1.066797, 0.987109, 118.359375] + [alpha, phi]
    string_geo_dum = """0 1
                    N
                    C 1 {0}
                    H 2 {1}  1 {3}
                    H 2 {1}  1 {3} 3 180
                    H 1 {2}  2 {4} 3 {5}
                    symmetry c1
                    """.format(*variables)

    psi4.core.set_output_file("output_Psi4.txt", False)
    molecule_dum = psi4.geometry(string_geo_dum)
    molecule_dum.translate(psi4.core.Vector3(-molecule_dum.x(0),
                                             -molecule_dum.y(0),
                                             -molecule_dum.z(0)))
    mol_geom_dum = np.copy(molecule_dum.geometry().np) * R_BOHR_ANG
    if not np.isclose(mol_geom_dum[1, 1], 0.):
        mol_geom_dum[:, [1, 2]] = mol_geom_dum[:, [2, 1]]
        mol_geom_dum[4, 0] = -mol_geom_dum[4, 0]
        print("switched axes, new geom:", mol_geom_dum)
    return mol_geom_dum

#######################
# Method specification
#######################
estimator = Estimator()

n_states = 2
repetitions = 1

#########################
# Molecule specification
#########################
alpha = 130
phi = 90
geometry_coordinate = gen_formaldimine_geom(alpha, phi)

# geometry = [('N', [0.000000000000, 0.000000000000, 0.000000000000]),
#             ('C', [0.000000000000, 0.000000000000, 1.498047000000]),
#             ('H', [0.000000000000, -0.938765985000, 2.004775984000]),
#             ('H', [0.000000000000, 0.938765985000, 2.004775984000]),
#             ('H', [-0.744681452, -0.131307432, -0.634501434])]

geometry = [('N', geometry_coordinate[0]),
            ('C', geometry_coordinate[1]),
            ('H', geometry_coordinate[2]),
            ('H', geometry_coordinate[3]),
            ('H', geometry_coordinate[4])]


n_orbs_active = 3
n_elec_active = 4
charge = 0
spin = 0
multiplicity = 1
basis =  "sto-3g" #"cc-pVDZ"

#########################################################

# Weights of the ensemble:
problem = saoovqe.ProblemSet(geometry, charge, multiplicity, n_elec_active, n_orbs_active, basis)

# Step 1: Initialization - states |phiA>, |phiB>
initial_circuits = saoovqe.OrthogonalCircuitSet.from_problem_set(n_states, problem)

# Define the ansatz circuit:
#
# Operator Û(theta)
ansatz = saoovqe.Ansatz.from_ProblemSet(saoovqe.AnsatzType.GUCCSD,
                                        problem,
                                        repetitions,
                                        qubit_mapper=problem.fermionic_mapper)

# Perform SA-VQE procedure
saoovqe_solver = saoovqe.SAOOVQE(estimator,
                                 initial_circuits,
                                 ansatz,
                                 problem,
                                 orbital_optimization_settings={})

# # TODO debug - remove!
ic(problem.frozen_orbitals_indices)
ic(problem.active_orbitals_indices)
ic(problem.virtual_orbitals_indices)
# c1 = initial_circuits.circuits[0]
# c2 = initial_circuits.circuits[1]
# # crot = c1.copy()
# crot = saoovqe_solver._create_trans_circ_imag(0)
#
# print(c1)
# print(c2)
# print(crot)
#
# assert np.allclose((Statevector(c1).data + 1j*Statevector(c2).data).real/np.sqrt(2), Statevector(crot).data.real)
# print(f'The imag circuit is correct. True or False? \n{np.allclose((Statevector(c1).data + 1j*Statevector(c2).data).real/np.sqrt(2), Statevector(crot).data.real)}')
# exit(-1)

energies = saoovqe_solver.get_energy(SciPyOptimizer('SLSQP', options={'maxiter': 500, 'ftol': 1e-8}))
#energies = saoovqe_solver.get_energy(SciPyOptimizer('COBYLA', options={'maxiter': 1000, 'ftol': 1e-8}))


print('\n============== SA-OO-VQE Results ==============')
print(f'Optimized ansatz parameters: {saoovqe_solver.ansatz_param_values}')
print(f'Optimized (state-resolution) angle: {saoovqe_solver.resolution_angle}')
print(f'Energies: {energies}')

print('\n============== Gradients ==============')
for state_idx in range(2):
    for atom_idx in range(len(geometry)):
        print(state_idx, atom_idx, saoovqe_solver.eval_eng_gradient(state_idx, atom_idx))

print('\n============== Total non-adiabatic couplings ==============')
for atom_idx in range(len(geometry)):
    print(atom_idx, saoovqe_solver.eval_nac(atom_idx))

print('\n============== CI non-adiabatic couplings ==============')
for atom_idx in range(len(geometry)):
    print(atom_idx, saoovqe_solver.ci_nacs[atom_idx])

print('\n============== CSF non-adiabatic couplings ==============')
for atom_idx in range(len(geometry)):
    print(atom_idx, saoovqe_solver.csf_nacs[atom_idx])
