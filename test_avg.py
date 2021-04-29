import unittest
import avg

class testCaseAvg(unittest.TestCase):
    def test_average(self):
    # Pass tests
        #simple list
        result = avg.avg([5, 6, 10, 60])
        self.assertEqual(result, 20.25)

        # negative list
        # result = avg.avg([-60, -19, -7, -6, -19, -70, -79])
        # self.assertEqual(result, -37.142857142857146)

    #Fail tests
        #letters in the list
        # result = avg.avg([s, q, w, l])
        # self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()