#even or odd
def even_or_odd(number):
    return 'Even' if number % 2 == 0 else 'Odd'
#convert num to string
def number_to_string(num):
    # Return a string of the number here!
    return str(num)
#vowelcount
def get_count(sentence):
    senstring = sentence.lower()
    count = 0
    listvow = "aeiou"

    for char in senstring:
        if char in listvow:
            count = count + 1
    return count