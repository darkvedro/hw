import pytest


@pytest.fixture(params=[3, 4, 5, 6])
def list_ofparams(request):
    return request.params
