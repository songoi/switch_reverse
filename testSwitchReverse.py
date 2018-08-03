import unittest
from switchReverse import switchReverse

class test_switchReverse(unittest.TestCase):
    def test_switchReverse(self):
        self.assertEqual(switchReverse([2,3,4]), [4,3,2])
        self.assertEqual(switchReverse(["a","b","c"]), ["A","B","C"])
        self.assertEqual(switchReverse([2,"a",4]), [2,"a",4])

if __name__ == '__main__':
    unittest.main()