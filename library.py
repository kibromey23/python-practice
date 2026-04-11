import random

#selecting a random element from a list
seq = ["apple", "banana", "cherry", "date", "elderberry"]
print(random.choice(seq))

#selecting a random integer from a range of numbers
number = random.randint(1, 10)
print(number)


#shuffling a list
cards = ["one", "Two", "Three", "Four", "Five"]
random.shuffle(cards)
for card in cards:
    print(card)
