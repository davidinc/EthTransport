import unittest


class BasicTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_basic(self):
        a = 1
        self.assertEqual(1, a)

    def test_basic_2(self):
        a = 1
        assert a == 1


if __name__ == '__main__':
    unittest.main()
