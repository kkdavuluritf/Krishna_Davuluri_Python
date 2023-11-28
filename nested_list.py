# Get the number of sublists
num_sublists = int(input("Enter the number of sublists: "))

# Create an empty list to store the sublists
nested_list = []

# Iterate over the number of sublists
for i in range(num_sublists):
    # Create an empty list for the current sublist
    sublist = []

    # Get the number of elements in the current sublist
    num_elements = int(input("Enter the number of elements in sublist " + str(i + 1) + ": "))

    # Iterate over the number of elements in the sublist
    for j in range(num_elements):
        element = int(input("Enter element " + str(j + 1) + " of sublist " + str(i + 1) + ": "))
        sublist.append(element)

    # Append the sublist to the nested list
    nested_list.append(sublist)

# Print the nested list
print(nested_list)
##Use code with caution. Learn more
##This method involves using nested loops to collect input for both the sublists and their individual elements. It provides more control over the input process.

##Method 2: Using list comprehension

#3Python
# Get the nested list input as a string
input_string = input("Enter the nested list (e.g., [[1, 2, 3], [4, 5]]): ")

# Convert the input string to a nested list using eval()
nested_list = eval(input_string)

# Print the nested list
print(nested_list)