import unittest
from program import run_computer_file

class TestIntCodeComputer(unittest.TestCase):
    
 def testDay9Part1(self):
    out = run_computer_file('input', [1])
    self.assertEqual(out, [2870072642])

 def testDay9Part2(self):
    out = run_computer_file('input', [2])
    self.assertEqual(out, [58534])


if __name__ == '__main__':
    unittest.main()
