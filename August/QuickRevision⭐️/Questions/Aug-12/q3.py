set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}

result = (set1 & set2) | (set2 & set3) | (set1 & set3)

print(result)