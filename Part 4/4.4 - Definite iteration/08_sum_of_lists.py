# Write your solution here
#Write solution in here
def list_sum(list_a, list_b):
    list_c = [a + b for a, b in zip(list_a, list_b)]
    return list_c

#zip function combines the lists, then can add them together
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    result = list_sum(a, b)
    print(result)  # Output: [8, 10, 12]

#Notes from suggested solution
# Another solution would be use zip-function,
# which creates new list by combining items in two or more lists
# for item1, item2 in zip(list1, list2):
#   results.append(item1 + item2)
# Write your solution here