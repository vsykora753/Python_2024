import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from rodne_cislo import validate_rodne_cislo
import pytest


@pytest.mark.parametrize(
    "par1,  vysledek", [
        ("750724/0345",  "7507240345"),
        ("7507240346", "chyba")       
    ]
)
def test_validate_rodne_cislo(par1,vysledek):
    assert validate_rodne_cislo(par1) == vysledek
