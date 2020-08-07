import random
import math
user_name = input('Enter your name: ')
print('Hello, {}'.format(user_name))
rating_file = open('rating.txt', 'r')
scores_by_name = {}
for line in rating_file:
    line = line.split()
    name = line[0]
    score = int(line[1])
    if name == user_name:
        scores_by_name[user_name] = score
    else:
        scores_by_name[user_name] = 0
options = input('').split()
options = [option for option in options]
if len(options) < 1:
    options = ['paper', 'rock', 'scissors']
print("Okay, let's start")
while True:
    user_move = input('')
    if user_move == '!exit':
        print('Bye!')
        break
    elif user_move == '!rating':
        print('Your rating: ', scores_by_name[user_name])
    else:
        if user_move in options:
            comp_move = random.choice(options)
            if user_move == comp_move:
                scores_by_name[user_name] += 50
                print('There is a draw ({})'.format(comp_move))
            else:
                user_move_index = options.index(user_move)
                all = options[user_move_index+1:]
                preceding = options[:user_move_index]
                all.extend(preceding)
                mid_index = math.trunc(len(all) / 2)
                first_half = all[:mid_index]
                second_half = all[mid_index:]
                if comp_move in first_half:
                    scores_by_name[user_name] += 100
                    print('Well done. Computer chose {} and failed'.format(comp_move))
                elif comp_move in second_half:
                    print('Sorry, but computer chose {}'.format(comp_move))
        else:
            print('Invalid input')
    rating_file.close()
