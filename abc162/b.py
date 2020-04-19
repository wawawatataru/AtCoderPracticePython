import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
      if i % 3 != 0 and i % 5 != 0:
        ans += i
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
        input = """15"""
        output = """60"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1000000"""
        output = """266666333332"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()