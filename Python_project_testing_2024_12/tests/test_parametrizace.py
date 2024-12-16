import pytest
from parametrizace import my_function


@pytest.mark.parametrize(
    "par1, par2, vysledek", [
        (20, 40, 60),
        (100, 200, 300),
        (1000, 1, 1001)
    ]
)
def test_my_function(par1, par2, vysledek):
    assert my_function(param1=par1, param2=par2) == vysledek