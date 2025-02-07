form get_name import *
form validate_age import *
form survaey import *

print("="*35)
print("Welcome to voting eligilibity check")
print("="*35)
print("/n")


user_name = get_namme()
print(f"Hello {user_name}!\n")

age = int(input("Enter your age:"))
validate_age(age)

survaey_flag = input("Would you like to participate in our survey (y/n):")

if survaey_flag == 'Y':
    survaey()

    print("\nThank you! Please visit again.\n\n")