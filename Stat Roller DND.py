import random
import time

num_die = input('How many die would you like to roll? ')

results = [] 
n = int(num_die)
print('Rolling the dice...')

for i in range(n): # rolls dice n times
    dice = random.randint(1,6)
    results.append(dice) #add each roll to result list


results.sort()
results.pop(0)
print("Your results with the lowest number taken out are: ", results)
    

