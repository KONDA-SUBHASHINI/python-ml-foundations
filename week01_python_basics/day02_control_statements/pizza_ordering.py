size=input("What size pizza you want(S/M/L)? ")
bill=0

if size=='s' or size=='S':
    print("Small Pizza price is 100 Rs.")
    bill+=100
elif size=='m' or size=='M':
    print("Medium Pizza price is 200 Rs.")
    bill+=200
elif size=='l' or size=='L':
    print("Large Pizza price is 300 Rs.")
    bill+=300
    
want_peperoni=input("Do you want peperoni(T/F)? ")
if want_peperoni=='y' or want_peperoni=='Y':
    if size=='s' or size=='S':
        bill+=30
    else:
        bill+=50
        
want_cheese=input("Do you want cheese(T/F)? ")
if want_cheese=='y' or want_cheese=='Y':
    bill+=20

print("your final bill is ",bill)
print("Thank You!")
