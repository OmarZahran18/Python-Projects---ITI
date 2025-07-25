from vowels_and_location_i import counter_vowels , location_of_i
from valid_emails import filter_valid_emails , check_email_attempts
from users_data import get_user_data , check_user_login
from sorted_array import sorted_array
from mario_pyramid import mario_pyramid , right_aligned_pyramid
from mamultiplication import mamultiplication_table , generate_a_multiplication_table 

text = "My Name is Omar Zahran"

print("Vowel Tasks")
counter_vowels(text)
location_of_i(text)
print("-" * 60)

print("Email Tasks")
filter_valid_emails()
print("-" * 60)
check_email_attempts()
print("-" * 60)

print("User Info")
get_user_data()
print("-" * 60)
check_user_login()
print("-" * 60)

print("Array Sorting")
sorted_array()
print("-" * 60)

print("Mario Pyramids")
mario_pyramid()
print("-" * 60)
right_aligned_pyramid()
print("-" * 60)

print("Multiplication Tasks")
mamultiplication_table()
print("-" * 60)
generate_a_multiplication_table()
print("-" * 60)

