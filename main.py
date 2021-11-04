Employee = ["Raj",102,"USA"]
Dep1 = ["CS",10]
Dep2 = ["IT",11]
HOD_CS = [10,"Mr. Shyam"]
HOD_IT = [11,"Mr. Harsh"]

print("Printing employee data...")
print("Name : %s, ID = %d , Country = %s"%(Employee[0],Employee[1],Employee[2]))

print("Printing Departments...")
print("Deparment 1:\nName:%s, ID: %d\nDepartment 2:\nName:%s,ID:%s"%(Dep1[0],Dep2[1],Dep2[0],Dep2[1]))

print("HOD details...")
print(" CS HOD Name : %s,ID : %d"%(HOD_CS[1],HOD_CS[0]))
print(" IT HOD Name : %s, ID=%d"%(HOD_IT[1],HOD_IT[0]))

print(type(Employee),type(Dep1),type(Dep2),type(HOD_CS),type(HOD_IT))





emp = ["John", 102, "USA"]
Dep1 = ["CS",10]
Dep2 = ["IT",11]
HOD_CS = [10,"Mr. Holding"]
HOD_IT = [11, "Mr. Bewon"]
print("printing employee data...")
print("Name : %s, ID: %d, Country: %s"%(emp[0],emp[1],emp[2]))
print("printing departments...")
print("Department 1:\nName: %s, ID: %d\nDepartment 2:\nName: %s, ID: %s"%(Dep1[0],Dep2[1],Dep2[0],Dep2[1]))
print("HOD Details ....")
print("CS HOD Name: %s, Id: %d"%(HOD_CS[1],HOD_CS[0]))
print("IT HOD Name: %s, Id: %d"%(HOD_IT[1],HOD_IT[0]))
print(type(emp),type(Dep1),type(Dep2),type(HOD_CS),type(HOD_IT))





list = [1,2,3,4,5,6,7]
print(list[0])
print(list[1])
print(list[2])
print(list[3])

# slicing the element

print(list[0:6])

# By default the index value is 0 so its starts from the 0th element and go for index -1.

print(list[:])
print(list[2:5])
print(list[1:6:2])




list = [1,2,3,4,5,6]
print(list)

# It will assign value to the value to the second index
list[2] = 10
print(list)

# Adding multiple-element

list[1:3] = [56,78]
print(list)

# It will add value at the end of the list
list[-1] = 90
print(list)




# Declaring the empty list
l = []

# Number of elements entered by the users

n = int(input(" * Enter number in list"))

# for - loop to take the input
for i in range(0,n):
    l.append(input(" Enter item :"))
print(" * Printing the list items...")

for i in l:
    print(i,end=" ")

a = [6, 4, 6, 6, 8, 12]

for item in a:
    a.remove(6)
print(a)




list = [0,1,2,3,4]
print(" original list :")
for i in list:
    print(i,end = " ")
list.remove(2)
print(" \n after removal of 2nd element:")




my_list = [2, 4, 6, 8, 10, 12]

# remove item present at index 2
my_list.pop(2)
print(my_list)
# Output [2, 4, 8, 10, 12]

# remove item without passing index number
my_list.pop()
print(my_list)
# Output [2, 4, 8, 10]


list1 = [1,2,2,3,55,98,65,65,13,29]

# an empty list to store unique values
list2 = []

for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

for i in list:
    print(i,end=" ")
