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
        input = """3 3 10
60 2 2 4
70 8 7 9
50 2 3 9"""
        output = """120"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 3 10
100 3 1 4
100 1 5 9
100 2 6 5"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """8 5 22
100 3 7 5 3 1
164 4 5 2 7 8
334 7 2 7 2 9
234 4 7 2 8 2
541 5 4 3 3 6
235 4 8 6 9 7
394 3 6 1 6 2
872 8 4 3 7 2"""
        output = """1067"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()