# Write your solution here

def everything_reversed(list):
    new_list = []
    for item in list:
        new_item = item[::-1] # reverse item
        new_list.insert(0, new_item) #insert items in reverse order
    return new_list
        
if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
