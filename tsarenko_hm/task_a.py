import random

number = int(input ("Please enter a number:"))

random.number = int(random.randint(0,number))

print("The random number from 0 to", number, "is", random.number)

print("Here are", random.number, "numbers from range 0 to", number, ":", random.sample(range(number), random.number))






