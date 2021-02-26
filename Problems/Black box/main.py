# use the function blackbox(lst) that is already defined
my_list = [1, 2, 3]

my_new_list = blackbox(my_list)
if id(my_list) == id(my_new_list):
    print("modifies")
else:
    print("new")
