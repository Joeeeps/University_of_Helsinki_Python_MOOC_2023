# Write your solution here
number = int(input("Please type in a number:"))

if number > 0:
    for i in range(2, number + 1, 2): #start point, interval
        print(i) #gets the even
        if i - 1 <= number:  
            print(i - 1) #gets the odd, if it exists
    if number % 2 != 0:  
        print(number) #if final number is odd, it won't be in the even range (i.e. 5 won't be in 2,4,6) so manually print the number

#model solution
#number = int(input("Please type in a number: "))
#index = 1
#while index+1 <= number:
#    print(index+1)
#    print(index)
#    index += 2
#if index <= number:
#    print(index)

 


