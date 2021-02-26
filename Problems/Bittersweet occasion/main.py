# finish the function
def find_the_parent(child):
    for food_class in [Drinks, Pastry, Sweets]:
        if issubclass(child, food_class):
            print(food_class.__name__)
