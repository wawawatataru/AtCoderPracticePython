import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    k, m = map(int, input().split())
    a = []
    if k == 1:
        print(m)
    else:
        for i in range(m - k + 1, m + k):
            a.append(str(i))
        print(" ".join(a))


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
        input = """3 7"""
        output = """5 6 7 8 9"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4 0"""
        output = """-3 -2 -1 0 1 2 3"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """1 100"""
        output = """100"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
