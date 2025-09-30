#Locke Hemphill
#9/29/25
#Pd 8

import os
os.system("cls")



#Task #1 (Text Formatting)
full_name = input("What is your first and last name?\t")

#seperating first and last name
first_name = full_name[:full_name.find(" ",0)]
last_name = full_name[full_name.find(" ",0)+1:]

#printing First-name, Last-name
print(first_name.title()+", "+last_name.title())
#printing fIRST-NAME, lAST-NAME
print(first_name[0].lower()+first_name[1:].upper()+", "+last_name[0].lower()+last_name[1:].upper())



#Task #2 (Simple Encryption)
phrase1 = "Once you start down the dark path, forever will it dominate your destiny."
encrypted_phrase = phrase1.upper()
encrypted_phrase = encrypted_phrase.replace('A','1')
encrypted_phrase = encrypted_phrase.replace('E','2')
encrypted_phrase = encrypted_phrase.replace('I','3')
encrypted_phrase = encrypted_phrase.replace('O','4')
encrypted_phrase = encrypted_phrase.replace('U','5')
print(encrypted_phrase)
encrypted_phrase = encrypted_phrase.replace(' ', '*')
piece1 = encrypted_phrase[:len(encrypted_phrase)//3]
piece2 = encrypted_phrase[len(encrypted_phrase)//3:(len(encrypted_phrase)//3)*2]
piece3 = encrypted_phrase[(len(encrypted_phrase)//3)*2:len(encrypted_phrase)]
print(piece2)
print(piece3)
print(piece1)



#Task #3 (Digit Sum)
number = input("Enter a 5 digit number:\t")
print(number[0],number[1],number[2],number[3],number[4]+' = '+(int(number[0])+int(number[1])+int(number[2])+int(number[3])+int(number[4])),sep='+')



#Task #4 (Some Weird Slicing)
phrase2 = "Why, you stuck-up half-witted scruffy-looking nerf herder."