import unittest
import au_address

class TestTagging(unittest.TestCase) :

    def test_broadway(self) :
        s1 = '1775 Broadway And 57th, Newyork NY'
        au_address.tag(s1)
