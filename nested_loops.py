#nested loop = the "inner loop" will finish all it's iterations before 
            # finishing one iteration of the "outer loop"

## Prompt the user to input the number of rows, columns, and a symbol
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

# Loop through each row
# for i in range(rows):
#     # Loop through each column in the current row
#     for j in range(columns):
#         # Print the specified symbol for the current position in the row
#         print(symbol, end="")
    
#     # Move to the next line after printing all columns in the current row
#     print()
