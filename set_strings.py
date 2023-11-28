## assignment
new_set = set("macbook")
# check if 'a' is present
# Output: True
print('a' in new_set)

def count_characters(string, p_set):
##"""Counts the number of occurrences of each character in a string."""
    count_string = 0
    for char in p_set:
        if char == string:
            count_string = count_string + 1
    return count_string
print('Set value:', new_set)
print(f'count of a in {new_set} is:', count_characters('a', new_set))

