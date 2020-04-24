'''
    To run the test:
        python test_thisfile.py

    Note:
    The unittest module can be used from the command line to run
    tests from modules, classes or even individual test methods:
        python -m unittest test_module1 test_module2
        python -m unittest test_module.TestClass
        python -m unittest test_module.TestClass.test_method
    if __name__=='__main__': unittest.main()   --> is not required in this case.
'''


import unittest


class TestMyClass(unittest.TestCase):
    '''
        Name of all test cases methods must start with 'test_',
        if not then the test won't run.

        flow:
            setupClass

            setUp
            test_method1
            tearDown

            setUp
            test_method1
            tearDown

            .
            .

            tearDownClass
    '''

    @classmethod
    def setUpClass(cls):
        '''
            Class method. Method name must be 'setUpClass'.
            Called once, at the start of testing.
        '''
        pass

    @classmethod
    def tearDownClass(cls):
        '''
            Class method. Method name must be 'tearDownClass'.
            Called once, at the end of testing.
        '''
        pass

    def setUp(self):
        '''
            Method name must be 'setUp'. Called before each test cases,
            mostly initialize instance variable which are
            common for all test cases.
        '''
        pass
        # ex: self.instance = MyClass('var1', 'var2')

    def tearDown(self):
        '''
            Method name must be 'tearDown'. Called after each test cases,
            Used as destructor for instances created in setUp method.
        '''
        pass

    def test_method1(self):
        '''
            Name must start with 'test_'
        '''
        # Assert equal or not
        self.assertEqual('foo'.upper(), 'FOO')

        # Assert True/False
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

        # Check if proper exception is raised or not
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)


# Unit test can bb run using command line interface
# for that comment the below code and run by 'python -m unittest test_thisfile.py'
# Note: dont use ' python -m unittest ./test_thisfile.py'
# if __name__ == '__main__':
#     unittest.main()
