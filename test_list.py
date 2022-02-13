import pytest

class TestList:

    number = [1, 2, 3, 4]

    def test_L1(self):
        assert self.number[0] < self.number[1]

    def test_L2(self):
        assert self.number[1] == self.number[0] + 1

    def test_L3(self):
        assert len(self.number) == 4

    def test_L4(self):
        assert (self.number[0] + self.number[2]) >= self.number[3]

    @pytest.mark.parametrize('number_parameters', [3, 4, 5, 6])
    def test_L5(self, number_parameters):
        assert number_parameters >= self.number[0]
