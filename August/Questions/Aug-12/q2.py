text = "Hello world hello Python"
l1=text.lower().split(' ')
dict={}
for items in l1:
    x=l1.count(items)
    dict[items]=x
print(dict)