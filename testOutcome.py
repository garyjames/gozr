import unittest
from outcome import Outcome

class TestOutcome(unittest.TestCase):
    def setUp(self):
        self.oc0 = Outcome("00", 35)
        self.oc1 = Outcome("0", 35)
        self.oc2 = Outcome("1", 35)
        self.oc3 = Outcome("Split 1-2", 17)
        self.oc4 = Outcome("Split 1-4", 17)
    def testName(self):
        self.assertEqual("00", self.oc0.name)
        self.assertRaises(AttributeError, self.assertEqual, "00", self.oc0)
        self.assertEqual("Split 1-2", self.oc3.name)
        self.assertEqual(self.oc1, self.oc1)
        self.assertNotEqual(self.oc3, self.oc4)

if __name__ == "__main__":
    unittest.main()
