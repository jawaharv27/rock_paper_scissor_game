print(" *** \" ROCK PAPER SCISSOR GAME \" ***")
print()
import random
choices=('r','p','s')
emojis={'r':'🪨','p':'📃','s':'✂️'}
while True:
    user_choice=input("Rock(r)/Paper(p)/Scissor(s) ? \n Enter (r/p/s):").lower()
    computer_choice=random.choice(choices)
    if(user_choice not in choices):
        print(" INVALID INPUT! Try Again \n")
        continue
    print(f'You Chose {emojis[user_choice]}')
    print(f'computer Chose {emojis[computer_choice]}')
    if(computer_choice==user_choice):
        print(" TIE! \n")
    elif((user_choice=='r' and computer_choice=='s') or 
         (user_choice=='s' and computer_choice=='p') or 
         (user_choice=='p' and computer_choice=='r') ):
        print(" YOU WON!\n")
    else:    
        print(" YOU LOSE! \n ")
    wantto_continue=input('Once more? Enter(y/n):').lower()  
    print()
    if(wantto_continue=='n'):
        break

         

