
number = int(input())
print(number)
print(number + 1)
print(number + 2)

number1 = int(input())
number2 = int(input())
number3 = int(input())
print(number1 + number2 + number3)

number = int(input())
volume = number * number * number
square = 6 * (number * number)
print("Объем =", volume)
print("Площадь полной поверхности =", square)

number1 = int(input())
number2 = int(input())

result = 3 * ((number1 + number2) * (number1 + number2) * (number1 + number2)) + 275 * (number2 * number2) - 127 * number1 - 41
print(result)

number = int(input())
print("Следующее за числом", number, "число:", number + 1)
print("Для числа", number, "предыдущее число:", number - 1)

monitor = int(input())
processor = int(input())
keyboard = int(input())
mouse = (int(input()))
result = 3 * monitor + 3 * processor + 3 * keyboard + 3 * mouse
print(result)

number1 = int(input())
number2 = int(input())
print(number1, "+", number2, "=", number1 + number2)
print(number1, "-", number2, "=", number1 - number2)
print(number1, "*", number2, "=", number1 * number2)

a = int(input())
d = int(input())
n = int(input())
result = a + d * (n - 1)
print(result)

number = int(input())
print(number, number * 2, number * 3, number * 4, number * 5, sep='---')

number1 = int(input())
number2 = int(input())
number3 = int(input())
result = number1 * number2 ** (number3 - 1)
print(result)

number = int(input())
print(number // 100)

pupil = int(input())
mandarin = int(input())
print(mandarin // pupil)
print(mandarin % pupil)
population = int(input())
oddCheck = population % 2
print(population // 2 + oddCheck)

number = int(input())
print((number + 3) // 4)

number = int(input())
hours = number // 60
minutes = int(number % 60)
print(number, "мин - это", hours, "час", minutes, "минут.")

number = int(input())
fisrt = number % 10
second = (number % 100) // 10
third = number // 100
print("Сумма цифр =", fisrt + second + third)
print("Произведение цифр =", fisrt * second * third)

number = int(input())
first = number % 10
second = (number % 100) // 10
third = number // 100
print(third, second, first, sep='')
print(third, first, second, sep='')
print(second, third, first, sep='')
print(second, first, third, sep='')
print(first, third, second, sep='')
print(first, second, third, sep='')

number = int(input())
fourth = number % 10
third = (number % 100) // 10
second = (number % 1000) // 100
first = number // 1000
print("Цифра в позиции тысяч равна", first)
print("Цифра в позиции сотен равна", second)
print("Цифра в позиции десятков равна", third)
print("Цифра в позиции единиц равна", fourth)