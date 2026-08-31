# String Slicing
s="Anant"
print(s[:3]) # Ana
print(s[-1:-4:-1]) # tna

print(s[::2]) # Ant
print(s[-1:-4:-1])


# String Methods
s="Anant Annie Betty Anant Ash Anant"
s.endswith("t") # True
print(s.endswith("t"))
print(s.find("Anant"))
print(s.count("Anant"))