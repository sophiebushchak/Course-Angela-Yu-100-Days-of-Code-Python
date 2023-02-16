import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
choices = [
    "Rock",
    "Paper",
    "Scissors"
]
visualization = [
    rock,
    paper,
    scissors
]
chosen = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))

computer_chosen = random.randint(0, 2)

print(f"\nYou chose {choices[chosen]}:\n{visualization[chosen]}")
print(f"Opponent chose {choices[computer_chosen]}:\n{visualization[computer_chosen]}")

if chosen == 0:
    if computer_chosen == 0:
        print("Draw")
    elif computer_chosen == 1:
        print("You lose.")
    else:
        print("You win!")
elif chosen == 1:
    if computer_chosen == 0:
        print("You win!")
    elif computer_chosen == 1:
        print("Draw")
    else:
        print("You lose.")
else:
    if computer_chosen == 0:
        print("You lose.")
    elif computer_chosen == 1:
        print("You win!")
    else:
        print("Draw")



