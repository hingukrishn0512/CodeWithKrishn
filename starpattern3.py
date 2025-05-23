n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    # Printing spaces for the alignment of the stars
    print(" " * (n - i), end="")
    
    # Printing 'R' pattern
    if i == 1:
        print("*" * (2 * i - 1), end="")  # top row of R
    elif i < n // 2:
        print("*", end="")
        print(" " * (2 * i - 3), end="")
        print("*", end="")
    elif i == n // 2:
        print("*" * (2 * i - 1), end="")  # middle row of R
    elif i > n // 2 and i < n:
        print("*", end="")
        print(" " * (2 * i - 3), end="")
        print("*", end="")

    # Space between 'R' and 'A'
    print(" " * 3, end="")

    # Printing 'A' pattern
    if i == 1:
        print(" " * (n // 2) + "*", end="")  # top row of A
    elif i == n // 2 + 1:
        print(" " * (n // 2 - 1) + "*" * 5, end="")  # middle row of A
    elif i > 1 and i < n // 2 + 1:
        print(" " * (n // 2) + "*", end="")  # upper part of A

    # Space between 'A' and 'M'
    print(" " * 3, end="")

    # Printing 'M' pattern
    if i == 1:
        print("*" * (2 * i - 1), end="")  # top row of M
    elif i == n:
        print("*" * (2 * i - 1), end="")  # bottom row of M
    else:
        print("*", end="")
        print(" " * (2 * i - 3), end="")
        print("*", end="")

    print()  # Move to the next row
