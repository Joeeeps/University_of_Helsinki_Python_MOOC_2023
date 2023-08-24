# Write your solution here
def no_shouting(shout):
    pruned_list = []
    for item in shout:
        if not item.isupper():  # Check if the item is not all uppercase
            pruned_list.append(item)
    return pruned_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
