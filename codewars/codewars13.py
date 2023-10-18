def camel_case(s):
    words = s.split()
    camel_case = [word.capitalize() for word in words]
    print(''.join(camel_case))

camel_case("test case")