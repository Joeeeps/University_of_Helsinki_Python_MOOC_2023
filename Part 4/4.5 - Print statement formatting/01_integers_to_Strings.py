# Write your solution here

def formatted(my_list):
    new_list = [f"{item:.2f}" for item in my_list]
    return new_list

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)
