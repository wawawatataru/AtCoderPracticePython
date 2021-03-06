import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    n, m = map(int, input().split())
    if n > m:
        print(str(m) * n)
    else:
        print(str(n) * m)


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
        input = """4 3"""
        output = """3333"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """7 7"""
        output = """7777777"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
