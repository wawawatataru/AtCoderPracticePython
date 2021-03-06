import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = [0] * (n + 1)
    l[0] = 2
    l[1] = 1
    if n == 1:
        print(1)
    else:
        for i in range(2, n + 1):
            l[i] = l[i - 1] + l[i - 2]
        print(l[n])


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
        input = """5"""
        output = """11"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """86"""
        output = """939587134549734843"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
