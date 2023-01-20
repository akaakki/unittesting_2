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

test = MethodsToTest()

import pytest 

def test_method1():
    assert test.method1() == True

def test_method2():
    assert not test.method2()

def test_method3():
    assert test.method3() != 'BLA!'

def test_method4():
    assert test.method3() in 'BLA1'

def test_method5():
    #if test.method3() == 'BLA':
        #assert True
    #else:
        #assert False
    assert test.method3() == 'BLA'

def test_method6():
    with pytest.raises(KeyError):
        test.method4()

def test_method7():
    with pytest.raises(TypeError):
        test.method5()