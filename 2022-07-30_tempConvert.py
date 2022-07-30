# convert between temperatures
# 2022-07-30

def c2f(c):
    return (c * 9 / 5) + 32
def f2c(f):
    return (f-32) * 5 / 9

def isFloat(v):
    try:
        float(v)
        return True
    except ValueError:
        return False

convertFrom = ''
while convertFrom == '':
    convertFrom = input('What do you want to convert FROM? (c/f)')
    if convertFrom not in ('c', 'f'):
        print('Error, type c or f')
        convertFrom = ''

temp = ''
while temp == '':
    temp = input('What temperature to convert?')
    if not isFloat(temp):
        print('Give me a number')
        temp = ''
    else:
        temp = float(temp)

result = 0
if convertFrom == 'c':
    result = c2f(temp)
elif convertFrom == 'f':
    result = f2c(temp)

finalStatement = 'Temperature' +str(temp)+str(convertFrom)+ ' converts to: ' + str(result) + str('f' if convertFrom == 'c' else 'c')
print(finalStatement)
