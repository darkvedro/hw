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

class TestDictionary:

    colors = {'белый': '000', 'красный': '111', 'синий': '222'}

    def test_d1(self):
        assert self.colors['белый'] == '000'

    def test_d2(self):
        assert len(self.colors.items()) == 3

    def test_d3(self):
        assert len(self.colors) == 3


    def test_d4(self, dict_params):
        assert dict_params in self.colors.values()


    @pytest.mark.parametrize('dict_params2', ['белый', 'синий', 'красный',])
    def test_dict_5(self, dict_params2):
        assert dict_params2 in self.colors.keys()

class TestString:

    ttext = """Launching pytest with arguments test_types"""

    def test_S1(self):
        assert self.ttext.startswith('Launching')

    def test_S2(self):
        assert 'pytest with arguments' in self.ttext

    def test_S3(self):
        assert len(self.ttext) <= 100

    def test_S4(self, string_params):
        assert string_params in self.ttext

    @pytest.mark.parametrize('part_ttext', ['arguments', 'with'])
    def test_S5(self, part_ttext):
        assert part_ttext in self.ttext
        
class TestSet:

    set1 = {'один', 'два', 'три', 1, 2, 3}
    set2 = {'один', 'два', 'три', 'четыре', 'пять', 1, 2, 3, 4, 5}

    def test_S1(self):
        assert self.set1 <= self.set2

    def test_S2(self):
        assert 'один' in self.set1

    def test_S3(self):
        assert len(self.set1) == 6

    def test_S4(self, set_params):
        assert set_params in self.set1

    @pytest.mark.parametrize('set_params4', ['один', 'два', 'три', 1, 2, 3])
    def test_S5(self, set_params4):
        assert set_params4 in self.set1
