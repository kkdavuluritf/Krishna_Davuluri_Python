new_tuple=(1,2,3,4,77)
new_tuple2=new_tuple+([656,454,565],)  # Comma used to declare type as tuple

print("Tuple and list", new_tuple2)
new_tuple_string = str(new_tuple2)  # convert them to string otherwise print(wont work)
print('77' in new_tuple_string)
new_tuple_square=(0,)
##new_tuple_square=(2**item for item in new_tuple2)  # this worn work as we need For loop
print('Sqaures:', new_tuple_square)
    
    

