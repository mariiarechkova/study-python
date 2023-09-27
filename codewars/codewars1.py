def gimme_the_letters(sp):
    new_letters = []
    for n in range(ord(sp[0]), ord(sp[-1]) + 1):
        new_letters.append(chr(n))
    print("".join(new_letters))

# gimme_the_letters("n-p")
gimme_the_letters("H-I")