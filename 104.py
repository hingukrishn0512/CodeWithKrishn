n = int(input("Enter number: "))

for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n, end="")  # Print full row of stars for the first and last rows
    else:
        print("*", end=" ")      # Print a star at the beginning
        print(" " * (n - 2), end="")  # Print spaces in the middle
        print("*", end="")        # Print a star at the end
    print()  # Move to the next line
