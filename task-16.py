mas = list(map(int, input().split()))
if len(mas) <= 100000:
    unique_numbers = list(set(mas))
    print(len(unique_numbers))
else:
    print("Количество вводимых символов не должно превышать 100 000")


