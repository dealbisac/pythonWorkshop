#defining the strings
#hello again

my_string = 'Dipendra Laxmi'
print(my_string)
print('First Letter', my_string[0])
print(':Last Letter', my_string[-1])


# Strings are immutable
# my_string = 'e'
# print(my_string)

my_string = 'Dependra Laxmi'
print(my_string)
print(my_string[8])

my_address = 'Kathmandu'
print(my_address)

my_love = '''Python'''
print(my_love)

#multiple line in the python
my_description = """Hello this is me and I love being myself
and love coding and singing as well as travelling.
I love making new friends.
"""

print(my_description)


#concatenation of string (+, *)
str1 = " Hello"
str2 = " Guys"

#use of +
print('str1 + str2 =', str1 + str2)

#use of *
print('str1 *3', str1*3)


#Escape Characters
statement = 'She said "I don\'t want this"'
print(statement)