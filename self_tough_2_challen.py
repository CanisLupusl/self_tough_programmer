#1
def square_num(x):
    '''
    (num) -> num

    Returns square of a x.

    >>>square_num(3)
    6
    '''
    return x ** 2

print(square_num(3))
#2
def string(x):
    '''
    (string) -> string

    Prints a string.

    >>>string('labas')
    labas
    '''
    print(x)

string('labas vakaras')
#3
def parametr(x, y, z, v=0, t=0):
    '''
    Takes 3 rquired and 2 optional parameters.
    '''
    return x + y +z + v + t

result = parametr(14, 18, 20)
print(result)

#4
def divide2(x):
    '''
    (int) -> int

    Returns x divided by 2.

    >>>divide2(6)
    3
    '''
    return x / 2

def mult4(x):
    '''
    (int) -> int

    Returns x multiplied by 4.

    >>>mult4(5)
    20
    '''
    return x * 4

a = divide2(2)
b = mult4(a)

print(b)
#5
def constrin(x):
    '''
    (str) -> float

    Takes string and converts it to a float.

    >>>constrin('2')
    2.0
    '''
    try:
        return float(x)
    except ValueError:
        print('Enter a string')
  
c = constrin('55.0')
print(c)
