#Write solution in here

def distinct_numbers(my_list):
    my_list = list(set(my_list))
    my_list = sorted(my_list)
    return my_list 

#model solution
#def distinct_numbers(my_list: list):
#    results = []
#    for item in my_list:
#        if item not in results:
#            results.append(item)
#    results.sort()
#    return results

# Write your solution here
            
#zip function combines the lists, then can add them together
if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]