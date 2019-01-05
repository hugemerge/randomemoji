import json
import random

# load emoji list
with open('emojis_picked.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
emojis = data["emojis"]

# choose emoji
def choose(l):
    return random.choice(emojis)

# return emoji
print(choose(emojis))