###projekt_2_Bulls&Cows.py: Druhý projekt - hra Bulls & Cows
###author: Eliška Matějková
###email: elinka.elis.111@gmail.com
###discord: eliskamatejkova_72569

import random

cow = 0
bull = 0
separator = "-" * 48
entries_number = 0

random_number = list()
while len(random_number) < 4:
    number = random.randint(0, 9)
    if number not in random_number:
        random_number.append(number)

if random_number[0] == 0:
    random_number.reverse()

random_number_list = list()
for number in random_number:
    random_number_list.append(str(number))

print("Hi there!")
print(separator)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print(separator)

def list_entered_number():
    entered_number = input("Enter a number:")
    print(separator)
    
    global entries_number
    if entered_number != 0:
        entries_number = entries_number + 1
        print(f"guess: {entries_number}")
    
    if entered_number.isnumeric() and len(entered_number) == 4:
        pass
    elif len(entered_number) < 4:
        print("The number has a little numbers! Stop")
        quit()
    else:
        print("The number doesn\'t have four numbers or not numeric.")
    
    global entered_number_list
    entered_number_list = list(f"{entered_number[0]}{entered_number[1]}{entered_number[2]}{entered_number[3]}")
    
    if len(entered_number_list) != len(set(entered_number_list)):
        print("The numbers mustn\'t be same.")
   
    if entered_number[0] == "0":
        print("0 mustn\'t be in the first place.")

def counting_bull(bull=0):
    if entered_number_list[0] == random_number_list[0]:
        bull = bull + 1
    if entered_number_list[1] == random_number_list[1]:
        bull = bull + 1
    if entered_number_list[2] == random_number_list[2]:
        bull = bull + 1
    if entered_number_list[3] == random_number_list[3]:
        bull = bull + 1
   
    if bull <= 1:
        print("bull: ", bull)
    else:
        print("bulls: ", bull)
    if bull == 4:
        print(f"Correct, you've guessed the right number in {entries_number} guesses!")
        print(separator)
        quit()

def counting_cow(cow=0):
    if entered_number_list[0] == random_number_list[1]:
        cow = cow + 1
    if entered_number_list[0] == random_number_list[2]:
        cow = cow + 1
    if entered_number_list[0] == random_number_list[3]:
        cow = cow + 1
    if entered_number_list[1] == random_number_list[0]:
        cow = cow + 1
    if entered_number_list[1] == random_number_list[2]:
        cow = cow + 1
    if entered_number_list[1] == random_number_list[3]:
        cow = cow + 1
    if entered_number_list[2] == random_number_list[0]:
        cow = cow + 1
    if entered_number_list[2] == random_number_list[1]:
        cow = cow + 1
    if entered_number_list[2] == random_number_list[3]:
        cow = cow + 1
    if entered_number_list[3] == random_number_list[0]:
        cow = cow + 1
    if entered_number_list[3] == random_number_list[1]:
        cow = cow + 1
    if entered_number_list[3] == random_number_list[2]:
        cow = cow + 1
  
    if cow <= 1:
        print("cow: ", cow)
    else:
        print("cows: ", cow)
    
    print(separator)

while bull < 4:
    list_entered_number()
    counting_bull()
    counting_cow()

