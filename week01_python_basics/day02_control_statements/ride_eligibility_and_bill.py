height=int(input("What is youe height?"))
bill=0
if height>=3:
    print("You can ride")
    age=int(input("Enter your age:"))
    if age<12:
        bill+=150
    elif age<=18:
        bill+=250
    else:
        bill+=500
    want_photo=input("Do you want to take photo(y/n)?")
    if want_photo=='y' or want_photo=='Y':
        bill+=50
    print("Your total bill is ",bill)
else:
    print(You can't ride!")
