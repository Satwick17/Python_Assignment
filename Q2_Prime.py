
# Function to check prime number
def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


num = int(input("Input any Number to check if it is prime or not: "))
if(isPrime(num)):
    print(num, "is Prime")
else:
    print(num, "is not Prime")

