from unittest import TestCase

from datatool.singleton import Singleton, SingletonParameterized


class SingletonTest(TestCase):
    def test_singleton(self):
        class MyClass(metaclass=Singleton):
            pass

        a = MyClass.get_instance()
        b = MyClass.get_instance()
        self.assertTrue(a is b)

    def test_singleton_parameterized(self):
        class MyClass(metaclass=SingletonParameterized):
            def __init__(self, a):
                self._a = a

        a = MyClass.get_instance(1)
        b = MyClass.get_instance(2)
        c = MyClass.get_instance(2)

        self.assertTrue(a is not b)
        self.assertTrue(b is c)
        self.assertTrue(a is not c)
