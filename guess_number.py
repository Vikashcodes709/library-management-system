import random
number = random.randint(1, 10)

guess = int(input("Guess a number(1 to 10): "))

if guess == number:
    print("Congratulation! You guessed correctly. ")
else:
    print("Wrong Guess!")
    print("Correct Number was:", number)