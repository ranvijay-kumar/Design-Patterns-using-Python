import unittest


class Sentence:
    def __init__(self, plain_text):
        self.words = plain_text.split(" ")
        self.caps = [False for _ in range(len(plain_text))]


class Evaluate(unittest.TestCase):
    def test_exercise(self):
        s = Sentence('alpha beta gamma')
        s[1].capitalize = True
        self.assertEqual(str(s), 'alpha BETA gamma')
