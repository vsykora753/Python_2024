
# def my_function(param1, param2):
#     if isinstance(param2, str):
#         return param1
#     else:
#         return param1 + param2

# napiste funkci validujici telefonni cislo, funkce bere jako parameter string s telefonnim cislem, a vrati True nebo False v zavislosti na vysledku validace.
# k funkci pridejte positivni a negativni Pytest test case.
# Zkuste pouzit programovani s cyklem.

#
# def check_phone_number(phone_number: str) -> bool:
#     if len(phone_number) != 9:
#         return False
#     return True


    # # Regulární výraz pro validní telefonní čísla
    # pattern = re.compile(r'^\+?\d{9,15}$')
    # return bool(pattern.match(phone_number))


# napiste funkci slouzici k vypoctu faktorialu (parameter funkce urcuje "velikost" faktorialu k vypoctu).
# pokrejte positivnim a negativnim test casem (edited)

def factorial(number) :
    if not isinstance(number,int):
        raise ValueError("Musíš zadat číslo")
    if number < 0 :
        raise ValueError("Musíš zadat kladné číslo")

    result = 1
    for number in range(1, number + 1):
        result *= number
    return result

if __name__ == '__main__':
    # print(my_function(param1=20, param2=40))
    # print(my_function(param1=20, param2="abcd"))
    #
    # print(check_phone_number(""))
    factorial("d")
