# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

test_values = test_dict.values()
min_value = min(test_values)
max_value = max(test_values)
for i in test_dict.items():
    if i[1] == min_value:
        min_key = i[0]
    if i[1] == max_value:
        max_key = i[0]
print("min:", min_key)
print("max:", max_key)
