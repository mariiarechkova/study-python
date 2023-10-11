def unique_in_order(sequence):
    list1 = (list(sequence))
    unic_values = []
    len(sequence) and unic_values.append(list1[0])
    for item in list1:
        if item != unic_values[-1]:
            unic_values.append(item)
    print(unic_values)
unique_in_order([])