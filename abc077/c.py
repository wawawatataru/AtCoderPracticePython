import bisect
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()
    ans = 0
    for i in range(n):
        x = bisect.bisect_left(a, b[i])
        y = bisect.bisect_right(c, b[i])
        ans += x * (n - y)
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
        input = """2
1 5
2 4
3 6"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """3
1 1 1
2 2 2
3 3 3"""
        output = """27"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """6
3 14 159 2 6 53
58 9 79 323 84 6
2643 383 2 79 50 288"""
        output = """87"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
