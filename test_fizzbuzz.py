import unittest

def fizzbuzz(num):
    if num % 15 == 0:
        return 'fizzbuzz'
    elif num % 5 == 0:
        return 'fizz'
    elif num % 3 == 0:
        return 'buzz'
    else:
        return num

class PlusTest(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual('fizzbuzz', fizzbuzz(15))
        self.assertEqual('fizz', fizzbuzz(5))
        self.assertEqual('buzz', fizzbuzz(3))
        self.assertEqual(2, fizzbuzz(2))

if __name__ == "__main__":
    unittest.main()
