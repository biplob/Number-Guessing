import random


n = random.randrange(1, 10)
# input from user
guess = int(input("Enter Any Number: "))

# start loop from the below

while n != guess:
    if guess < n:
        print("Too Low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high")
        guess = int(input("Enter number again: "))
    else:
        break
print("You guessed it right!")