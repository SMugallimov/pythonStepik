
password = input()
confirmPassword = input()
if password == confirmPassword:
    print("Пароль принят")
else:
    print("Пароль не принят")

number = int(input())
if number % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

number = int(input())
digit1 = number % 10
digit2 = (number % 100) // 10
digit3 = (number % 1000) // 100
digit4 = number // 1000
if (digit1 + digit4) == (digit3 - digit2):
    print("ДА")
else:
    print("НЕТ")

age = int(input())
if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

number1 = int(input())
number2 = int(input())
number3 = int(input())
if (number2 - number1) + number2 == number3:
    print("YES")
else:
    print("NO")

number1 = int(input())
number2 = int(input())
if number1 < number2:
    print(number1)
else:
    print(number2)

number1 = int(input())
number2 = int(input())
number3 = int(input())
number4 = int(input())
if number1 < number2:
    number2 = number1
if number2 < number3:
    number3 = number2
if number3 < number4:
     print(number3)
else:
    print(number4)

age = int(input())
if age <= 13:
    print("детство")
if 14 < age < 24:
        print("молодость")
if 25 <= age < 59:
    print("зрелость")
if age >= 60:
    print("старость")

number1 = int(input())
number2 = int(input())
number3 = int(input())
result1 = int()
result2 = int()
result3 = int()
if number1 >= 0:
    result1 = number1
if number2 >= 0:
    result2 = number2
if number3 >= 0:
    result3 = number3
print(result1 + result2 + result3)
