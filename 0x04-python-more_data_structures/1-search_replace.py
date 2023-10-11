def search_replace(my_list, search, replace):
    return [replace if item == search else item for item in my_list]

my_list = [1, 2, 3, 2, 4, 5]
print(search_replace(my_list, 2, 8))
