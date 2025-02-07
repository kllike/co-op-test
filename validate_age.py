from validate_age import *

age = int(input ("Enter your age: "))
validate_age(age)

def validate_age(age):
    if age < 18:
    print ("Not eligible for voting\n\n ")
    else:
        print( "Eligible for voting\n\n")