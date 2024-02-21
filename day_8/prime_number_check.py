def prime_checker(number):
    is_prime = True
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                is_prime = False
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


n = int(input("Enter number to check for prime: "))
prime_checker(number=n)