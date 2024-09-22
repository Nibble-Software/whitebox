import types
import unittest


class _EmptyStream:
    def write(self, *args, **kwargs):
        pass

    def flush(self, *args, **kwargs):
        pass


def _run_code_with_tests(code: str, tests: str) -> unittest.TestResult:
    test_module = types.ModuleType("test_module")

    exec(code, test_module.__dict__)
    exec(tests, test_module.__dict__)

    # Step 3: Run the tests
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromModule(test_module)
    test_runner = unittest.TextTestRunner(verbosity=0, stream=_EmptyStream())  # noqa
    test_result = test_runner.run(tests)
    # Return results, this could be customized further
    return test_result


def perform_evaluation(student_code: str, teachers_tests: str) -> tuple[bool, float]:
    test_result = _run_code_with_tests(student_code, teachers_tests)
    tests_run = test_result.testsRun
    failures = len(test_result.failures)
    errors = len(test_result.errors)
    tests_failed = failures + errors
    success_rate = (tests_run - tests_failed) / tests_run * 100

    return test_result.wasSuccessful(), success_rate
