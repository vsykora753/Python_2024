from Kalkulacka import Calc
import pytest


@pytest.mark.parametrize(
    "par1, par2, vysledek", [
        (20, 40, 60),
        (100, 200, 300),
        (1000, 1, 1001)
    ]
)