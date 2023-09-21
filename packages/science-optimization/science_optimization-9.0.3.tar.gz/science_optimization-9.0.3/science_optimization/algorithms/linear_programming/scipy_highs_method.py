"""
HiGHS method that automatically chooses between 'highs-ds' and 'highs-ipm'
"""
from .scipy_base_linear import ScipyBaseLinear


class ScipyHighsMethod(ScipyBaseLinear):
    """Scipy highs method.

    """

    def __init__(self, n_max: int=None):
        """Constructor of highs optimization.

            Args:
                n_max: (int) maximum number of iterations.

        """

        super().__init__(method='highs', n_max=n_max)

