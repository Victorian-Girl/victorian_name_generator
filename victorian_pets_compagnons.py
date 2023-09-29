import random

pets_mapping = [
    "cat",
    "dog",
    "parrot",
    "rabbit",
    "hamster",
    "mouse",
    "fish",
    "snake",
    "lizard",
    "turtle",
    "frog",
    "spider",
    "scorpion",
    "guinea pig",
    "chinchilla",
    "gerbil",
    "rat",
    "squirrel",
    "pig",
    "lambs",
    "lemur",
    "mungoose",
    "stag-beetle",
    "donkey",
    "horse",
    "ferret"
]


names = [f"{v}" for v in pets_mapping]
random.shuffle(names)
r_names = names[:1]

result = r_names
# print(r_names)