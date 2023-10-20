# Initialize a variable called 'number' with a value of -1.
number = -1  # This variable keeps track of the number of '+' signs in each layer.

# Prompt the user to input the number of layers they want in the tree. 
Range = int(input("How many layers do you want the tree?"))

# Create a for loop that iterates through each layer from 0 to the number of layers minus 1.
for x in range(0, Range):
    # Increment the 'number' variable by 2 (each layer has 2 more '+' signs than the previous one).
    number = number + 2
    
    # Use string formatting to create spaces and '+' signs for the current layer.
    # The " " * (Range - x) part creates spaces, and the "+" * number part creates '+' signs.
    spaces = " " * (Range - x)
    plus_signs = "+" * number
    
    # Print the result to the console. This will display the current layer of the tree.
    print(spaces + plus_signs)
