#Сумма трёх чисел

a = int(input())
b = int(input())
c = int(input())
print(a + b + c)


#Площадь прямоугольного треугольника

b = int(input())
h = int(input())
s = ((b * h) * 0.5)
print(s)

#Дележ яблок

n = int(input())
k = int(input())
print(k // n)
print(k % n)


#Электронные часы

n = int(input())
a = n % (60 * 24) // 60
b = n % 60
print(a, b)


#Hello, Harry!

name = input()
print('Hello, ' + name + '!')

#Следующее и предыдущее

d = 1
n = int(input())
next = n + d
previous = n - d
j = str(next)
g = str(previous)
h = str(n)
print('The next number for the number' ' ' + h + ' ' 'is' ' ' + j + '.')
print('The previous number for the number' ' ' + h + ' ' 'is' ' ' + g + '.')


#Парты

x1 = int(input())
x2 = int(input())
x3 = int(input())
y = ((x1 // 2)+ (x2 // 2) + (x3 // 2)) + ((x1 % 2) + (x2 % 2) + (x3 % 2))
print(y)


#Шнурки

a = int(input())
b = int(input())
l = int(input())
n = int(input())
y = (a * (n * 2 - 1)) + (l * 2) + (b * (n * 2 - 2))
print(y)
