# Write your solution here

limit = int(input("Limit:"))
total = 1
count = 1 

while limit > total:
    count += 1 
    total = total + count

finale = count 
print(f"{total}")

