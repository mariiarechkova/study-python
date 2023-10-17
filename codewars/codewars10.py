def likes (names):
    if len(names) == 0:
        return ("no one likes this")
    if len(names) == 1:
        print (str(names[0]) + " like this")
    if len(names) == 2:
        return (names[0], " and ", names[1], " like this")
    if len(names) == 3:
        return (names[0], names[1], " and ", names[2], " like this")
    if len(names) > 3:
        x = int(len(names) - 2)
        return (names[0], ',', names[1], " and ", str(x), " others like this")

likes(["Alex"])