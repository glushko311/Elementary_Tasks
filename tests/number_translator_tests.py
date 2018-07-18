import unittest

from number_translator import NumberTranslator


class NumberTranslatorTestSuit(unittest.TestCase):

    def test_translate_thousands1(self):
        actual_res = NumberTranslator().translate(12000)
        expected_res = "двенадцать тысяч"
        self.assertEqual(actual_res, expected_res)

    def test_translate_thousands2(self):
        actual_res = NumberTranslator().translate(222000)
        expected_res = "двести двадцать две тысячи"
        self.assertEqual(actual_res, expected_res)

    def test_translate_null(self):
        actual_res = NumberTranslator().translate(0)
        expected_res = "ноль"
        self.assertEqual(actual_res, expected_res)

    def test_translate_millions1(self):
        actual_res = NumberTranslator().translate(12000000)
        expected_res = "двенадцать миллионов"
        self.assertEqual(actual_res, expected_res)

    def test_translate_millions2(self):
        actual_res = NumberTranslator().translate(204000000)
        expected_res = "двести четыре миллиона"
        self.assertEqual(actual_res, expected_res)

    def test_translate_large(self):
        actual_res = NumberTranslator().translate(7897829347)
        expected_res = "семь миллиардов восемьсот девяносто семь " \
                       "миллионов восемьсот двадцать девять тысяч триста сорок семь"
        self.assertEqual(actual_res, expected_res)

    def test_translate_negative(self):
        actual_res = NumberTranslator().translate(-12356356)
        expected_res = "минус двенадцать миллионов триста пятьдесят шесть" \
                       " тысяч триста пятьдесят шесть"
        self.assertEqual(actual_res, expected_res)

    def test_translate_teen1(self):
        actual_res = NumberTranslator().translate(15)
        expected_res = "пятнадцать"
        self.assertEqual(actual_res, expected_res)

    def test_translate_teen2(self):
        actual_res = NumberTranslator().translate(19)
        expected_res = "девятнадцать"
        self.assertEqual(actual_res, expected_res)

    def test_translate_teen3(self):
        actual_res = NumberTranslator().translate(11)
        expected_res = "одинадцать"
        self.assertEqual(actual_res, expected_res)

    def test_translate_teen4(self):
        actual_res = NumberTranslator().translate(111)
        expected_res = "сто одинадцать"
        self.assertEqual(actual_res, expected_res)

    def test_translate_one1(self):
        actual_res = NumberTranslator().translate(1)
        expected_res = "один"
        self.assertEqual(actual_res, expected_res)

    def test_translate_one2(self):
        actual_res = NumberTranslator().translate(9)
        expected_res = "девять"
        self.assertEqual(actual_res, expected_res)

    def test_translate_two(self):
        actual_res = NumberTranslator().translate(56)
        expected_res = "пятьдесят шесть"
        self.assertEqual(actual_res, expected_res)

    def test_translate_two2(self):
        actual_res = NumberTranslator().translate(20)
        expected_res = "двадцать"
        self.assertEqual(actual_res, expected_res)


if __name__ == '__main__':
    unittest.main()
