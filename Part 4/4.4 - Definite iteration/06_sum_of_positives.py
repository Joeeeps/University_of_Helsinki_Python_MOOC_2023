#Write solution in here
def sum_of_positives(nums):
    positive_sum = 0
    for num in nums: 
        if num > 0:
            positive_sum += num
    return positive_sum #make positive_sum only include positive numbers added together 

 
 
if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5] # list name 
    result = sum_of_positives(my_list)
    print("The result is", result)

