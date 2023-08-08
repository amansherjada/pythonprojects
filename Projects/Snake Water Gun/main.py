# Snake Water Gun Game by Aman.
import random


def get_player_choices():
  user_choice = input("Enter your choice (snake/water/gun): ").lower()
  while user_choice not in ["snake", "water", "gun"]:
    print("Invalid choice! Please choose from 'snake', 'water', or 'gun'.")
    user_choice = input("Enter your choice (snake/water/gun): ").lower()
  return user_choice


def winner(player, computer):
  if (player == computer):
    return (" It's a Draw")

  if (player == "Snake" and computer == "Water") or (
      player == "Water" and computer == "Gun") or (player == "Gun"
                                                   and computer == "Snake"):
    return ("You Win")
  else:
    return ("Computer Win")


print("Welcome to Snake Water Gun Game made by Aman")
choices = ["snake", "water", "gun"]
playerchoice = get_player_choices()
computerchoice = random.choice(choices)
print(f"Compter Choice is {computerchoice}")
result = winner(playerchoice, computerchoice)
print(result)
