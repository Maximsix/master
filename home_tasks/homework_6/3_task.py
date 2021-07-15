
def search_prime_number(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number

