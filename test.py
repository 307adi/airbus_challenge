
import unittest
#from cal.py import ops
ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y), "*": (lambda x,y: x*y), "/": (lambda x,y: x/y)}

class Test(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(ops["+"](1,3), 4, "Should be 4")

    def test_sub(self):
        self.assertEqual(ops["-"](5,3), 2, "Should be 2")

    def test_mul(self):
        self.assertEqual(ops["*"](1,3), 3, "Should be 3")

    def test_div(self):
        self.assertEqual(ops["/"](6,3), 2, "Should be 2")

if __name__ == '__main__':
    unittest.main()
    
