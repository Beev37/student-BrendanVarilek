gnrl_traits = ["Name:", "Birthday:", "Hobbies:", "Favorite Book:", "Favorite Movie"]
brendan = ["Brendan Varilek", "August 9th 1995", "Cooking, Making Music, and Playing Games", "Neuromancer", "The Lord of the Rings Trilogy"]

prsn_traits = {}
ppl_traits = {}

for x in gnrl_traits:
    prsn_traits[x] = brendan[gnrl_traits.index(x)]

#print(prsn_traits)

for pair in prsn_traits.items():
    print(pair)