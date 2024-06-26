t1 = ("sand","and","my")
t2 = ("mad","dya","mine")
t3 = t1 + t2
print(t3)
t4 = (t1,t2)
print(t4)
print(t4[0])
print(t4[0][0])

t5=tuple(["ans","qn"])
print(t5)


# unpacking of tuple
p,q,r = (32,24,15)


# in operator

cities = ("hyd","bang","chennai")
print("hyd" in cities)



# tuple
t = (1,2,3)

# 'tuple' object has no attribute 'append'
# t.append(4)
print(t)
tnew = t+(4,)
print(tnew)


# set
# collection of unique items
list = [1,2,3,4,5]
unique = set(list)
print(unique)
print(len(unique))
tuple_set = ('sand','and','sand')
print(set(tuple_set))

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))
print(set1.symmetric_difference(set1))



se1 = {1,2,3,4,5}
se2 = {1,4,5}
print(se2.issubset(se1))
print(se1.issubset(se2))

w = set(["sand","and","and."])
print(len(w))


d = {1,2,3,4,5}
print(len(d))
d.remove(1)
print(len(d))
print(d.pop())
print(d.add(20))
print(d)



























