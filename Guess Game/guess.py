#Mille Made This
import random #module

#hint_engine_function
def hint_engine():
    # hint_engine
    very_near_msg="(hint) You're very near to the secret number"
    far_msg="(hint) You're far from the secret number"
    if hint_engine_dice==1:
        if guess_left!=0:
            #print(str((main_guess-user_guess))+'or'+str((user_guess-main_guess)))
            if main_guess<user_guess:
                if (user_guess-main_guess)==2 or (user_guess-main_guess)==1:
                    print(very_near_msg)
                elif (main_guess-user_guess)>=2 or (user_guess-main_guess)>=2:
                    print(far_msg)
            elif user_guess<main_guess:
                if (main_guess-user_guess)==2 or (main_guess-user_guess)==1:
                    print(very_near_msg)
                elif (main_guess-user_guess)>=2 or (user_guess-main_guess)>=2:
                    print(far_msg)
        else:
            print("Come On! You were giving a Hint. You got this!") 
    else:
        if guess_left!=0:
            if main_guess<user_guess:
                if (user_guess-main_guess)==2 or (user_guess-main_guess)==1:
                    print(far_msg)
                elif (main_guess-user_guess)>=2 or (user_guess-main_guess)>=2:
                    print(very_near_msg)
            elif user_guess<main_guess:
                if (main_guess-user_guess)==2 or (main_guess-user_guess)==1:
                    print(far_msg)
                elif (main_guess-user_guess)>=2 or (user_guess-main_guess)>=2:
                    print(very_near_msg)                  
        else:
            if hint_engine_dice==0:
                print('You Played Yourself. The Hint was FAKE!') 
                print("Now Let See How You Are Going To Win.")

#variables
user_guess, main_guess, guess_left, hint_engine_dice=input("Take Your First Guess: "), random.randint(0, 10), 2, random.randint(0, 1)
# guess_left is 2 because the user guess already took the first guess(chance), so by subtraction of 1, the guesses left out of 3 will be 2




#Exception handling for allowed characters
def character_check(user_guess):
    while user_guess.isdigit()!=True:
        #print('self.user_guess'+self.user_guess)
        print('Enter A Valid Number')
        user_guess=input("Take Your First Guess: ")
    if user_guess.isdigit()==True:
        user_guess=int(user_guess)
        #print('user_guess'+str(user_guess)+str(type(user_guess)))
        return user_guess

user_guess=character_check(user_guess)

#Program actually starts here
while user_guess!=main_guess:
    #print(str(guess_left)+' (1)')
    if guess_left!=0:
        #print(str(guess_left)+' (2)')
        guess_left-=1

        #hint_engine_call
        hint_engine()
  
        if guess_left==1:
            user_guess=input('('+str(guess_left)+' chance left)'+" Take Another Guess: ")
            user_guess=character_check(user_guess)
        elif guess_left==0:
            user_guess=input('('+str(guess_left)+' chance left)'+" Your Last Chance: ")
            user_guess=character_check(user_guess)
        
    else:
        if hint_engine_dice!=1:
            print('LOL, You exhausted all your chances.')
            print('You Lose! You Can Play Again to Discover the Secret Number.')
            break
        else:
            print('Limit Reached.')
            print('You Lose! Try Again Later')
            break
else:
    print("Yes, The Secret Number is: "+str(main_guess))
    if hint_engine_dice!=1:
        print("NO WAY YOU GOT THAT RIGHT! YOU'RE A GENIUS!")
    else:
        print("CONGRATULATIONS, YOU WON!")