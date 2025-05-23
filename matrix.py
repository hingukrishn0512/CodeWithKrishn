def matrix_add():
    rows = int(input("enter the number of rows : "))
    columns = int(input("enter the number of columns : "))

    print("enter the values for matrix A :" )
    A = []
    for i in range (rows):
        row = []
        for j in range(columns):
            value = int(input(f"A[{i}][{j}] : "))
            row.append(value)
        A.append(row)
     
    print("enter the values for matrix b :" )
    B = []
    for i in range (rows):
        row = []
        for j in range(columns):
            value = int(input(f"B[{i}][{j}] : "))
            row.append(value)
        B.append(row)

    result = []

    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(A[i][j] + B[i][j])
        result.append(row)

    print("\nthe result is")
    for row in result:
        print(row)
matrix_add()