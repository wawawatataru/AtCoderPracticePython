import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, q = map(int, input().split())
    l = [list(map(int, input().split())) for i in range(q)]
    ans = [0] * n
    for i in range(q):
        s = l[i][0] - 1
        e = l[i][1]
        a = l[i][2]
        for j in range(s, e):
            ans[j] = a
    for i in range(n):
        print(ans[i])


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
        input = """5 2
1 3 10
2 4 20"""
        output = """10
20
20
20
0"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """10 4
2 7 22
3 5 4
6 10 1
4 4 12"""
        output = """0
22
4
12
4
1
1
1
1
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
