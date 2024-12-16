from main import factorial
import pytest

def test_factorial_positive():
    ocekavane_hodnoty = [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (10, 3628800)
    ]
    for vstup, ocekavany_vysledek in ocekavane_hodnoty:
        vysledek = factorial(vstup)
        assert vysledek == ocekavany_vysledek,f"Test selhal pro vstup {vstup}: \
        očekáváno {ocekavany_vysledek}, ale bylo {vysledek}"

    print("Pro testovaný seznam jsou výpočty správně!")

def test_factorial_negative():
    with pytest.raises(ValueError, match="Musíš zadat číslo"): factorial("abc")
    with pytest.raises(ValueError, match="Musíš zadat kladné číslo"): factorial(-10)

    print("Pro negativní test je výsledek správný !")