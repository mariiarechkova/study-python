def in_array(array1, array2):
    array3 = []
    for item in array2:
        for i in array1:
            res = item.find(i)
            if res >= 0:
                array3.append(i)
    # qwe = [el for el in array1 if el in array3]
    new_array = [el for el in array1 if el in array3]
    print(new_array)



in_array(['oes', 'oint', 'ect', 'wh', 'ou', 'wh', 'ing', 'he', 'by', 'ect'],
         ['by', 'ect', 'he', 'ing', 'oes', 'oint', 'ou', 'wh'])
