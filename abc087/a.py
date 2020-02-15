import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    x = int(input())
    a = int(input())
    b = int(input())
    print((x-a) % b)


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
        input = """1234
150
100"""
        output = """84"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """1000
108
108"""
        output = """28"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """579
123
456"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """7477
549
593"""
        output = """405"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
