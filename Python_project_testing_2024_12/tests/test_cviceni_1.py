#napiste funkci, ktera vstupni parametr s textem vrati v opačném pořadí

import pytest
from cviceni_1 import zmena_poradi


@pytest.mark.parametrize(
    "text_1,text_2, vystup", [
        ("Karel", "Marek", "MarekKarel"),
        (0 , 3, 30)
    ]
)
def test_zmena_poradi(text_1, text_2,vystup):
    assert zmena_poradi(input_1 = text_1, input_2 = text_2) == vystup

