a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
if a > b and a > c:
    print(a, b, c)
elif b > a and b > c:
    print(b, a, c)
elif c > a and c > b:
    print(c, a, b)
elif b > a and b < c:
    print(c, b, a)
elif c > a and c < b:
    print(b, c, a)
else:
    print(a, c, b)