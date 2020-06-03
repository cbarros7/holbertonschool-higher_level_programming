#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(7)
my_list.append(5)
my_list.append(3)

print(my_list)
my_list.print_sorted()
print(my_list)
