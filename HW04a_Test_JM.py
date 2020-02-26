"""
@author- Jigar Masekar

HW04a Testing

"""

import unittest

from HW04a_JM import *
from unittest import mock


def mocker(url):
    if url == 'https://api.github.com/users/JMasekar/repos':
        return call('repos.json')
    elif url == "https://api.github.com/repos/JMasekar/helloworld/commits":
        return call('commitshelloworld.json')
    elif url == "https://api.github.com/repos/JMasekar/RepChecker/commits":
        return call('commitsRepChecker.json')
    elif url == "https://api.github.com/repos/JMasekar/stevens_ssw810/commits":
        return call('commitsstevens_ssw810.json')
    elif url == "https://api.github.com/repos/JMasekar/Triangle567/commits":
        return call('commitsTriangle567.json')
    elif url == "https://api.github.com/repos/JMasekar/Triangles/commits":
        return call('commitsTriangles.json')


def call(path):
    data = MyClass()
    with open(path, 'r') as f:
        data.text = json.load(f)
    return data


class MyClass:
    text = ""


class TestRep(unittest.TestCase):

    @mock.patch('requests.get')
    def test_rep(self, mocked_request):
        mocked_request.side_effect = mocker

        repos = rep_checker('JMasekar')
        expect = [['helloworld', 1], ['RepChecker', 9], ['stevens_ssw810', 4], ['Triangle567', 8], ['Triangles', 2]]
        self.assertEqual(repos, expect)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
