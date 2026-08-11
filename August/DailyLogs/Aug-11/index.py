# Lists
marks=[90, 80, 70, 60, 50]
print("Marks:", marks)

# Indexing & Slicing
print("First mark:", marks[0])
print("Last mark:", marks[-1])
print("First three marks:", marks[:3])

# List Methods
# Perfroming Any Methods on the list will modify the original list
# Whereas performing any methods on the string will not modify the original string

marks.append(40)    #Adding an element to the end of the list
marks.sort()        #Sorting the list in ascending order[40, 50, 60, 70, 80, 90]
marks.reverse()     #Reversing the list[90, 80, 70, 60, 50, 40]
marks.insert(2, 75) #Inserting an element at a specific index(index, value)



# Lists Are Mutable
# Strings Are Immutable