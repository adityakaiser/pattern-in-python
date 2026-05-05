
rows = int(input("enter your rows: "))

for i in range(1, rows + 1):
    
    print(" " * (rows - i), end="")
    
    # Print the number 'i' repeatedly 'i' times
    print(str(i) * i)