import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b = map(int, input().split())
    print(max(a+b, a-b, a*b))


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
        input = """-13 3"""
        output = """-10"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """1 -33"""
        output = """34"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """13 3"""
        output = """39"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
