    #print(len(rodne_cislo))
    #if not isinstance(rodne_cislo,int): 
        raise ValueError("Musíš zadat číslo")
    if rodne_cislo % 11 == 0 :
        print("Toto je opravdu číslo")
    else:
        print("Číslo není dělitelné  11 beze zbytku")
            
    return rodne_cislo