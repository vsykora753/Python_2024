"""
napiste funkci validujici rodne cislo, funkce bere jako parameter string s rodnym cislem, a vrati True nebo False v zavislosti na vysledku validace.
k funkci pridejte positivni a negativni Pytest test cases.
Zkuste pouzit programovani s cyklem. Zkuste parametrizovani testu. Zkuste testovani vyjimek.

odkaz na paragraf 2 zakona stanovujici validni rodne cislo: https://www.slov-lex.sk/pravne-predpisy/SK/ZZ/1995/301/
"""


def validate_rodne_cislo(rod_cislo:str):

    znak_delete = "/"
    rodne_cislo_list =[]
    for znak in rod_cislo:
        if znak !=  znak_delete:
           rodne_cislo_list.append(znak) 
    rodne_cislo = ''.join(rodne_cislo_list)

    if int(rodne_cislo) % 11 == 0:
        return rodne_cislo
    else:
        return f"rodné číslo {rodne_cislo} neodpovídá platnému číslu"
        


    

    # rodne_cislo = int(rod_cislo.replace("/",""))
    # print(rodne_cislo)
    # if not isinstance(rodne_cislo,int):
    #     raise ValueError("Musíš zadat číslo")
    
    
    # print(rodne_cislo)
    # print(len(str(rodne_cislo)))



    # #print(len(rodne_cislo))
    # #if not isinstance(rodne_cislo,int): 
    #     raise ValueError("Musíš zadat číslo")
    # if rodne_cislo % 11 == 0 :
    #     print("Toto je opravdu číslo")
    # else:
    #     print("Číslo není dělitelné  11 beze zbytku")
            
    # return rodne_cislo
     
if __name__ == '__main__':
   
    
    print(validate_rodne_cislo("7507240345"))
     
    #print(validate_rodne_cislo(75345))
