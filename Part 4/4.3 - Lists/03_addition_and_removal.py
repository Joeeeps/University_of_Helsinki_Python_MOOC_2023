# Write your solution here
list = []
count = 1 
print(f"The list is now {list}")

while True:
    adr = input("a(d)d, (r)emove or e(x)it: ")
    if adr == "d":
        list.append(count)
        print(f"The list is now {list}")
        count +=1 
    elif adr == "r":
        list.remove(count-1)
        print(f"The list is now {list}")
        count -= 1    
    elif adr == "x":
        print("Bye!")
        break
    
        

