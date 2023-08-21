# Write your solution here
def hash_square(length):
    hash = length
    while length > 0:
        print("#"*hash)
        length -= 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)
