list_string=['ProbeTest', 1,2,3,4,[10,20,890],True,False, 'Davuluri']
n = len(list_string)
##for i in range(n):
#print(list_string[:])
#print(list_string[-3][1])"" list index + range
#print(list_string[0][3])

##for i in range(n):
for i in list_string:
    if type(i) == str:
        print(i)
