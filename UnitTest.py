from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {
            1: {'s': '101', 'output': 1},
            2: {'s': '100', 'output': 2},
            3: {'s': '0111', 'output': 0}
        }
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        s, output = self.__testCases[1].values()
        result = self.__obj.minimumSteps(s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        s, output = self.__testCases[2].values()
        result = self.__obj.minimumSteps(s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case3(self):
        s, output = self.__testCases[3].values()
        result = self.__obj.minimumSteps(s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()