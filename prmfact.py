number=int(raw_input("Enter the number: "))
def prime_factors(number):
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number /= divisor

        divisor += 1

    print factors
    
prime_factors(number)