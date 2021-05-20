num1 = int(input('введите целое положительное число= '))
min  = 9
while num1 // 10 > 0:
     if min > num1 % 10:
         min = num1 % 10
         num1 = num1 // 10
         print(min)