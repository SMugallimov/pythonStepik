
number1 = int(input())
number2 = int(input())
result1 = (number1 + number2) * (number1 + number2)
result2 = number1 * number1 + number2 * number2
print("Квадрат суммы", number1, "и", number2, "равен", result1)
print("Сумма квадратов", number1, "и", number2, "равна", result2)

number1 = int(input())
number2 = int(input())
number3 = int(input())
number4 = int(input())
result = number1 ** number2 + number3 ** number4
print(result)

number = int(input())
print(number * 1 + number * 11 + number * 111, sep='')