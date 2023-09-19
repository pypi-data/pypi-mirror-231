# Setuptools for saoovqe package
from setuptools import setup

# Readme file as long_description:
long_description = ('================================================================\n' +
                    'State-averaged Orbital-optimized Variational Quantum Eigensolver\n' +
                    '================================================================\n')

setup(
        name='saoovqe',
        version='0.1.1',
        url='https://gitlab.com/MartinBeseda/sa-oo-vqe-qiskit',
        description='State-averaged Orbital-optimized Variational Quantum Eigensolver with the Qiskit library.',
        long_description=long_description,
        packages=['saoovqe']
)
