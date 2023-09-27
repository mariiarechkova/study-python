def array_diff(a, b):
    return ([el for el in a if el not in b])

array_diff([1,2,2], [1])