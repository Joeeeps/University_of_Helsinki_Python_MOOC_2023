def no_vowels(my_string: str):
    vowels = ["a","e","i","o","u"]
    for character in vowels:
        my_string = my_string.replace(character, "")
    return my_string

# Write your solution here

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
