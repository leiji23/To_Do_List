distance_sum = 0
for walk in walks:
    distance_sum += walk.get('distance')
print(int(distance_sum / len(walks)))
