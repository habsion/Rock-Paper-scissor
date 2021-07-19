#Rock-Paper-scissor
from random import randint
t=('rock','paper','scissor')
user_name=input('Player name: ')
print('Enter input as rock/paper/scissor or stop to terminate the game')
while True:
    user=input('user: ').lower()
    if user not in t:
        print('Invalid input!!!!')
        continue
    if user=='stop':
        break
    com=randint(0,2)
    print('Computer:',t[com])
    if user==t[com]:
        print('Tie!!!!!')
    elif user==t[0]:
        print('Computer wins!!!!' if com==1 else user_name+' wins!!!!')
    elif user==t[1]:
        print('Computer wins!!!!' if com==2 else user_name+' wins!!!!')
    else:
        print('Computer wins!!!!' if com==0 else user_name+' wins!!!!')