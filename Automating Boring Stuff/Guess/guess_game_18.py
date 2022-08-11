import random
secret_number = 3 #random.randint(0, 10)
users_guess = int(input("Take a guess: "))
guess_count = 0
try_again=users_guess

if users_guess == secret_number:
    print("congrat")
    

else:
    while guess_count < 4:
        if users_guess > secret_number:
            print("Guess is higher than the secret number")
        elif users_guess < secret_number:
            print("Guess is lower than the secret number")
        elif try_again > secret_number:
            print("Guess is higher than the secret number")
        elif try_again < secret_number:
            print("Guess is lower than the secret number")
        
        guess_count += 1
        guess_left = 5 - guess_count
        try_again = int(input("({}) Try again: ".format(str(guess_left) + " guess left")))
        if try_again == secret_number:
            print("congrats")
            break
    else:
        if guess_count == 4:
            print("You lose!")


# try_again = int(input("Try again ({}): ".format(str(guess_left) + " guesses left")))

















'''if users_guess == secret_number:
        print("congrats")
4
while users_guess < 4:      
    while guess_count < :
        guess_count += 1
        print(guess_count)
        try_again = int(input("Try again: "))
        while try_again == secret_number:
            print('congrat')
            break
    else:
        print("You lose")
        break'''

'''if users_guess == secret_number:
    print("congrats")

while users_guess != secret_number:
    guess_count += 1

    if guess_count < 4:
        try_again = int(input("Try Again: "))
        if try_again == secret_number:
            print('correct')
    else:
        print('You lose')
        break'''

'''if users_guess == secret_number:
    print("congrats")
else:
    while users_guess != secret_number:
        guess_count += 1
        try_again = int(input(str(guess_count) + "Try again: "))
        if guess_count < 3:
            if try_again == secret_number:
                print("correct!")
                break
        else:
            print("sorry, you lose")'''
        

'''while secret_number != users_guess:
    guess_count += 1
    try_again = int(input("Try Again: "))
    print(int(input("Try Again: ")))
    if try_again == secret_number:
        print('congrats')
        break
    if guess_count == 5:
        break
else:
    print("congrats!")'''

    