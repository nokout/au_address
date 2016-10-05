# -*- coding: utf-8 -*-
from au_address import tokenFeatures
import unittest


class TestTokenFeatures(unittest.TestCase):

    def test_unicode(self):
        features = tokenFeatures(u'å')
        assert features['endsinpunc'] is False

if __name__ == '__main__':
    unittest.main()
