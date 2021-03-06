import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, c, d = map(int, input().split())
    x = c - a
    y = d - b
    print(c-y, d+x, a-y, b+x)


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
        input = """0 0 0 1"""
        output = """-1 1 -1 0"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2 3 6 6"""
        output = """3 10 -1 7"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """31 -41 -59 26"""
        output = """-126 -64 -36 -131"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
