name = "Sanjana"
print(type(name))

# display "name" str
print(name)

#accessing 3rd charcter of the str
print(name[3])

# store int value
roll_no = 33
# display roll no
print("Roll number is:", roll_no)
# output 33
print(type(roll_no))
# output class 'int'

# store integer using int() class
id = int(25)
print(id)  # 25
print(type(id))  # class 'int'



# store a floating-point value
emp_salary = 8000.456
print("Salary is :", emp_salary)  # 8000.456
print(type(emp_salary))  # class 'float'

# store a floating-point value using float() class
num = float(54.75)
print(num)  # 54.75
print(type(num))  # class 'float'


# store a floating-point value
emp_salary = 8000.456
print("Salary is :", emp_salary)  # 8000.456
print(type(emp_salary))  # class 'float'

# store a floating-point value using float() class
num = float(54.75)
print(num)  # 54.75
print(type(num))  # class 'float'


mylist =  [ "Meghana", "Sanjana", " Sahana " , "Vyoma"]

b = len(mylist) ## This will return the length of the list which is 4. The index is 0, 1, 2, 3,4.

print("total element in mylist are : ",b)

print(mylist[1])     ## This will return the value at index 1, which is "Deepali"
print(mylist[0:2])  ## This will return the first 2 elements in the list.



mylist = [0,1,2,3,4]
mylist[0] = 'Meghana'
mylist[1] = "Sanjana"
mylist[2] = 'Sahana'
mylist[3] = 'Vyoma'
print( mylist[1])



mylist = ['Sanjana', 'Rani', 'Harsh']
mylist.append('shemp')         ## append elem at end
mylist.insert(0, 'xxx')        ## insert elem at index 0
mylist.extend(['yyy', 'zzz'])  ## add list of elems at end
print (mylist)  ## ['xxx', 'Deepali', 'Rani', 'Harsh', 'shemp', 'yyy', 'zzz']
print (mylist.index('Rani'))    ## 2

mylist.remove('Rani')         ## search and remove that element
mylist.pop(1)                  ## removes and returns 'larry'
print (mylist)



mylist = ['a', 'b', 'c', 'd']
print(mylist[1:-1])   ## ['b', 'c']
mylist[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print (mylist)         ## ['z', 'c', 'd']



# create a tuple
my_tuple = (11, 24, 56, 88, 78)
print(my_tuple)  # (11, 24, 56, 88, 78)
print(type(my_tuple))  # class 'tuple'

# Accessing 3rd element of a tuple
print(my_tuple[2])  # 56

# slice a tuple
print(my_tuple[2:7])  # (56, 88, 78)

# create a tuple using a tuple() class
my_tuple2 = tuple((10, 20, 30, 40))
print(my_tuple2)  # (10, 20, 30, 40)


# create a dictionary
my_dict = {1: "Deepali", 2: "Neelam", 3: "Jaya"}

# display dictionary
print(my_dict)  # {1:"Deepali", 2: "Neelam", 3: "Jaya"}
print(type(my_dict))  # class 'dict'

# create a dictionary using a dit class
my_dict = dict({1: "Sanjana", 2: "Vyoma", 3: "Jaya"})

# display dictionary
print(my_dict)  # {1: "Sanjana", 2: "Vyoma", 3: "Jaya"}
print(type(my_dict))  # class 'dict'

# access value using a key name
print(my_dict[1])  # Sanjana

# change the value of a key
my_dict[1] = "Kelly"
print(my_dict[1])  # Kelly



# create a set using curly brackets{,}
my_set = {100, 25.75, "Sanjana"}
print(my_set)  # {25.75, 100, "Sanjana"}
print(type(my_set))  # class 'set'

# create a set using set class
my_set = set({100, 25.75, "Sanjana"})
print(my_set)  # {25.75, 100, 'Sanjana'}
print(type(my_set))  # class 'set'

# add element to set
my_set.add(300)
print(my_set)  # {25.75, 100, 'Sanjana', 300}

# remove element from set
my_set.remove(100)
print(my_set)  # {25.75, 'Sanjana', 300}