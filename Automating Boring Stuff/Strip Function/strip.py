import re

def stripper(string):
    regex=re.compile(r'\w+.+\w+')
    matches=regex.search(str(string))
    print(matches)


stripper('  strips first   whitespace  skkrr  aih  ')