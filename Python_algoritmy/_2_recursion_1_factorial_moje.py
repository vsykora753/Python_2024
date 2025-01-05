"""
5! = 5 * 4 * 3 * 2 * 1 
4! =     4 * 3 * 2 * 1
5! = 5 * 4!
n! = n * (n - 1)!

"""
"""
# faktorial  N
if n > 1:
    n * (n -1)!
if n == 1 :
    return 1
"""


def factorial(n: int) -> int:
    
    if not isinstance(n,int) :
        raise TypeError("Faktorial funguje pouze s celýma číslama")

    if n < 0 :
        raise ValueError("Faktorial není definován pro záporná čísla")

    if n in(1, 0):
       return 1  
    
    return n * factorial(n-1)

factorial(5)
factorial(0)
factorial(1)
factorial(2)
factorial(3)
factorial(4)

factorial(-5)
