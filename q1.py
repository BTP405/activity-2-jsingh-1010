def getPrimeNumbers(num):
    """ 
    Determine whether a given number is a prime number.
    The argument is the number (int) that has to be checked.
    Returns: bool: True in the event that the number is prime; false otherwise.
    """
    
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False

# Input from user
n = int(input("Enter the desired number: "))
if getPrimeNumbers(n):
    print("The number is a prime number")
else:
    print("The provided number is not a prime number")
