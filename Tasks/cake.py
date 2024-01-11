recipe = {"flour": 500, "sugar": 200, "eggs": 1}
ingredients = {"flour": 1200, "sugar": 1200, "eggs": 3}


def cakes(recipe, ingredients):
    count = []
    for i in recipe:
        if i not in ingredients:
            return 0
        else:
            count.append(ingredients[i] / recipe[i])
    return min(count)


print(cakes(recipe, ingredients))
