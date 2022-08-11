import random
user = ''
while len(user)<1:
    try:
        user = input('Enter Username: ')
    except Exception as e:
        print(e)
    if len(user)>1:
        def pin():
            return int(random.randint(0, 9))
        # pins
        pin1, pin2, pin3, pin4 = pin(), pin(), pin(), pin()
        pin = "{}{}{}{}".format(pin1, pin2, pin3, pin4)
        # writing files
        file = open("users.txt", "a")
        file.write("(user = {}, pin = {})\n".format(user, pin))
        file.close()
        print("Your pin is: {}{}{}{}".format(pin1, pin2, pin3, pin4))
        break