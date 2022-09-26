import random, time

input("Press Enter To Start")

init_min, init_secs=time.strftime('%M'), time.strftime('%S')

doc=['i','am','boy']

def words(phrase):
    '''Outputs unjoined version of the input'''
    words=[]
    for i in range(0,3):
        words+=(phrase[i])+' '
    words.pop()
    return words

main_phrase= ''.join(words(doc))
typed_phrase= input(main_phrase+'\n')

main=list(main_phrase)
typed=list(typed_phrase)

flags=0
try:
    for i in range(0,8):
        # print(main[i] == typed[i]) # print(main[i], typed[i])
        if main[i] != typed[i]:
            flags+=1
except IndexError:
    raise 'Not Accurate Enough'

print('flags = '+ str(flags))

final_min, final_secs=time.strftime('%M'), time.strftime('%S')

min=int(final_min)-int(init_min)
secs=int(final_secs)-int(init_secs)

print(f"Result: {min} minute(s), {secs} seconds")
#-------------------------------------------------------------------
