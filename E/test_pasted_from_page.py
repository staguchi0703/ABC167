#
from resolve import resolve
####################################
####################################
# 以下にプラグインの内容をペーストする
#  
import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """3 2 1"""
        output = """6"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """100 100 0"""
        output = """73074801"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """60522 114575 7559"""
        output = """479519525"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()