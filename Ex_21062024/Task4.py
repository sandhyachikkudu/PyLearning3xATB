def count_v(name):
    count_vow = 0
    count_con = 0
    for i in name:
        if i in ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']:
            count_vow += 1

        else:
            count_con += 1

    return count_vow, count_con


a = count_v("hello")
print(a)

n = input("name:")
count_vow = 0
count_con = 0
for i in n:
    if i in ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']:
        count_vow += 1
    else:
        count_con += 1

print(count_vow, count_con)