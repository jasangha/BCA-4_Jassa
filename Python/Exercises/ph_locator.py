import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import os

n = input("Enter a Phone number to track: ")
number = "+91"+str(n)
print(number)

a = phonenumbers.parse(number)
b = phonenumbers.parse(number,"RO")

if len(n) == 10:
    print("country:\t",geocoder.description_for_number(a, "en"))
    print("ISP Provider:   ",carrier.name_for_number(b, "en"))
    file = "jassa.wav"
    os.system(file)
else:
    print("Entered number is incorrect!!")
    