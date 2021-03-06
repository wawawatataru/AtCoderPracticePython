import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n = int(input())
    l = [int(input()) for i in range(n)]
    x = 0
    check = [True] * n
    ans = 0
    flg = False
    while (check[x]):
        if x == 1:
            flg = True
            break
        else:
            ans += 1
            check[x] = False
            x = l[x] - 1
    if flg:
        print(ans)
    else:
        print(-1)


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
3
1
2"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4
3
4
1
2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5
3
3
4
2
4"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
