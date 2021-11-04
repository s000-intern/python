# create a dictionary using {}
person = {"Name": "Deepali", "Country": "India", "Telephone": 56789}
print(person)

# create a dictionary using dict()
person = dict({"Name": "Deepali", "Country": "India", "Telephone": 56789})
print(person)

# create a dictionary from sequence having each item as a pair
person = dict([("Name", "Harsh"), ("Country", "USA"), ("Telephone", 11789)])
print(person)

# create dictionary with mixed keys keys
# first key is string and second is an integer
sample_dict = {"Name": "Deepali", 10: "Mobile"}
print(sample_dict)

# create dictionary with value as a list
person = {"Name": "Deepali", "Telephones": [1178, 2563, 4569]}


# create a dictionary named person
person = {"Name": "Deepali", "Country": "India", "Telephone": 56789}

# access value using key name in []
print(person['Name'])

#  get key value using key name in get()
print(person.get('Telephone'))


person = {"name": "Deepali", "country": "India", "telephone": 1178}

# Get all keys
print(person.keys())

print(type(person.keys()))


# Get all values
print(person.values())
print(type(person.values()))

# Get all key-value pair
print(person.items())
print(type(person.items()))


person = {"name": "Deepali", "country": "India", "telephone": 1178}

# Iterating the dictionary using for-loop
print('key', ':', 'value')
for key in person:
    print(key, ':', person[key])

print("\n")

# using items() method
print('key', ':', 'value')
for key_value in person.items():
    # first is key, and second is value
    print(key_value[0], key_value[1])

    person = {"name": "Deepali", "country": "India", "telephone": 1178}

    # count number of keys present in  a dictionary
    print(len(person))

    person = {"name": "Deepali", "country": "India", "telephone": 1178}

    # update dictionary by adding 2 new keys
    person["weight"] = 50
    person.update({"height": 6})

    # print the updated dictionary
    print(person)

    person_details = {"name": "Deepali", "country": "India", "telephone": 1178}

    # set default value if key doesn't exists
    person_details.setdefault('state', 'Texas')

    # key doesn't exists and value not mentioned. default None
    person_details.setdefault("zip")

    # key exists and value mentioned. doesn't  change value
    person_details.setdefault('country', 'Canada')

    # Display dictionary
    for key, value in person_details.items():
        print(key, ':', value)

        person = {"name": "Deepali", "country": "India"}

        # updating the country name
        person["country"] = "Canada"
        # print the updated country
        print(person['country'])

        # updating the country name using update() method
        person.update({"country": "USA"})
        # print the updated country
        print(person['country'])

        person = {'name': 'Deepali', 'country': 'India', 'telephone': 2834, 'weight': 58, 'height': 6}

        # Remove last inserted item from the dictionary
        deleted_item = person.popitem()
        print(deleted_item)  # output ('height', 6)
        # display updated dictionary
        print(person)

        # Remove key 'telephone' from the dictionary
        deleted_item = person.pop('telephone')
        print(deleted_item)  # output 1178
        # display updated dictionary
        print(person)

        # delete key 'weight'
        del person['weight']
        # display updated dictionary
        print(person)

        # remove all item (key-values) from dict
        person.clear()
        # display updated dictionary
        print(person)  # {}

        # Delete the entire dictionary
        del person

        person = {'name': 'Deepali', 'country': 'India', 'telephone': 2834, 'weight': 50, 'height': 6}

        # Get the list of keys and check if 'country' key is present
        key_name = 'country'
        if key_name in person.keys():
            print("country name is", person[key_name])
        else:
            print("Key not found")

            dict1 = {'Deepali': 25, 'Arun': 80, 'Meena': 55}
            dict2 = {'Kelvin': 68, 'Harry': 50, 'Om': 66}

            # copy second dictionary into first dictionary
            dict1.update(dict2)
            # printing the updated dictionary
            print(dict1)

            # each dictionary will store data of a single student
            Deepali = {'Name': 'Deepali', 'State': 'Maharashtra', 'City': 'Mumbai', 'Marks': 75}
            Emma = {'Name': 'Emma', 'State': 'Texas', 'City': 'Dallas', 'Marks': 60}
            kelvin = {'Name': 'Kelvin', 'State': 'Texas', 'City': 'Austin', 'Marks': 85}

            # Outer dictionary to store all student dictionaries (nested dictionaries)
            class_six = {'student1': Deepali, 'student2': Emma, 'student3': kelvin}

            # Get student3's name and mark
            print("Student 3 name:", class_six['student3']['Name'])
            print("Student 3 marks:", class_six['student3']['Marks'])

            # Iterating outer dictionary
            print("\nClass details\n")
            for key, value in class_six.items():
                # Iterating through nested dictionary
                # Display each student data
                print(key)
                for nested_key, nested_value in value.items():
                    print(nested_key, ':', nested_value)
                print('\n')

                # calculate the square of each even number from a list and store in dict
                numbers = [1, 3, 5, 2, 8]
                even_squares = {x: x ** 2 for x in numbers if x % 2 == 0}
                print(even_squares)

                # dictionary with both 'true' keys
                dict1 = {1: 'True', 1: 'False'}

                # dictionary with one false key
                dict2 = {0: 'True', 1: 'False'}

                # empty dictionary
                dict3 = {}

                # '0' is true actually
                dict4 = {'0': False}

                # dictionary with both 'true' keys
                dict1 = {1: 'True', 1: 'False'}

                # dictionary with one false key
                dict2 = {0: 'True', 1: 'False'}

                # empty dictionary
                dict3 = {}

                # '0' is true actually
                dict4 = {'0': False}

                # all false
                dict5 = {0: False}

                print('All True Keys::', any(dict1))
                print('One False Key ::', any(dict2))
                print('Empty Dictionary ::', any(dict3))
                print('With 0 in single quotes ::', any(dict4))
                print('all false :: ', any(dict5))

                print('All True Keys::', all(dict1))
                print('One False Key', all(dict2))
                print('Empty Dictionary', all(dict3))
                print('With 0 in single quotes', all(dict4))