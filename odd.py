# Take input from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Create list of squares
squares = []
for num in range(start, end + 1):
    squares.append(num * num)

# Separate odd and even square values
even_squares = []
odd_squares = []
for value in squares:
    if value % 2 == 0:
        even_squares.append(value)
    else:
        odd_squares.append(value)

#Display result
print("\nSquares of numbers in the given range:")
print(squares)
print("\nEven square values:")
print(even_squares)
print("\nOdd square values:")
print(odd_squares)