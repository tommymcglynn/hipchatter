import unittest
from hipchatter import messenger, norris

class NorrisTest(unittest.TestCase):

    def test_joke(self):
        joke = norris.get_joke()
        self.assertTrue(joke is not None)
        self.assertTrue(len(joke) > 0)
