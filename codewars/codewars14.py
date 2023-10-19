def pig_it(text):
    words = []
    marks = ['!', ',', '.', '?', '/', ':', ';', '*']
    new_text = text.split()
    print(new_text)
    for item in new_text:
        if item in marks:
            words.append(item)
        else:
            word = item[1:] + item[0] + "ay"
            words.append(word)
    return (' '.join(words))


pig_it('Hello world !')