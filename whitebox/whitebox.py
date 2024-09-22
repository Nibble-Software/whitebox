__all__ = ["whitebox", "WhiteBoxResult"]
from .actions import perform_evaluation


class WhiteBoxResult:
    """
    Return type for the whitebox function.
    attributes:
    - passed: A boolean indicating the success of the tests.
    - success_rate: A float indicating the success rate of the tests.
    """

    def __init__(self, passed: bool, success_rate: float):
        self.passed = passed
        self.success_rate = success_rate

    def __eq__(self, other):
        if not isinstance(other, WhiteBoxResult):
            return False
        return self.passed == other.passed and self.success_rate == other.success_rate


def whitebox(student_code: str, teachers_tests: str) -> WhiteBoxResult:
    passed, success_rate = perform_evaluation(student_code, teachers_tests)
    return WhiteBoxResult(passed, success_rate)
