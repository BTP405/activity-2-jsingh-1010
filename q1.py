def getPrimeNumbers(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False


n = int(input("Enter the desired number: "))
if getPrimeNumbers(n):
    print("The number is a prime number")
else:
    print("The provided number is not a prime number")
