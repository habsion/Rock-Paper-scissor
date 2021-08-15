#Rock-Paper-scissor
from random import randint


t=('rock','paper','scissor')               # sample space
user_name=input('Player name: ')
print('Enter input as rock/paper/scissor or stop to terminate the game')
while True:                                # run the loop until the player gives input as "stop"
    user=input('user: ').lower()
    if user=='stop':
        print('Game terminated!')
        break
    if user not in t:                      # if the user gives an input outside of sample space then stop the current iteration and move to the next iteration
        print('Invalid input!!!!')
        continue
    com=randint(0,2)                       # generate a random int from 0 to 2 which acts as a index and that index gives our bot it's pick from the sample space
    print('Computer:',t[com])
    
    # Bunch of if statements to determine the winner
    if user==t[com]:
        print('Tie!!!!!')
    elif user==t[0]:
        print('Computer wins!!!!' if com==1 else user_name+' wins!!!!')
    elif user==t[1]:
        print('Computer wins!!!!' if com==2 else user_name+' wins!!!!')
    else:
        print('Computer wins!!!!' if com==0 else user_name+' wins!!!!')
