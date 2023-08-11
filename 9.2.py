print("Введите первый список (через пробел): ")
list1 = list(map(int, input().split()))

print("Введите второй список (через пробел): ")
list2 = list(map(int, input().split()))

if len(list1) < 100000 and len(list2) < 100000:
    common = len(set(list1) & set(list2))
    print("Кол-во одинаковых чисел: ", common)
else:
    print("False")