import unittest
import person

class testCasePerson(unittest.TestCase):
    def test_per(self):
        
        result = person.getInfo()

    # passing test
        #capital letters
        # self.assertEqual("Sarah", result.first)
        # self.assertEqual("Jane", result.last)

        # capital and lower case
        # self.assertEqual("jeSS", result.first)
        # self.assertEqual("ranDalF", result.last)
    
    # fail test
        #  type errors 
        bIsLetter = True

        if not result.first.isalpha() or not result.last.isalpha():
            bIsDigit = False
        self.assertNotEqual(bIsDigit, False)

if __name__ == "__main__":
    unittest.main()