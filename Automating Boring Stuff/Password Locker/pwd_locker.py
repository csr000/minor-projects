import random, pyperclip
print('Welcome Master')
count = 0
while True:
    master_pwd = input('Enter Master Password: ')
    if master_pwd != 'a':
        print('Access Denied!')
        count += 1
        if count == 3:
            print('No more try. Limit Reached!')
            break
    else: 
        print('Access Granted!')
        small = 'abcdefghijklmnopqrstuvwxyz'
        capital, numbers = small.upper(), '1234567890'
        char, count, c = list(small+capital+numbers), [], {}
        name = input('Enter name to generate password: ')
        #machine gen number
        while True:
            if name.isalnum():
                print("granted")
                while len(count) < 30:
                    count += char[random.randint(0, 61)]
                    if len(count) == 30:
                        pwd = ''.join(count)
                        print('('+str(name)+')' + ' => Password: ' + str(pwd))
                        pyperclip.copy(pwd)
                        print('Copied To Clipboard!')
                        break
                break
            else:
                if name.isalnum() != True:
                    name = input('Valid Characters Only(letters & numbers): ')
                    continue
        break

    
    

















'''
______plan_______
user has one master pwd-------
if user is authenticated:
    print access granted-------
    user types in name and machine gen the pwd
    and copy to clipboard
    and save 
    
    
    advance tings
    if user is authenticated:
        print access granted
        user types in name and machine gen the pwd (option to change pwd)
        option to (save and copy to clipboard)
        








'''