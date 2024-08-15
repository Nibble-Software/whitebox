import types
import unittest
from typing import TypedDict

__all__ = ['whitebox']


class _EmptyStream:
    def write(self, *args, **kwargs):
        pass

    def flush(self, *args, **kwargs):
        pass


class WhiteBoxResult(TypedDict):
    passed: bool
    success_rate: float


def _run_code_with_tests(code: str, tests: str) -> unittest.TestResult:
    test_module = types.ModuleType('test_module')

    exec(code, test_module.__dict__)
    exec(tests, test_module.__dict__)

    # Step 3: Run the tests
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromModule(test_module)
    test_runner = unittest.TextTestRunner(verbosity=0, stream=_EmptyStream())
    test_result = test_runner.run(tests)
    # Return results, this could be customized further
    return test_result


def whitebox(student_code: str, teachers_tests: str) -> WhiteBoxResult:
    test_result = _run_code_with_tests(student_code, teachers_tests)
    success_rate = ((test_result.testsRun - len(test_result.failures) - len(test_result.errors))
                    / test_result.testsRun * 100)

    return {
        'passed': test_result.wasSuccessful(),
        'success_rate': success_rate
    }
