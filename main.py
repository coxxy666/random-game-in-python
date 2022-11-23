
import random

# Split string method
names_string = input("ENTER")
names = names_string.split(", ")

names_len = len(names)

names_random = random.randint(0,names_len-1)

random_result = names[names_random]

print(random_result + " is going to buy the meal today!")