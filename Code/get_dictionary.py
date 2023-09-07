items={'Coconut':4.5, 'Mango':1.5, 'Banana':0.25, 'Apples':0.5, 'PineApple':1.25}

product = input('Please enter the fruit which you want to know Price:')
product = product.capitalize()
price = items.get(product)

if price:
    print(f'Cost of the', product, 'is:', price)
else:
    print('Sorry prodcut was not there in dictionary')