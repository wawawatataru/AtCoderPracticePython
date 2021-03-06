import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b, c = map(int, input().split())
    max_a = 0
    max_b = 0
    if a == b:
        max_a += 1
    if a == c:
        max_a += 1
    if b == c:
        max_b += 1
    if max(max_a, max_b) == 1:
        print("Yes")
    else:
        print("No")


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
        input = """5 7 5"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """4 4 4"""
        output = """No"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """4 9 6"""
        output = """No"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """3 3 4"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
