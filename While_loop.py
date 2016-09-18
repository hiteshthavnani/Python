import math
number = input('Enter the integer greater than 2:\t')
number = int(number)
while True:
    for i in range(1,100):
        if number > 2:
            number = math.sqrt(number)
            print('%d: %.3f' %(i,number))
    break
