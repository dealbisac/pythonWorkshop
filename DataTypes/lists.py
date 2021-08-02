#list - heterogenous / array - homogenous

#empty_list
my_list = []

#list of integers
my_list = [1, 2 , 3, 4 , 5]

print(my_list)
print(my_list[2])

#list of books
book_list = ["Rich Dad Poor Dad", "Fundamentals of Programming", "The 4 Hour a Week", "Stacey Grave"]

print("The my favourite book is " + book_list[0])


#lists with mixed data types
my_new_list = ["Dipendra Laxmi", 6, 65.6, ['C', ".Net", "Python"], "Gongabu"]

print(my_new_list)

#Accessing the list
print("++++++++++++++++My Information++++++++++++++")
print("Name : " + my_new_list[0])
print(my_new_list[1])
print(my_new_list[2])
print(my_new_list[3][2])
print("Address : " + my_new_list[4])


#negative indexing always start from -1 as the last element.
print(my_new_list[-2][-1])