class MethodsToTest:

    def __init__(self):
        pass

    def method1(self):
        return True

    def method2(self):
        return False

    def method3(self):
        return 'BLA'

    def method4(self): ### KeyError
        d = {'a':1,'b':2}
        d['c'] 

    def method5(self): ### TypeError
        set() + 1

import unittest

class TestMethods(unittest.TestCase):
    
    def setUp(self):
        self.test = MethodsToTest()

    def test_method1(self):
        self.assertTrue(self.test.method1())

    def test_method2(self):
        self.assertFalse(self.test.method2())

    def test_method3(self):
        self.assertNotEqual(self.test.method3(), 'BLA1')

    def test_method4(self):
        self.assertIn(self.test.method3(), 'BLA1')  

    def test_method5(self):
        if self.test.method3() == 'BLA':
            pass
        else:
            self.fail('Failed')

    def test_method_6(self):
        with self.assertRaises(KeyError):
            self.test.method4()

    def test_method_7(self):
        with self.assertRaises(TypeError):
            self.test_method5()

if __name__== '__main__':
    unittest.main()
