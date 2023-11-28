NList=[["Mumbai","India",2000],["New York","USA",10000]]
list_kids=[['Nithya',8,'Hyderabad'], ['Samaira',9,'Chennai']]
Dict1={}
kids_dict={}
N=len(NList)
i=0
for i in NList:
    city=i[0]
    country=i[1]   #3 nested loop 1 and 2
    distance=i[2]  #3 nested loop 1 and 2
    Dict1[city]=[country,distance]
print(Dict1)



len_kids = len(list_kids)

i=0
for i in list_kids:
    kid = i[0] #"Name"
    age = i[1] #"Age"
    cob = i[2] #"City of birth"
    kids_dict[kid]=[age,cob]

print('Kids Dictionary', kids_dict)
