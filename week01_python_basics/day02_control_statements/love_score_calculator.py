name=input("what is you name? ")
friend_name=input("What is your friend name? ")
both_names=name+friend_name
lower_string=both_names.lower()
t=lower_string.count('t')
r=lower_string.count('r')
u=lower_string.count('u')
e=lower_string.count('e')
true=t+r+u+e
l=lower_string.count('l')
o=lower_string.count('o')
v=lower_string.count('v')
e=lower_string.count('e')
love=l+o+v+e
love_score=int(str(true)+str(love))
if love_score<10 or love_score>90:
   print(f"Your love score is {lovescore}% and you go together like ice and water")
elif love_score>=40 and love_score<=50:
    print(f"Your love score is {lovescore}% and you go alright together.")
else:
    print(f"Your love score is {love_score}%")
