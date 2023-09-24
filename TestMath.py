import unittest
from Mathematics import Mathematics

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.mat = Mathematics()

    def test_add(self):
        result = self.mat.sum_to_numbers(10,5)
        self.assertEqual(result, 15)  # add assertion here

    def test_multiply(self):
        result = self.mat.multiply_to_numbers(10,5)
        self.assertEqual(result, 50)  # add assertion here

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()
