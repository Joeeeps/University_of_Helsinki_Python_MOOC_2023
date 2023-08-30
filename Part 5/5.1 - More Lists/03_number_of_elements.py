# Write your solution here 
#You can also have lists within lists

def count_matching_elements(my_matrix:list, element: int):
    i = 0 
    for row in my_matrix:
        for value in row:
            if value == element:
                i += 1 
 
    return i 
        
    

#take a 2d ray of integers and single integer value as arguments
#function counts no of elements within matrix 


if __name__ == "__main__":
    m = [[1, 2, 3], [2, 3, 1], [4, 5, 6]]
    print(count_matching_elements(m, 2)) #list and integer
