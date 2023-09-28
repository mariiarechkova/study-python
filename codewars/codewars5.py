def filter_list(l):
    nums = []
    for el in l:
        if type(el) is int:
            nums.append(el)
    print(nums)

filter_list([1,2,'a','b'])