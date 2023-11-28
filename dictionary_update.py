"""# Initialize an empty dictionary
my_dict = {}

# Prompt for user input
while True:
  key = input("Enter a key (or type 'done' to finish): ")
  if key == "done":
    break
  value = input("Enter a value for " + key + ": ")

  # Add key-value pair to dictionary
  my_dict[key] = value

# Print the final dictionary
print("The final dictionary is:", my_dict) 
"""
list_keys=[]
list_values=[]
my_dict = {}
key1 = input("Enter a key Name, None to break: ")
while True:
    list_keys.append(key1)
    key = input(f"Enter values for {key1}, None to break: ")
    if key == "None":
        break
    else:
        list_keys.append(key)
    my_dict.update(key=list_keys) ## update keys
value1 = input("Enter a Value name, None to break: ")
while True:
    list_values.append(value1)
    value = input(f"Enter a values for {value1}, None to break: ")
    if value == "None":
        break
    else:
        list_values.append(value)
    my_dict.update(value=list_values)## update values
 
##my_dict.update({key: value})
  
print(my_dict)
#print(my_dict.keys())
#print(my_dict.values())

