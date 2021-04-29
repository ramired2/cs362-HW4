import unittest
import person

class testCasePerson(unittest.TestCase):
    def test_per(self):
        
        result = person.getInfo()

    # passing test
        #capital letters test
        # self.assertEqual("Sarah", result.first)
        # self.assertEqual("Jane", result.last)

        # capital and lower case test
        # self.assertEqual("jeSS", result.first)
        # self.assertEqual("ranDalF", result.last)
    
    # fail test - type errors --> adding numbers
        bIsDigit = False

        if result.first.isdigit() or result.last.isdigit():
            bIsDigit = True
        self.assertNotEqual(bIsDigit, True)

if __name__ == "__main__":
    unittest.main()