import os

def generationtable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n * i}\n"
    # Ensure the 'tables' directory exists
    os.makedirs('tables', exist_ok=True)
    # Save to a text file with a unique name in the 'tables' folder
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

# Generate tables for numbers 2 to 20
for i in range(2, 21):
    generationtable(i)
