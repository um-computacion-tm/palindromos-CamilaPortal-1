import unittest
from palindrome import palindromeRecursivo
from palindrome import palindromeIterativo

class TestPalindromeRecursivo(unittest.TestCase):
    def test1(self):
        result=palindromeRecursivo("ala")
        self.assertEqual(result, True)

    def test2(self):
        result=palindromeRecursivo("hola")
        self.assertEqual(result, False)

    def test3(self):
        result=palindromeRecursivo("neuquen")
        self.assertEqual(result, True)
    
    def test4(self):
        result=palindromeRecursivo("ojo")
        self.assertEqual(result, True)

    def test5(self):
        result=palindromeRecursivo("perro")
        self.assertEqual(result, False)

class TestPalindromeIterativo(unittest.TestCase):
    
    def test_1(self):
        result=palindromeIterativo("ala")
        self.assertEqual(result, True)

    def test_2(self):
        result=palindromeIterativo("hola")
        self.assertEqual(result, False)

    def test_3(self):
        result=palindromeIterativo("neuquen")
        self.assertEqual(result, True)
    
    def test_4(self):
        result=palindromeIterativo("ojo")
        self.assertEqual(result, True)

    def test_5(self):
        result=palindromeIterativo("perro")
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()