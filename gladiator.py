import random
namn = input("Vad är ditt namn?")
print(f"Välkommen till Colosseum! Du {namn} är en gladiator som ska strida en motståndare tills en dödas.")
motståndarna = ["Spartacus", "Flamma", "Priscus", "Spiculus", "Tetraites", "Commodus", "Marcus", "Aurelius", "Decimus", "Gaius", "Maximus", "Verus", "Crixus", "Carpophorus", "Antonius", "Augustus"]
motståndaren = random.choice(motståndarna)
attacker = ["näve", "spark"]
spelaren_hp = 10
fienden_hp = 8
strid = True