import math
from imghdr import tests

import pytest


class TestBasic:

    @pytest.mark.mytest
    def test_sqrt(self):
        num = 25
        assert math.sqrt(num) == 5

    @pytest.mark.mytest
    def testsquare(self):
        num = 7
        assert 7 * 7 == 40

    def tesequality(self):
        assert 10 == 11

# to run tests
# pytest -v
# pytest