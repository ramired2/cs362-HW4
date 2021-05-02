import unittest
import person

class testCasePerson(unittest.TestCase):
    def test_per(self):
        
        result = person.getInfo()

    # passing test
        #capital letters
        # when input "Sarah" and "Jane"
        self.assertEqual("Sarah", result.first)
        self.assertEqual("Jane", result.last)
    
    # fail test
        # ramdonly capitalized letters
        # if input "jeSS" expects "Jess"
        self.assertEqual("Jess", result.first)
        self.assertEqual("Randalf", result.last)

        #  type errors 
        bIsLetter = True

        if not result.first.isalpha() or not result.last.isalpha():
            bIsDigit = False
        self.assertNotEqual(bIsDigit, False)

if __name__ == "__main__":
    unittest.main()