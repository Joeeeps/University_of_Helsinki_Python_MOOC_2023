# Write your solution here
def list_of_stars(list):
    for num in list:
        print("*" * num)

if __name__ == "__main__":
    my_list = [5, 4, 3]
    list_of_stars(my_list)
