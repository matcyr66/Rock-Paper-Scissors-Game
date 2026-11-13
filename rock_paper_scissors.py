import random

def cont():
    input("Press Enter for CPU's turn...")

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
my_list = [rock, paper, scissors]

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n").strip().lower()

while user_choice not in ["0", "1", "2"]:
    print("Your input is invalid. Please try again.")
    user_choice = input("Choose 0 for Rock, 1 for Paper or 2 for Scissors.\n")

user_choice = int(user_choice)
print(my_list[user_choice])

cont()

print("Computer chose:")
pc_choice = random.choice([0, 1, 2])
print(my_list[pc_choice])

if (user_choice == 0 and pc_choice == 2) or \
   (user_choice == 1 and pc_choice == 0) or \
   (user_choice == 2 and pc_choice == 1):
    print("You win!")
elif (pc_choice == 0 and user_choice == 2) or \
     (pc_choice == 1 and user_choice == 0) or \
     (pc_choice == 2 and user_choice == 1):
    print("You lose!")
elif user_choice == pc_choice:
    print("It's a draw!")