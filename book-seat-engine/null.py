import datetime

while True:
    if str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")) == '2020-09-06 23:15':
        break
    print(str(datetime.datetime.now()))