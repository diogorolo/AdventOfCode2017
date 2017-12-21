from unittest import TestCase
from src.passphrase import PassPhrase


class TestPassPhrase(TestCase):
    def test_is_valid_all_different(self):
        p = PassPhrase('aa bb cc dd ee')
        result = p.is_valid()
        self.assertTrue(result)

    def test_is_valid_repeated_phrase(self):
        p = PassPhrase('aa bb cc dd aa')
        result = p.is_valid()
        self.assertFalse(result)

    def test_is_valid_similar_phrase_but_valid(self):
        p = PassPhrase('aa bb cc dd aaa')
        result = p.is_valid()
        self.assertTrue(result)

    def test_is_valid_repeated_with_newline(self):
        p = PassPhrase('aa aa\n')
        result = p.is_valid()
        self.assertFalse(result)
