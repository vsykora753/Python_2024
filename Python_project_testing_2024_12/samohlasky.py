#napiste funkci, ktera secte samohlasky ve slove udanem vstupnim parametrem

def samohlasky_pocet(slovo:str):
    samohlasky="aeiouyáéíóúýů"
    pocet = 0
    for pismeno in slovo.lower():
        if pismeno in samohlasky:
            pocet = pocet + 1
    return pocet


if __name__ == '__main__':
    print(samohlasky_pocet("ahoj"))
