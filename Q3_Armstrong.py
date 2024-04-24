num = int(input("Input any Number to check if it is Armstrong or not: "))

sum = 0
tempNum = num
while tempNum > 0:
   digit = tempNum % 10
   sum += digit ** 3
   tempNum //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")