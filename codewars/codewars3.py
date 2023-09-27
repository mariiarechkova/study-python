def square_digits(num):
    square_nums = []
    new_num = list(map(int, str(num)))
    for el in new_num:
        square_nums.append(str(el**2))
    print(int(''.join(square_nums)))

square_digits(3022652)