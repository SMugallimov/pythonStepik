
number = int(input())
if -1 < number < 17:
    print("Принадлежит")
else:
    print("Не принадлежит")

number = int(input())
if number <= -3 or number >= 7:
    print("Принадлежит")
else:
    print("Не принадлежит")

number = int(input())
if -30 < number <= -2 or 7 < number <= 25:
    print("Принадлежит")
else:
    print("Не принадлежит")

number = int(input())
if (10000 > number >= 1000) and (number % 7 == 0 or number % 17 == 0):
    print("YES")
else:
    print("NO")

number1 = int(input())
number2 = int(input())
number3 = int(input())
if (number3 < number1 + number2) and (number2 < number1 + number3) and (number1 < number2 + number3):
    print("YES")
else:
    print("NO")

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")