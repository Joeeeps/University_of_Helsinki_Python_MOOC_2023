# Write your solution here
def same_chars(word, x, y):
    if len(word) > x and len(word) > y and word[x] == word[y]:
        return(True)
    else:
        return(False)
 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abracadabra", 0,3))
