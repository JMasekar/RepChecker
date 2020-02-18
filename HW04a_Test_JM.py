"""
@author- Jigar Masekar

HW04a Testing

"""

import unittest

from HW04a_JM import rep_checker


class TestRep(unittest.TestCase):

    def test_rep(self):
        repos = rep_checker('JMasekar')
        expect = [['helloworld', 1], ['RepChecker', 6], ['stevens_ssw810', 4], ['Triangle567', 8], ['Triangles', 2]]
        self.assertEqual(repos, expect)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
