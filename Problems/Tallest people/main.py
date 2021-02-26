def tallest_people(**persons):
    tallest_names = []
    tallest_height = max(persons.values())

    for name, height in persons.items():
        if height == tallest_height:
            tallest_names.append(name)

    for name in sorted(tallest_names):
        print(name + " : " + str(tallest_height))
