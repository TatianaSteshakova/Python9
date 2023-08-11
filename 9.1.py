N = int(input("Введите n: "))

numbers = []

if N < 1 or N > 100000:
    print("False")
else:
    print("Введите числа: ")
    for i in range (0, N):
        n = int(input())
        if abs(n) < 2 * 10e9:
            numbers.append(n)
        else:
            print("False")
            break
    unique_numbers = set(numbers)

print("Количество различных чисел: ", len(unique_numbers))