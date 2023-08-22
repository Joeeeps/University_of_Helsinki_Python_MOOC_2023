# Write your solution here
def range_of_list(x):
    maximum = max(x) # avoid conflict with maximum and max() functions
    minimum = min(x)
    range_value = maximum - minimum
    return range_value

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = range_of_list(my_list)
    print("The range of the list is", result)
