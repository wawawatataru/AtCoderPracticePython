import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = {}
    ans = 0
    for _ in range(n):
        a = int(input())
        if a in l:
            l[a] += 1
        else:
            l[a] = 1
    for v in l.values():
        if v % 2 == 1:
            ans += 1
    print(ans)


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
        input = """3
6
2
6"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4
2
5
5
2"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """6
12
22
16
22
18
12"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
