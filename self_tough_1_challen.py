#1 print three strings
print('Ha')
print('Ho')
print('Hi')

#2 prints message if x <10 and if x >= 10

x = 0

if x < 10:
    print('x are less than 10')
else:
    print('x is more or equal to 10')

#3
x = 20

if x <= 10:
    print('x is less or equal to 10')
elif 10 < x <= 25:
    print('x is more than ten or equal 25')
else:
    print('x is more than 25')

#4 divides to variables and print remainder

print(5 % 2)

#5 two variables, divides, print quatient

print(8 // 3)

#6
age = 10

if age < 12:
    print('child')
elif age < 18:
    print('adolescent')
elif age > 18 and age < 65:
    print('grown up')
else:
    print('old')
