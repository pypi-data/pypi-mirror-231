import unittest
from mongolian_to_ipa import mongolian2ipa


class MongoliaIPATest(unittest.TestCase):
    def test_a(self):
        result = mongolian2ipa('a')
        self.assertEqual(result, 'a')

    def test_aa(self):
        result = mongolian2ipa('аа')
        self.assertEqual(result, 'aː')

    def test_ai(self):
        result = mongolian2ipa('ай')
        self.assertEqual(result, 'æː')

    def test_a_with_i_ii(self):
        result = mongolian2ipa('ань')
        self.assertEqual(result[0], 'æ')


if __name__ == '__main__':
    unittest.main()
