#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.'''

def hello_name(user_name):
    print ("hello_", user_name, "!")

hello_name("Kovid")

#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for number in range(1,100,2):
        print (number)

first_odds()

#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_number_in_list(a_list):
    a_list= [int(i)for i in a_list]
    return max(a_list)

max_number_in_list([1,2,34,5,3,21,4,193])
#this doesn't seem to be working and I'm not sure why 

#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    a_year: int(a_year)
    if a_year % 400 == 0:
        print ("this is a leap year")
    elif a_year % 4 ==0 and a_year %100 != 0:
        print ("this is a leap year")
    else:
        print ("this is not a leap year")

is_leap_year(213)

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

#I'm not sure how to do this one









