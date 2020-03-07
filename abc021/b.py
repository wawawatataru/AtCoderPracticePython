import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    m = int(input())
    j = list(map(int, input().split()))
    s = l + j
    o = set(s)
    if len(s) == len(o):
        print("YES")
    else:
        print("NO")


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input1(self):
        print("test_input1")
        input = """5
1 5
3
3 4 2"""
        output = """YES"""
        self.assertIO(input, output)

    def test_input2(self):
        print("test_input2")
        input = """7
1 3
4
2 4 2 7"""
        output = """NO"""
        self.assertIO(input, output)

    def test_input3(self):
        print("test_input3")
        input = """4
1 4
3
2 1 3"""
        output = """NO"""
        self.assertIO(input, output)

    def test_input4(self):
        print("test_input4")
        input = """4
1 4
3
2 4 3"""
        output = """NO"""
        self.assertIO(input, output)

    def test_input5(self):
        print("test_input5")
        input = """20
1 4
12
2 3 5 7 8 9 10 11 12 15 13 14"""
        output = """YES"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
