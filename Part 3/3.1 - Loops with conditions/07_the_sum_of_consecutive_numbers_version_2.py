# Write your solution here
limit = int(input("Limit:"))
total = 1
count = 1 
consecutive = "The consecutive sum: "

while limit > total:
    countstr = str(count)   
    count += 1 
    consecutive += countstr + " + "    
    total = total + count

finale = count 
print(f"{consecutive}{count} = {total}")
 
