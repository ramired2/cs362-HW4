import unittest
import volume

class testCaseVolume(unittest.TestCase):
    def test_vol(self):
    #pass tests
        # simple num
        result = volume.vol(3)
        self.assertEqual(result, 27)

        # neg number
        result = volume.vol(-6)
        self.assertEqual(result, -216)

    #fail test
        #type error test
        result = volume.vol(s)
        
        self.assertEqual(result, s)

if __name__ == "__main__":
    unittest.main()