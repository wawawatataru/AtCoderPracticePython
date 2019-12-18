import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(n)]
    ans = set(a[0][1:])
    for i in range(1, n):
        ans = ans & set(a[i][1:])
    print(len(ans))


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
        input = """3 4
2 1 3
3 1 2 3
2 3 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5 5
4 2 3 4 5
4 1 3 4 5
4 1 2 4 5
4 1 2 3 5
4 1 2 3 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """1 30
3 5 10 30"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
