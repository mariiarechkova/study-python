def cakes(recipe, available):
    try:
        result = {x:available[x]//recipe[x] for x in recipe}
        print(min(result.values()))
    except:
        print(0)



cakes({'flour': 500, 'sugar': 200, 'eggs': 3}, {'flour': 1200, 'sugar': 1200, 'eggs': 2, 'milk': 200})