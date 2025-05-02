import random
from random import choice

coin = choice(['heads', 'tails'])
print(coin) 

number = random.randint(1, 10)
print(number)


shuffle_list = [1, 2, 3, 4, 5]
random.shuffle(shuffle_list)
for num in shuffle_list:
    # The `print(num)` statement is printing each element in the `shuffle_list` after it has been
    # shuffled randomly using the `random.shuffle()` function. This will output the elements of the
    # list in a random order each time the code is run.
    print(num)