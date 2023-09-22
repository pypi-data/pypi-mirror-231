from unittest import TestCase

from algortest.core import Core


class TestCore(TestCase):
    def test_core(self):
        assert Core().return_me(2) == 2