# Write your solution here

items = int(input("How many items: "))
count = 1
list = []
while count <= items:
    item = int(input(f"Item {count}: "))
    list.append(item)
    count+=1 
else:
    print(list)
    
