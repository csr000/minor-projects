import random, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.CRITICAL)
guess = ''

while guess not in ('heads', 'tails'):    
    print('Guess the coin toss! Enter heads or tails:')    
    guess = input() 
    
toss = random.randint(0, 1) # 0 is tails, 1 is heads 

if toss == 0:
    toss = 'tails'
elif toss == 1:
    toss = 'heads'
    
logging.debug('toss= '+ str(toss) + '|guess= ' + str(guess))

if toss == guess:    
    print('You got it!') 
else:    
    print('Nope! Guess again!')    
    guess = input()
    logging.debug('toss= '+ str(toss) + ' guess= ' + str(guess))    
    if toss == guess:        
        print('You got it!')    
    else:        
        print('Nope. You are really bad at this game.') 
    
