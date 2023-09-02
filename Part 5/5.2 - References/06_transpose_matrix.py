def transpose(matrix: list):
 
    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    # Create an empty transposed matrix with the correct dimensions
    transposed_matrix = [[0] * num_rows for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]
    print(transposed_matrix)
 
if __name__ == "__main__":
    matrix = [[1, 2],
              [1, 2],
              ]

    transpose(matrix)

