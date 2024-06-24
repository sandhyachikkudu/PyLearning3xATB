name = input("Enter your name: ")
name1 = name[::(-1)]
print(name1)

def reverse_string_loop(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string_loop("sand"))


def rever_str(d):
    a=""
    for char in d:
        a=char + a
    return a

print(rever_str("sad"))
