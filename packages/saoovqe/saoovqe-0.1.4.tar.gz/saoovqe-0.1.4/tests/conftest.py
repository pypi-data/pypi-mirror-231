"""
Configuration file for Pytest automatic tests
"""

import pytest


def pytest_configure():
    """
    Function defining properties to be shared between tests
    """

    # SA-VQE solver without orbital optimization
    pytest.solver = None

    # SA-VQE solver with active orbital-optimization
    pytest.solver_oo = None

    # SA-VQE solver with active orbital-optimization optimizing only 8 orbitals
    pytest.solver_oo_8 = None

    # SA-VQE solver with active orbital-optimization for 3 active MOs containing 4 electrons
    pytest.solver_oo_4_3 = None
