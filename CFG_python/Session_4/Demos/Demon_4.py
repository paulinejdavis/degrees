import random

verbs = ["run", "jump", "eat", "sleep"]
nouns = ["dog", "man", "girl", "cat"]

random_verb = random.choice(verbs)
random_noun = random.choice(nouns)

random_sentence = "The " + random_noun + " " + random_verb + "s. "
print(random_sentence)