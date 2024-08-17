from unittest import TestCase
from whitebox.whitebox import whitebox, WhiteBoxResult


class TestWhiteBox(TestCase):

    def test_white_box(self) -> None:
        # Example student code (as a string)
        with open('../tests/resources/student_code.py', 'r') as file:
            student_code = file.read()
        # Example teacher test cases (as a string)
        with open('../tests/resources/teacher_code.py', 'r') as file:
            teacher_tests = file.read()

        expected = WhiteBoxResult(passed=True, success_rate=100.0)

        result = whitebox(student_code, teacher_tests)

        self.assertEqual(expected, result)

    def test_white_box_wrong_code(self) -> None:
        with open('../tests/resources/wrong_student_code.py', 'r') as file:
            student_code = file.read()

        with open('../tests/resources/teacher_code.py', 'r') as file:
            teacher_tests = file.read()

        expected = WhiteBoxResult(passed=False, success_rate=0.0)

        result = whitebox(student_code, teacher_tests)

        self.assertEqual(expected, result)

    def test_white_box_partially_wrong(self) -> None:
        with open('../tests/resources/partially_wrong_student_code.py', 'r') as file:
            student_code = file.read()

        with open('../tests/resources/teacher_test_operations.py') as file:
            teacher_tests = file.read()

        expected = WhiteBoxResult(passed=False, success_rate=50.0)

        result = whitebox(student_code, teacher_tests)

        self.assertEqual(expected, result)
