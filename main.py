import random

number = random.randrange(1, 1000)
guess = int(input('guess the number between 1 and 1000 : '))
count = 0

while guess != number:
    count += 1
    if guess < number:
        guess = int(input('you need to guess higher. Try again! : '))
    else:
        guess = int(input('you need to guess lower. Try again! : '))

print(f'you guess the number correctly by {count} Times')



