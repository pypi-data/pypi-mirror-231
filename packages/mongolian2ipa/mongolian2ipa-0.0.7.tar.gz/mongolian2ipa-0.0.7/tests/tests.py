import unittest
from mongolian2ipa import mongolian2ipa
from mongolian2ipa.helpers import check_male_female_word, WordGender, check_first_level_vowel


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

    def test_male(self):
        result = check_male_female_word('машин')
        self.assertEqual(result, WordGender.MALE)

    def test_female(self):
        result = check_male_female_word('ээж')
        self.assertEqual(result, WordGender.FEMALE)

    def test_first_vowel(self):
        result = check_first_level_vowel('намар', 1)
        self.assertEqual(result, True)

    def test_not_first_vowel(self):
        result = check_first_level_vowel('намар', 3)
        self.assertEqual(result, False)

    def test_amsar(self):
        result = mongolian2ipa('амсар')
        self.assertEqual(result, 'amsər')

    def test_aimag(self):
        result = mongolian2ipa('айраг')
        self.assertEqual(result, 'æːrək')

    def test_darlagdsan(self):
        result = mongolian2ipa('дарлагсад')
        self.assertEqual(result, 'tarɬəksət')

    def test_ijil(self):
        result = mongolian2ipa('ижил')
        self.assertEqual(result, 'iʧəɬ')

    def test_ishig(self):
        result = mongolian2ipa('ишиг')
        self.assertEqual(result, 'iʃək')

    def test_ulger(self):
        result = mongolian2ipa('үлгэр')
        self.assertEqual(result, 'uɬkər')

    def test_niigem(self):
        result = mongolian2ipa('нийлмэл')
        self.assertEqual(result, 'niːɬməɬ')

    def test_omog(self):
        result = mongolian2ipa('омог')
        self.assertEqual(result, 'ɔmək')

    def test_oodon(self):
        result = mongolian2ipa('оодон')
        self.assertEqual(result, 'ɔːtəŋ')

    def test_orlog(self):
        result = mongolian2ipa('өрлөг')
        self.assertEqual(result, 'өrɬək')

    def test_horog(self):
        result = mongolian2ipa('хөрөг')
        self.assertEqual(result, 'xөrək')

    def test_gueg(self):
        result = mongolian2ipa('гүег')
        self.assertEqual(result, 'kujək')

    def test_jayg(self):
        result = mongolian2ipa('жаяг')
        self.assertEqual(result, 'ʧajək')

    def test_hayg(self):
        result = mongolian2ipa('хаяг')
        self.assertEqual(result, 'χajək')

    def test_soel(self):
        result = mongolian2ipa('соёл')
        self.assertEqual(result, 'sɔjəl')

    def test_aagim(self):
        result = mongolian2ipa('аагим')
        self.assertEqual(result, 'æːqəm')

    def test_aavgui(self):
        result = mongolian2ipa('аавгүй')
        self.assertEqual(result, 'aːwkui')

    def test_aagarhah(self):
        result = mongolian2ipa('аагархах')
        self.assertEqual(result, 'aːqərχəχ')

    def test_aadaih(self):
        result = mongolian2ipa('аадайх')
        self.assertEqual(result, 'aːtæːχ')

    def test_aajim(self):
        result = mongolian2ipa('аажим')
        self.assertEqual(result, 'æːʧəm')

    def test_aandaa(self):
        result = mongolian2ipa('аандаа')
        self.assertEqual(result, 'aːntaː')

    def test_aarnig(self):
        result = mongolian2ipa('аарниг')
        self.assertEqual(result, 'aːrnək')


if __name__ == '__main__':
    unittest.main()
