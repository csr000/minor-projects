#Mille Made This
import random #module

class Main(object):
    def __init__(self):
        self.user_guess, self.main_guess=(input("Take Your First Guess: ")), 0
        self.guess_left=2 # This is two because self.user_guess already took one outta the 3 guess_left
        self.hint_engine_dice=random.randint(0, 1) # 1 takes the correct path, 0 takes the tricked path
        self.very_near_msg, self.far_msg="(hint) You're very near to the secret number", "(hint) You're far from the secret number"
        
    def main_execute(self):
        #print('self.main_guess '+str(self.main_guess)+' '+str(type(self.main_guess)), 'self.user_guess '+str(self.user_guess)+' '+str(type(self.user_guess)))
        self.user_guess=self.validate() # self.validate returns self.user_guess only if self.user_guess.isdigit()
        while self.user_guess!=self.main_guess:
            if self.guess_left!=0:
                self.guess_left-=1 #Decrement of number of chances

                # hint_engine_call
                self.execute_hint_engine()
                # Let's you take guess till number of chances has been exhausted
                self.guess_again()
                
            else:
                if self.hint_engine_dice!=1:
                    print('LOL, You exhausted all your chances.\nYou Lose! You Can Play Again to Discover the Secret Number.')
                    break
                else:
                    print('Limit Reached.\nYou Lose! Try Again Later')
                    break
        else:
            print("Yes, The Secret Number is: "+str(self.main_guess))
            print("NO WAY YOU GOT THAT RIGHT! YOU'RE A GENIUS!" if self.hint_engine_dice!=1 else "CONGRATULATIONS, YOU WON!")
    
    # validation of characters
    def validate(self):
        #print('self.user_guess '+str(self.user_guess)+' '+str(type(self.user_guess)))
        while not self.user_guess.isdigit():
            print('Enter A Valid Number')
            self.user_guess=input("Take a Guess: ")
            #print('user_guess'+str(user_guess)+str(type(user_guess)))
        return int(self.user_guess) if self.user_guess.isdigit() else None

    # Paths
    #-------------------------------------------------------------------------------------------------------------
    def correct_path(self):
        if self.guess_left!=0:
            if abs((self.user_guess-self.main_guess))==2 or abs((self.user_guess-self.main_guess))==1:
                print(self.very_near_msg)
            elif abs((self.main_guess-self.user_guess))>=2 or abs((self.user_guess-self.main_guess))>=2:
                print(self.far_msg)
        else:
            print("Come On! You were giving a Good Hint. You got this!")   
            
    def tricked_path(self):
        if self.guess_left!=0:
            if abs((self.user_guess-self.main_guess))==2 or abs((self.user_guess-self.main_guess))==1:
                print(self.far_msg)
            elif abs((self.main_guess-self.user_guess))>=2 or abs((self.user_guess-self.main_guess))>=2:
                print(self.very_near_msg)                 
        elif self.hint_engine_dice==0: 
            print('You Played Yourself. The Hint was FAKE!\nNow Let See How You Are Going To Win.') 
    #-------------------------------------------------------------------------------------------------------------

    # Main Hint Engine Execution
    def execute_hint_engine(self):
        self.correct_path() if self.hint_engine_dice==1 else self.tricked_path()
            
    # Basically Let's user guess again till guess_left has been exhausted
    def guess_again(self):
        if self.guess_left==1:
            self.user_guess=input('('+str(self.guess_left)+' chance left)'+" Take Another Guess: ")
            self.user_guess=self.validate()
        elif self.guess_left==0:
            self.user_guess=input('('+str(self.guess_left)+' chance left)'+" Your Last Chance: ")
            self.user_guess=self.validate()

Main().main_execute()

'''
import time

t1=time.time()

for e in range(100):
    

t2=time.time()
t3=t2-t1

print('time: '+str(t3))'''

'''

#TEST
import random #module

class Main(object):
    def __init__(self):
        self.user_guess, self.main_guess=str(0), random.randint(0, 10)
        self.guess_left=2 # This is two because self.user_guess already took one outta the 3 guess_left
        self.hint_engine_dice=random.randint(0, 1) # 1 takes the correct path, 0 takes the tricked path
        self.very_near_msg, self.far_msg="(hint) You're very near to the secret number", "(hint) You're far from the secret number"
        
    def main_execute(self):
        #print('self.main_guess '+str(self.main_guess)+' '+str(type(self.main_guess)), 'self.user_guess '+str(self.user_guess)+' '+str(type(self.user_guess)))
        self.user_guess=self.validate() # self.validate returns self.user_guess only if self.user_guess.isdigit()
        while self.user_guess!=self.main_guess:
            if self.guess_left!=0:
                self.guess_left-=1

                # hint_engine_call
                self.execute_hint_engine()
                # Let's you take guess till number of chances has been exhausted
                self.guess_again()
                
            else:
                if self.hint_engine_dice!=1:
                    self.tricked_conclusion_for_losers()
                    break
                else:
                    self.correct_conclusion_for_losers()
                    break
        else:
            self.conclusion_for_winners()
    
    # validation of characters
    def validate(self):
        #print('self.user_guess '+str(self.user_guess)+' '+str(type(self.user_guess)))
        while self.user_guess.isdigit()!=True:
            print('Enter A Valid Number')
            self.user_guess=str(0)
        if self.user_guess.isdigit()==True:
            user_guess=int(self.user_guess)
            #print('user_guess'+str(user_guess)+str(type(user_guess)))
            return user_guess
    
    # hint_engine
    def correct_path(self):
        if self.guess_left!=0:
            if self.main_guess<self.user_guess:
                if (self.user_guess-self.main_guess)==2 or (self.user_guess-self.main_guess)==1:
                    print(self.very_near_msg)
                elif (self.main_guess-self.user_guess)>=2 or (self.user_guess-self.main_guess)>=2:
                    print(self.far_msg)
            elif self.user_guess<self.main_guess:
                if (self.main_guess-self.user_guess)==2 or (self.main_guess-self.user_guess)==1:
                    print(self.very_near_msg)
                elif (self.main_guess-self.user_guess)>=2 or (self.user_guess-self.main_guess)>=2:
                    print(self.far_msg)
        else:
            print("Come On! You were giving a Good Hint. You got this!")   
            
    def tricked_path(self):
        if self.guess_left!=0:
            if self.main_guess<self.user_guess:
                if (self.user_guess-self.main_guess)==2 or (self.user_guess-self.main_guess)==1:
                    print(self.far_msg)
                elif (self.main_guess-self.user_guess)>=2 or (self.user_guess-self.main_guess)>=2:
                    print(self.very_near_msg)
            elif self.user_guess<self.main_guess:
                if (self.main_guess-self.user_guess)==2 or (self.main_guess-self.user_guess)==1:
                    print(self.far_msg)
                elif (self.main_guess-self.user_guess)>=2 or (self.user_guess-self.main_guess)>=2:
                    print(self.very_near_msg)                  
        else:
            if self.hint_engine_dice==0: # if guess_left has been exhausted
                print('You Played Yourself. The Hint was FAKE!') 
                print("Now Let See How You Are Going To Win.")
    
    # Main Hint Engine Execution
    def execute_hint_engine(self):
        # hint_engine_exection
        if self.hint_engine_dice==1:
            self.correct_path()
        else:
            self.tricked_path()
            
    # Basically Let's user guess again till guess_left has been exhausted
    def guess_again(self):
        if self.guess_left==1:
            self.user_guess=str(0)
            self.user_guess=self.validate()
        elif self.guess_left==0:
            self.user_guess=str(0)
            self.user_guess=self.validate()
    
    # Conclusions
    @staticmethod
    def tricked_conclusion_for_losers():
        print('LOL, You exhausted all your chances.')
        print('You Lose! You Can Play Again to Discover the Secret Number.')
    
    @staticmethod
    def correct_conclusion_for_losers():
        print('Limit Reached.')
        print('You Lose! Try Again Later')
    
    def conclusion_for_winners(self):
            print("Yes, The Secret Number is: "+str(self.main_guess))
            if self.hint_engine_dice!=1:
                print("NO WAY YOU GOT THAT RIGHT! YOU'RE A GENIUS!")
            else:
                print("CONGRATULATIONS, YOU WON!")


import time

t1=time.time()

for e in range(100):
    Main().main_execute()

t2=time.time()
t3=t2-t1

print('time: '+str(t3))



# ORIGINAL

import random #module

class Main(object):
    def __init__(self):
        self.user_guess, self.main_guess=(input("Take Your First Guess: ")), random.randint(0, 10)
        self.guess_left=2 # This is two because self.user_guess already took one outta the 3 guess_left
        self.hint_engine_dice=random.randint(0, 1) # 1 takes the correct path, 0 takes the tricked path
        self.very_near_msg, self.far_msg="(hint) You're very near to the secret number", "(hint) You're far from the secret number"
        
    def main_execute(self):
        #print('self.main_guess '+str(self.main_guess)+' '+str(type(self.main_guess)), 'self.user_guess '+str(self.user_guess)+' '+str(type(self.user_guess)))
        self.user_guess=self.validate() # self.validate returns self.user_guess only if self.user_guess.isdigit()
        while self.user_guess!=self.main_guess:
            if self.guess_left!=0:
                self.guess_left-=1

                # hint_engine_call
                self.execute_hint_engine()
                # Let's you take guess till number of chances has been exhausted
                self.guess_again()
                
            else:
                if self.hint_engine_dice!=1:
                    self.tricked_conclusion_for_losers()
                    break
                else:
                    print('Limit Reached.\nYou Lose! Try Again Later')
                    break
        else:
            self.conclusion_for_winners()
    
    # validation of characters
    def validate(self):
        #print('self.user_guess '+str(self.user_guess)+' '+str(type(self.user_guess)))
        while self.user_guess.isdigit()!=True:
            print('Enter A Valid Number')
            self.user_guess=input("Take Your First Guess: ")
        if self.user_guess.isdigit()==True:
            user_guess=int(self.user_guess)
            #print('user_guess'+str(user_guess)+str(type(user_guess)))
            return user_guess
    
    # hint_engine
    def correct_path(self):
        if self.guess_left!=0:
            if self.main_guess<self.user_guess:
                if (self.user_guess-self.main_guess)==2 or (self.user_guess-self.main_guess)==1:
                    print(self.very_near_msg)
                elif (self.main_guess-self.user_guess)>=2 or (self.user_guess-self.main_guess)>=2:
                    print(self.far_msg)
            elif self.user_guess<self.main_guess:
                if (self.main_guess-self.user_guess)==2 or (self.main_guess-self.user_guess)==1:
                    print(self.very_near_msg)
                elif (self.main_guess-self.user_guess)>=2 or (self.user_guess-self.main_guess)>=2:
                    print(self.far_msg)
        else:
            print("Come On! You were giving a Good Hint. You got this!")   
            
    def tricked_path(self):
        if self.guess_left!=0:
            if self.main_guess<self.user_guess:
                if (self.user_guess-self.main_guess)==2 or (self.user_guess-self.main_guess)==1:
                    print(self.far_msg)
                elif (self.main_guess-self.user_guess)>=2 or (self.user_guess-self.main_guess)>=2:
                    print(self.very_near_msg)
            elif self.user_guess<self.main_guess:
                if (self.main_guess-self.user_guess)==2 or (self.main_guess-self.user_guess)==1:
                    print(self.far_msg)
                elif (self.main_guess-self.user_guess)>=2 or (self.user_guess-self.main_guess)>=2:
                    print(self.very_near_msg)                  
        else:
            if self.hint_engine_dice==0: # if guess_left has been exhausted
                print('You Played Yourself. The Hint was FAKE!') 
                print("Now Let See How You Are Going To Win.")
    
    # Main Hint Engine Execution
    def execute_hint_engine(self):
        # hint_engine_exection
        if self.hint_engine_dice==1:
            self.correct_path()
        else:
            self.tricked_path()
            
    # Basically Let's user guess again till guess_left has been exhausted
    def guess_again(self):
        if self.guess_left==1:
            self.user_guess=input('('+str(self.guess_left)+' chance left)'+" Take Another Guess: ")
            self.user_guess=self.validate()
        elif self.guess_left==0:
            self.user_guess=input('('+str(self.guess_left)+' chance left)'+" Your Last Chance: ")
            self.user_guess=self.validate()
    
    # Conclusions
    @staticmethod
    def tricked_conclusion_for_losers():
        print('LOL, You exhausted all your chances.')
        print('You Lose! You Can Play Again to Discover the Secret Number.')
    
    @staticmethod
    def correct_conclusion_for_losers():
        print('Limit Reached.')
        print('You Lose! Try Again Later')
    
    def conclusion_for_winners(self):
            print("Yes, The Secret Number is: "+str(self.main_guess))
            if self.hint_engine_dice!=1:
                print("NO WAY YOU GOT THAT RIGHT! YOU'RE A GENIUS!")
            else:
                print("CONGRATULATIONS, YOU WON!")


Main().main_execute()









'''