import random

first = ["the ", "a ", "another "]
obj = ["cat ", "dog ", "man ", "woman "]
verb = ["sang ", "ran ", "jumped "]
adv = ["loudly ", "quietly ", "well ", "badly "]

i = 5
while i > 0:
    print(random.choice(first) + random.choice(obj) + random.choice(verb) + random.choice(adv))
    i -= 1
