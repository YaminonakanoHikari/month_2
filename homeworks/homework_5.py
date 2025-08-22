from homeworks.distance import Distance

d1 = Distance(500, 'cm')    # 5 м
d2 = Distance(2, 'm')       # 2 м
d3 = Distance(1, 'km')      # 1000 м

print(d1)                   # 500 cm
print(d2)                   # 2 m
print(d3)                   # 1 km

# Сложение
print(d1 + d2)              # 500 cm + 2 m -> 700 cm
print(d2 + d3)              # 2 m + 1 km -> 1002 m

# Вычитание
print(d3 - d2)              # 1 km - 2 m -> 998 m

# Сравнения
print(d1 < d2)              # False
print(d1 == Distance(5, 'm'))  # True
print(d3 > d2)              # True
