# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2, rows1, cols1, cols2):
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Perform multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Main program
if __name__ == "__main__":
    # Input dimensions of the first matrix
    rows1 = int(input("Enter the number of rows for the first matrix: "))
    cols1 = int(input("Enter the number of columns for the first matrix: "))

    # Input dimensions of the second matrix
    rows2 = int(input("Enter the number of rows for the second matrix: "))
    cols2 = int(input("Enter the number of columns for the second matrix: "))

    # Check if multiplication is possible
    if cols1 != rows2:
        print("Matrix multiplication not possible. The number of columns in the first matrix must equal the number of rows in the second matrix.")
        exit()

    # Input elements of the first matrix
    print(f"\nEnter the elements for the first {rows1}x{cols1} matrix:")
    matrix1 = []
    for i in range(rows1):
        row = list(map(int, input(f"Enter row {i + 1} (space-separated): ").split()))
        matrix1.append(row)

    # Input elements of the second matrix
    print(f"\nEnter the elements for the second {rows2}x{cols2} matrix:")
    matrix2 = []
    for i in range(rows2):
        row = list(map(int, input(f"Enter row {i + 1} (space-separated): ").split()))
        matrix2.append(row)

    # Perform matrix multiplication
    result = multiply_matrices(matrix1, matrix2, rows1, cols1, cols2)

    # Display the result
    print("\nResultant Matrix:")
    for row in result:
        print(row)
