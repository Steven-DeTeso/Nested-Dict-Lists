# 1) Update values in dictionaries and lists
    # a) Change the value 10 in x to 15. Once you're done, x should now be [[5,2,3],[15,8,9]]
    # b) Change the last_name of the first student from 'Jordan' to 'Bryant'
    # c) in the sports_directory, change 'Messi to 'Andres'
    # d) change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# solutions start here: 
#a)
x[1][0] = 15
#b)
students[0]["last_name"] = 'Bryant'
#c)
sports_directory["soccer"][0] = 'Andres'
#d)
z[0]['y'] = 30

# 2) Iterate Through a List of Dictionaries - Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# #solution starts here:

def iterateDictionary(li):
    for a in students: # iterates through list first
        for key, value in a.items(): # steps into dictionaries and iterates through them next 
            print(key, value)

iterateDictionary(students)

# 3) Get Values From a List of Dictionaries - Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

# solution starts here: 

def iterateDictionary2(key_name, some_list):
    for a in range(0, len(some_list)): # starts a for loop, looping through the list of dictionarys
        for key, value in some_list[a].items(): # grabs the key and value of the first dictionary because initally [a] = index [0], continues to loop through all dictionaries after first
            if key == key_name: #evaluates if the key's name passed in an argument is equal to the key in the dictionary. If true, it prints that keys value out. 
                print(value)

iterateDictionary2('last_name', students)

# 4) Iterate through a Dictionary with List Values - Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# solution starts here: 

def printInfo(some_dict):
    for key, val in some_dict.items(): # sets up for loop to evaluate the key and values in the passed in dictionary. .items() evalutes these. 
        print(f"{key} {len(val)}") # prints an f string and passes in the name of the key first then the length of value items stored in that key.
        for i in range(0, len(val)): # loops through the index of values in key
            print(val[i]) # prints the value at said index denoted by [i]

printInfo(dojo)