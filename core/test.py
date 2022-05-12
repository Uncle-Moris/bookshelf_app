from categories import Categories

a = Categories.list_of_all_similar_categories()

for i in a:
    print(i[1])