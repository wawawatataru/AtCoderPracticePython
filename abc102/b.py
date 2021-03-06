import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    print(l[-1] - l[0])


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
        input = """4
1 4 6 3"""
        output = """5"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """2
1000000000 1"""
        output = """999999999"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5
1 1 1 1 1"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
