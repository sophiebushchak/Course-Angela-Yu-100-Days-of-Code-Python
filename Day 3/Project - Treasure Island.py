print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
question_1 = input(
    "You arrive on the island. A forest is on the left and to the right is a rocky path. Do you go left or right?\n"
).lower()

if question_1 == "left":
    question_2 = input(
        "\nYou come across a lake deep in the forest. Do you try to 'swim' across or do you 'wait' for a boat?\n"
    ).lower()
    if question_2 == "swim":
        print("You are attacked by a giant trout. Game over.")
    else:
        question_3 = input(
            "\nYou come across a blue, red and yellow door. Which colour door do you pick?\n"
        ).lower()
        if question_3 == "yellow":
            print("You win!")
        elif question_3 == "red":
            print("You enter a fiery room. You are unable to escape and burn to death. Game over.")
        elif question_3 == "blue":
            print("You enter a room full of beasts. They rip you to shreds. Game over.")
        else:
            print("Game over.")
else:
    print("A giant buzzard attacks you and you die. Game over.")
