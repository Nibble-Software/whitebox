from unittest import TestCase
from whitebox.whitebox import whitebox, WhiteBoxResult
import os


class TestWhiteBox(TestCase):
    def test_white_box(self) -> None:
        # Example student code (as a string)
        student_code = self._read_file("student_code.py")
        # Example teacher test cases (as a string)
        teacher_tests = self._read_file("teacher_code.py")

        expected = WhiteBoxResult(passed=True, success_rate=100.0)

        result = whitebox(student_code, teacher_tests)

        self.assertEqual(expected, result)

    def test_white_box_wrong_code(self) -> None:
        student_code = self._read_file("wrong_student_code.py")

        teacher_tests = self._read_file("teacher_code.py")

        expected = WhiteBoxResult(passed=False, success_rate=0.0)

        result = whitebox(student_code, teacher_tests)

        self.assertEqual(expected, result)

    def test_white_box_partially_wrong(self) -> None:
        student_code = self._read_file("partially_wrong_student_code.py")

        teacher_tests = self._read_file("teacher_test_operations.py")

        expected = WhiteBoxResult(passed=False, success_rate=50.0)

        result = whitebox(student_code, teacher_tests)

        self.assertEqual(expected, result)

    @staticmethod
    def _read_file(filename: str) -> str:
        file_path = os.path.join(os.path.dirname(__file__), "resources", filename)
        with open(file_path, "r") as file:
            return file.read()
