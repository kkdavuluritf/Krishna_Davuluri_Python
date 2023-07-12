import cmath
def calc_power(number,power):
    return(number**power)

numb = float(input('Please input a number to calculate power:'))
pow  = float(input('Enter a power value:'))
value = calc_power(numb,pow)
print('Power vlue is:', value)
