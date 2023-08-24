# Write your solution here

def all_the_longest(my_list):
    longest = ""
    longest_list = []
    for item in my_list:
        if len(item) > len(longest):
            longest = item
    for item in my_list:
        if len(item) == len(longest):
            longest_list.append(item)
    return longest_list

if __name__ == "__main__":
    my_list = ["one", "two", "three", "four", "seven", "eight"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']
