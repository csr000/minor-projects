import re, pyperclip
a = re.compile(r'''(
   (\d{3}|\(\d{3}\))  (\s|-)  \d{3}  (\s|-)  \d{4} #Contact
   |
   \S+  @  \w+  \.  \w+ #Email
    )''', re.VERBOSE)
info=str(input('Welcome, Press Enter To Start:'))
info=pyperclip.paste()
b = a.findall(info)
match="Contact & Email"
print('Analyzing...')
for i in b:
    match += "|"+i[0]
match=match.split("|") 
match="\n".join(match)
pyperclip.copy(match)
print("Contacts and Email Successfully Extracted!(Copied To Clipboard)")
