import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, a, b = map(int, input().split())
    c = n // (a + b)
    d = n % (a+b)
    print(c * a + min(d, a))


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input_1(self):
        print("test_input_1")
        input = """8 3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """8 0 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """6 2 4"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
