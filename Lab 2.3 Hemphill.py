#Locke Hemphill
#9/29/25
#Pd 8

import os
os.system("cls")



#Task #1 (Text Formatting)
print("Task #1")
full_name = input("What is your first and last name?\t")

#seperating first and last name
first_name = full_name[:full_name.find(" ",0)]
last_name = full_name[full_name.find(" ",0)+1:]

#printing First-name, Last-name
print(first_name.title()+", "+last_name.title())
#printing fIRST-NAME, lAST-NAME
print(first_name[0].lower()+first_name[1:].upper()+", "+last_name[0].lower()+last_name[1:].upper())



#Task #2 (Simple Encryption)
print("\nTask #2")
phrase1 = "Once you start down the dark path, forever will it dominate your destiny."
encrypted_phrase = phrase1.upper()
encrypted_phrase = encrypted_phrase.replace('A','1')
encrypted_phrase = encrypted_phrase.replace('E','2')
encrypted_phrase = encrypted_phrase.replace('I','3')
encrypted_phrase = encrypted_phrase.replace('O','4')
encrypted_phrase = encrypted_phrase.replace('U','5')
print(encrypted_phrase)



#Task #3 (Re-Ordering a sentence)
print("\nTask #3")
piece1 = phrase1[:len(phrase1)//3]
piece2 = phrase1[len(phrase1)//3:(len(phrase1)//3)*2]
piece3 = phrase1[(len(phrase1)//3)*2:len(phrase1)]
print(piece2)
print(piece3)
print(piece1)



#Task #4 (Digit Sum)
print("\nTask #4")
number = input("Enter a 5 digit number:\t")
print(number[0],number[1],number[2],number[3],number[4]+f' = {(int(number[0])+int(number[1])+int(number[2])+int(number[3])+int(number[4]))}',sep='+')



#Task #5 (Some Weird Slicing)
print("\nTask #5")
phrase2 = "Why, you stuck-up half-witted scruffy-looking nerf herder."
print(phrase2[0:len(phrase2):2])
print(phrase2[len(phrase2):0:-2])



#Task #6 (Parsing out the date)
print("\nTask #5")
from datetime import date
today = date.today()
today = today.strftime("%Y,%B,%d")
print(f"The date today is {today}")
year = today[:today.find(',',0)]
month = today[today.find(',',4)+1:today.find(',',5)]
day = today[today.find(',',5)+1:]
print(f"Today is the {day} of {month}, {year}.")