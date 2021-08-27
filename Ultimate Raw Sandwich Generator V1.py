import random
import textwrap

exclamation = ["Oh man...", "Great...", "Alrighty then!", "Geepers...", "Uh, okay.", "Buuuuuuuuuurp!", "Look Morty." "Oh boy, I'm hungry!", "I could really go for a sandwich."]
bravery = ["I guess I'll try a", "I bet I'd like a", "I'm gonna try a", "Here goes nothing: a", "My ultimate hoagie? A", "Whenever I can, I make a", "What's breakfast without a", "For good luck, try a"]
stuffOnBread = ['peanut butter', 'french fry', 'frikandel', 'cement', 'recyclable vegan shopping bag', 'microplastics', 'asbestos', 'printer ink', 'toothpaste', 'orange juice', 'sandwich', 'dog food', 'whale blubber', 'banana', 'chocolate', 'ham', 'mayo', 'sprinkles', 'lemon wedge', 'salami', 'cheese', 'carrot', 'coleslaw', 'chicken', 'jam', 'jelly', 'jello', 'whipped cream', 'pineapple chunks', 'peanut', '[UNDEFINED]', 'gritty paste', 'ice cream', 'ranch dressing', 'cream of corn', 'fresh lettuce', 'limp carrot', 'watermelon', 'bronzer', 'pencil shavings', 'wilted cabbage', 'hazelnut spread', 'fried banana', 'moist napkin', 'ketchup', 'aioli', 'sand', 'razor blade', 'strawberry']
typeOfBread = ['whole grain', 'brown bread', 'papier-mâché', 'multi grain', 'tiger white', 'cornbread', 'leftover pizza', '[EDIBLE BREAD]', 'crackers', 'shingles', 'vanilla wafers', 'lasagna', 'pancakes', 'waffles', 'sourdough', 'rice cakes', 'asbestos', 'rice paper', 'lemon poppy cake', 'pizza', 'biscuits', 'pie', 'cheese']
stateOfBread = ['fresh', 'mouldy', 'slightly stale', 'crispy', '[ADJECTIVE]', 'passionately burnt', 'toasted', 'dry', 'sad', 'tear-stained', 'yellowed', 'sundried', 'Pickle Rick(tm) branded', 'excessive amounts of', 'disappointing', 'very fresh', 'absolutely amazing', 'oddly salty', 'dubious quality', 'slightly blue', 'deep fried', 'battered and deep fried', 'twice baked', 'burnt and raw', 'soft and fluffy', 'very healthy', 'gluten free']
tasteOfBread = ['tasty', 'kind of weird', 'nice', 'amazing', 'yummy', 'just scrumptious', 'absolutely abhorrent', 'a hard pass next time', 'a once in a lifetime experience', 'completely inedible', 'mostly edible', 'kind of disappointing', 'uhh... very special, thanks', 'not my kind of sandwich', 'gonna make me cry']


def generateSandwich():
    randomStuff1 = random.choice(stuffOnBread)
    randomStuff2 = random.choice(stuffOnBread)
    randomStuff3 = random.choice(stuffOnBread)
    randomType = random.choice(typeOfBread)
    randomState = random.choice(stateOfBread)
    randomTaste = random.choice(tasteOfBread)
    randomExclamation = random.choice(exclamation)
    randomBravery = random.choice(bravery)
    breadSuggestion = textwrap.fill(randomExclamation + " " + randomBravery + " " + randomStuff1 + ", " + randomStuff2 + " and " + randomStuff3 + " sandwich on " + randomState + " " + randomType + ". I think it's " + randomTaste + "!")
    print(breadSuggestion)

generateSandwich()
