import random 

 
options = ['rock', 'paper', 'scissors']

user_input = str(input("enter a move: "))
user_input = user_input.lower()

random_number = random.randint(0,2)
computer_pick = options[random_number]

if user_input not in options:
	print('\nWrong input, please try again.')
else: 

  print('\nYou picked '+ user_input + '.')
  print('Computer picked '+ computer_pick + '.')

  if user_input == 'rock' and computer_pick=='scissors' or user_input == 'paper' and computer_pick=='rock' or user_input == 'scissors' and computer_pick=='paper':
    print('\nYou won!')

  elif user_input == 'rock' and computer_pick=='rock' or user_input == 'scissors' and computer_pick=='scissors' or user_input == 'paper' and computer_pick=='paper' :
    print('\nIts a draw!')

  else:
    print('\nYou lost!')
    
    












  