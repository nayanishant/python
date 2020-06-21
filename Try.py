# finding factor of a given number
def factors(m):
    factor = []
    for i in range(1, m + 1):
        if m % i == 0:
            factor.append(i)
    return factor


# Finding even number between range
def even_numbers(m):
    even = []
    for i in range(0, m + 1):
        if i % 2 == 0:
            even.append(i)
    return even


num = int(input("Enter a number: "))
list_of_factors = factors(num)
list_of_even = even_numbers(num)
print(f"Factors of {num} are: {list_of_factors}")
print(f"Even numbers between 0 to {num} are: {list_of_even}")



