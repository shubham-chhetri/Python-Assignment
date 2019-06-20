# Python-Assignment
Just started learning python. May be complete or incomplete projects.
#basic program of finding leap year

x=int(input("Enter a year"))
if x%100==0:
    if x%400==0:
        print("leap year")
    else :
            print("Not a leap year")
elif x%4==0:
        print("leap year")
else:
        print("Not a leap year")
