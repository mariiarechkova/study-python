def count_bits(n):
    num = format(n, 'b')
    bit_num = list(map(int, str(num)))
    print(bit_num.count(1))

count_bits(25)