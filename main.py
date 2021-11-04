# create a tuple using ()
# number tuple
number_tuple = (10, 20, 25.75)
print(number_tuple)
# Output (10, 20, 25.75)

# string tuple
string_tuple = ('Deepali', 'Nikita', 'Pooja')
print(string_tuple)
# Output (''Deepali', 'Nikita', 'Pooja')

# mixed type tuple
sample_tuple = ('Deepali', 30, 45.75, [25, 78])
print(sample_tuple)
# Output ('Deepali', 30, 45.75, [25, 78])

# create a tuple using tuple() constructor
sample_tuple2 = tuple(('Deepali', 30, 45.75, [23, 78]))
print(sample_tuple2)
# Output ('Deepali', 30, 45.75, [23, 78])


# packing variable into tuple

tup1 = 1,2,"hello"
print(tup1)

print(type(tup1))

# unpacking variable into tuple

a,b,c=tup1
print(tup1)



tup = ["p","y","t","h","o","n"]
print(len(tup))


# create a tuple
tup1 = (1,2,3,"hi",[4,5,6])

# iterate a tuple
for i in tup1:
    print(i)

tuple1 = ('P', 'Y', 'T', 'H', 'O', 'N')
# Negative indexing
# print last item of a tuple
print(tuple1[-1])  # N
# print second last
print(tuple1[-2])  # O

# iterate a tuple using negative indexing
for i in range(-6, 0):
    print(tuple1[i], end=", ")
    # Output P, Y, T, H, O, N,

    tuple1 = (10, 20, 30, 40, 50)

    # get index of item 30
    position = tuple1.index(30)
    print(position)

    tuple1 = (10, 20, 30, 40, 50, 60, 70, 80)
    # Limit the search locations using start and end
    # search only from location 4 to 6
    # start = 4 and end = 6
    # get index of item 60
    position = tuple1.index(60, 4, 6)
    print(position)



tuple1 = (10, 20, 30, 40, 50, 60, 70, 80)
# checking whether item 50 exists in tuple
print(50 in tuple1)
# Output True
print(500 in tuple1)
# Output False


tup1 = (1,2,3,4,5)

#coverting tuple into list
a = list(tup1)
a.append(6)

# converting list back into tuple
tup1=tuple(a)
print(tup1)



tup = (5,6,7,[8,9,10])
print(tup)

# modifing last item first value:
tup[3][0] = 89
print(tup)


a = (2,3,4,5,6)
del a
print(a)


tuple1 = (0, 1, 2, 3, 4, 5)

# converting tuple into a list
sample_list = list(tuple1)
# reomve 2nd item
sample_list.remove(2)

# converting list back into a tuple
tuple1 = tuple(sample_list)
print(tuple1)
# Output (0, 1, 3, 4, 5)



tuple1 = (10, 20, 60, 30, 60, 40, 60)
# Count all occurrences of item 60
count = tuple1.count(60)
print(count)
# Output 3

count = tuple1.count(600)
print(count)
# Output 0


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)

# concatenate tuples using + operator
tuple3 = tuple1 + tuple2
print(tuple3)
# Output (1, 2, 3, 4, 5, 3, 4, 5, 6, 7)



tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)

# using sum function
tuple3 = sum((tuple1, tuple2), ())
print(tuple3)
# Output (1, 2, 3, 4, 5, 3, 4, 5, 6, 7)


nest_tup = ((1,2,3),(4,5,6),"python")

# access the first item of the third tuple
print(nest_tup[2][0])

# iterate a nested tuple
for i in nest_tup:
    print("tuple",i,"element")
    for j in i:
        print(j,end=",")
    print("\n")

tuple1 = ('xyz', 'zara', 'abc')
# The Maximum value in a string tuple
print(max(tuple1))
# Output zara

# The minimum value in a string tuple
print(min(tuple1))
# Output abc

tuple2 = (11, 22, 10, 4)
# The Maximum value in a integer tuple
print(max(tuple2))
# Output 22
# The minimum value in a integer tuple
print(min(tuple2))
# Output 4


tuple3 = ('a', 'e', 11, 22, 15)
# max item
print(max(tuple3))