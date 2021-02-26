card_key = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
card_dict = dict.fromkeys(card_key)
i = 2
for key in card_key:
    card_dict[key] = i
    i += 1
    
my_sum = 0
for _ in range(6):
    input_key = input()
    my_sum += int(card_dict[input_key])

print(my_sum / 6)
