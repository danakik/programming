from math import *

print('Multiparadigm programming languages : Task 3')
print('Danil Mashkin, FI-9119')

x = int(input('Input x: '))
y = int(input('Input y: '))

if x == y:
    print('ERROR')
else:
    num_z = (1 / ((x**3) - (y**3))) - sqrt(2 * x)
    print(round(num_z, 5))
