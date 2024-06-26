numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(num):
    return num % 2 == 0


def is_odd(num1):
    return num1 % 2 != 0


def greaterthann_5(num):
    return num > 5


def map_numbers(num):
    return num * 2


new_map = map(map_numbers, numbers)
print(list(new_map))

l = map(lambda num: num * 2,numbers)
print(list(l))


new_numbers_even = filter(is_even, numbers)
print(list(new_numbers_even))

new_greater = filter(greaterthann_5, numbers)
print(list(new_greater))

new_odd_numbers = filter(is_odd, numbers)
print(list(new_odd_numbers))
# vowels

letters = ['a', 'e', 'i', 'o', 'u']


def vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels


s = vowels('e')
print(s)

d = filter(vowels, letters)
print(list(d))
