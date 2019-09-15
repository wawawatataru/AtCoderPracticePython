import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b = map(int, input().split())
    c = 0
    d = 1
    while (True):
        if d >= b:
            break
        d = d + a - 1
        c += 1
    print(c)


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
        input = """4 10"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """8 9"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """8 8"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
