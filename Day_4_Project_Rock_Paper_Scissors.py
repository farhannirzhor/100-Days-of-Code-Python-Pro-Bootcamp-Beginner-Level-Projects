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

games = [rock, paper, scissors]

user_choice = int(input("What would you like to choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

# Check for invalid input before using it
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(games[user_choice])
    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{games[computer_choice]}")

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")  
    elif user_choice > computer_choice:
        print("You win!")
    else:
        print("It's a draw!")
print("Thank you for playing Rock, Paper, Scissors!") 