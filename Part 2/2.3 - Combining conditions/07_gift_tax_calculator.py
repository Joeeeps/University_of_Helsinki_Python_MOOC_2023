# Write your solution here
gift = int(input("What is the value of your gift?"))

if gift < 5000:
    print("No tax!")
else:
    if gift >5000 and gift <25000:
        base = 100
        limit = 5000
        tax = 0.08
    elif gift >=25000 and gift <55000:
        base = 1700
        limit = 25000
        tax = 0.10
    elif gift >=55000 and gift <200000:
        base = 4700
        limit = 55000
        tax = 0.12
    elif gift >=200000 and gift <1000000:
        base = 22100
        limit = 200000
        tax = 0.15
    elif gift >= 1000000: 
        base = 142100
        limit = 1000000
        tax = 0.17
    
    print(f"Amount of tax: {base + (gift-limit)*tax} euros")  
