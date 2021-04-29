import unittest
import volume

class testCaseVolume(unittest.TestCase):
    def test_vol(self):
    #pass tests
        # test post simple num
        result = volume.vol(3)
        self.assertEqual(result, 27)

        # test post complex num
        # result = volume.vol(9.65)
        # self.assertEqual(result, 898.6321250000001)

        #test neg numbers
        # result = volume.vol(-6)
        # self.assertEqual(result, -216)

    #fail test
        #type error test
        # result = volume.vol(s)
        # self.assertEqual(result, s)

if __name__ == "__main__":
    unittest.main()