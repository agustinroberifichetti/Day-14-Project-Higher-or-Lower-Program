from random import choice
from replit import clear
from art import logo, vs
from game_data import data

print(logo)

def different_options(option_1, option_2, list_of_previous_choices):
  if option_1 == option_2 or option_2 in list_of_previous_choices :
    while option_1 == option_2 or option_2 in list_of_previous_choices :
      option_2 = choice(data)
  return option_2

def game():
  option_1 = choice(data)
  option_2 = choice(data)
  previous_choices = []
  option_2 = different_options(option_1, option_2, previous_choices)
  previous_choices = [option_1, option_2]
  current_score = 0
  game_end = False
  while not game_end:
    print(f"Compare: A -> {option_1['name']}, a {option_1['description']} from {option_1['country']}.")
    print(vs)
    print(f"\nAgainst: B -> {option_2['name']}, a {option_2['description']} from {option_2['country']}.")
    user_choice = input("\nWho has more followers on IG? Type 'A' or 'B' -> ").upper()
    while user_choice != "A" and user_choice != "B":
      user_choice = input("\nInvalid option entered. Please, type 'A' or 'B' -> ").upper()
    if user_choice == "A":
      if option_1['follower_count'] > option_2['follower_count']:
        clear()
        print(logo)
        current_score += 1
        print(f"You\'re right! Current score: {current_score}.\n")
        option_1 = option_2
        option_2 = different_options(option_1, option_2, previous_choices)
        previous_choices.append(option_2)
      else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {current_score}.")
        game_end = True
    if user_choice == "B":
      if option_2['follower_count'] > option_1['follower_count']:
        clear()
        print(logo)
        current_score += 1
        print(f"You\'re right! Current score: {current_score}.\n")
        option_1 = option_2
        option_2 = different_options(option_1, option_2, previous_choices)
        previous_choices.append(option_2)
      else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {current_score}.")
        game_end = True

  play_again = input("\nWant to play again? Type 'y' if so, or type 'n' if you don\'t -> ")
  if play_again == "y":
    clear()
    print(logo)
    game()
  else:
    print("\nHope you enjoyed it! See you soon!")
        
game()




  