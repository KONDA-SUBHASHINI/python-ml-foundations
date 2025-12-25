import random

print("Guess the number between 1 to 1000 with clues")

random_value = random.randint(1, 1000)

print("You have 10 tries:")

i = 1
while i <= 10:
    n = int(input("Guess Number: "))

    if n == random_value:
        print(f"You guessed the number in {i} tries")
        break
    elif n > random_value:
        print("Lesser value than you said")
    else:
        print("Greater value than you said")

    print(f"You completed {i} tries. You have {10 - i} tries remaining.")
    i += 1

if i > 10:
    print("Game over! You used all your tries.")
    print(f"The correct number was {random_value}")
