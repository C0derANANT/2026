# Tuples
t1=(1 , 2 , 3 , 4 , 5, 6 , 7 , 8 , 9 , 10) 
print(t1)

# Tuples Are Immutable Just Like Strings

# Indexing & Slicing
print("First element:", t1[0])
print("Last element:", t1[-1])
print("First three elements:", t1[:3])
print("Second To Second Last elements:", t1[1:-1])

for i in t1:
    if i == 5:
        print("Found 5!")
    else:
        print(i)