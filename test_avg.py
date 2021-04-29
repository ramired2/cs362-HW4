import unittest
import avg

class testCaseAvg(unittest.TestCase):
    def test_average(self):
    # Pass tests
        #simple list
        result = avg.avg([5, 6, 10, 60])
        self.assertEqual(result, 20.25)

        # result = avg.avg([99])
        # self.assertEqual(result, 99)

        # negative list
        # result = avg.avg([-60, -19, -7, -6, -19, -70, -79])
        # self.assertEqual(result, -37.142857142857146)

        # negative and positive list
        # result = avg.avg([99, -60, -1, -19, 5, 7, -5])
        # self.assertEqual(result, 3.7142857142857144)

    #Fail tests
        #empty list
        # result = avg.avg([])
        # self.assertEqual(result, 0)

        #letters in the list
        # result = avg.avg([s, q, w, l])
        # self.assertEqual(result, 0)

        # letters and numbers
        # result = avg.avg([-9, q, 20, w, 70, l, -70])
        # self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()