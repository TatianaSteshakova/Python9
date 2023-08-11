sequence = map(int, input("Введите числа через пробел: ").split())

unique = set()

for n in sequence:
    if n in unique:
        print("YES")
    else:
        print("NO")
        unique.add(n)