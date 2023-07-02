#this is the program for displaying total shopping cart based on input

gc_start = '**'
print(gc_start*45)
print(gc_start*18, 'Welcome to the store', gc_start*16)
print(gc_start*45)
gv_item = input('Enter the item you want to buy:')
gv_itemc =int(input('Enter the count of item you want to buy:'))
if gv_itemc < 0:
    print("Enter only Positive numbers")
    exit()
gv_itemp = float(input('Enter the price of item you want to buy:'))
if gv_itemc == 1:
    print(f"Total cost of ", gv_itemc, gv_item , f"is: ${float(gv_itemp*gv_itemc)}")
else:
    print(f"Total cost of ", gv_itemc, gv_item+"s", f"is: ${float(gv_itemp*gv_itemc)}")