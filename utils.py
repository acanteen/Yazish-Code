from datetime import datetime
from datetime import timedelta

# This will give details of the daf after days enterede


def find_date():
    try:
        while True:
            x = int(input("Type the days after which you want to renew :- "))
            y = datetime.now()
            z = y + timedelta(days=x)
            a = z.strftime("%D")
            b = z.strftime("%B")
            c = z.strftime("%A")
            e = z.strftime("%d")
            d = z.strftime("%Y")
            print(a)
            print("Month name= " + b)
            print("Day = " + c)
            print("Date = " + e)
            print("Year = " + d)
    except:
        print("I(COMPUTER) can understand integers(numbers) only! ")
