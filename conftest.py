import pytest


@pytest.fixture(params=[3, 4, 5, 6])
def list_params(request):
    return request.params

@pytest.fixture(params=['000', '111', '222'])
def dict_params(request):
    return request.param


@pytest.fixture(params=['arguments', 'with'])
def string_params(request):
    return request.param
