
def search_rime_number(number: int) -> int:
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number
