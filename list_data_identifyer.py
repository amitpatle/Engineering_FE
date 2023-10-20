input1 = input("Enter a value: ")
# Convert the input into a list
input_list = eval(input1)

def identify(data):
    if isinstance(data, list):
        data_type = type(data)
        print(f"The data is a list. Data type: {data_type}")
    else:
        print("The given input is not a list.")

# Test the function with different inputs
identify(input_list)
