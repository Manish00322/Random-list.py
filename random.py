import random

def generate_nested_tuple(num_tuples, manual_input):
    nested_tuple = ()
  
    for i in range(num_tuples):
        if manual_input:
            values = input(f"Enter values for tuple {i+1} (comma separated): ")
            values = tuple(values.split(","))
        else:
            values = tuple(random.sample(range(1, 10), random.randint(1, 5)))
        
        nested_tuple += (values,)

    return nested_tuple

# Ask the user for the number of tuples to combine
num_tuples = int(input("Enter the number of tuples to combine: "))

# Ask the user if they want to enter the tuple manually or generate random values
manual_input = input("Do you want to enter the tuple manually? (y/n): ")
manual_input = manual_input.lower() == "y"

# Generate the nested tuple using the given inputs
result = generate_nested_tuple(num_tuples, manual_input)

# Print the nested tuple
print(f"Nested tuple: {result}")