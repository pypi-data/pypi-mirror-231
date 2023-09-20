from unittest import TestCase

from datatool.string import to_camelcase, to_snakecase, to_cebabcase


class StringTest(TestCase):
    def test_to_camelcase(self):
        self.assertEqual(to_camelcase("This is a string."), "ThisIsAString")
        self.assertEqual(to_camelcase("URL"), "URL")
        self.assertEqual(to_camelcase("word12word"), "Word12Word")

    def test_to_snakecase(self):
        self.assertEqual(to_snakecase("This is a string."), "this_is_a_string")
        self.assertEqual(to_snakecase("ThisIsAString"), "this_is_a_string")
        self.assertEqual(to_snakecase("this-is-a-string"), "this_is_a_string")

    def test_to_cebabcase(self):
        self.assertEqual(to_cebabcase("This is a string."), "this-is-a-string")
        self.assertEqual(to_cebabcase("ThisIsAString"), "this-is-a-string")
        self.assertEqual(to_cebabcase("this_is_a_string"), "this-is-a-string")
