import random
spelaren = input("Vad är ditt namn?")
print(f"Välkommen till Colosseum! Du {spelaren} är en gladiator som ska strida en motståndare tills en dödas.")
motståndarna = ["Spartacus", "Flamma", "Priscus", "Spiculus", "Tetraites", "Commodus", "Marcus", "Aurelius", "Decimus", "Gaius", "Maximus", "Verus", "Crixus", "Carpophorus", "Antonius", "Augustus"]
motståndaren = random.choice(motståndarna)
attacker = ["näve", "spark"]
spelaren_hp = 10
motståndaren_hp = 8
def visa_hp():
    print(f"{spelaren} har just nu {spelaren_hp} hälsopoäng kvar.")
    print(f"{motståndaren} har just nu {motståndaren_hp} hälsopoäng kvar.")
print(f"Din motståndare är {motståndaren}")
strid = True

while strid == True:
    visa_hp()
    spelaren_attack = input("Hur attackerar du? (näve, spark)")
    motståndaren_attack = random.choice(attacker)
    if spelaren_attack == "näve":
        print(f"{spelaren} slår {motståndaren}.")
        motståndaren_hp -= 2
    if spelaren_attack == "spark":
        print(f"{spelaren} sparkar {motståndaren}.")
        motståndaren_hp -= 3
    if motståndaren_attack == "näve":
        print(f"{motståndaren} slår {spelaren}.")
        spelaren_hp -= 2
    if motståndaren_attack == "spark":
        print(f"{motståndaren} sparkar {spelaren}")
        spelaren_hp -= 3
    if spelaren_hp <= 0:
        print(f"{motståndaren} besegrar {spelaren}!")
        strid = False
    elif motståndaren_hp <= 0:
        print(f"{spelaren} besegrar {motståndaren}!")
        strid = False
    elif spelaren_hp <= 0 and motståndaren_hp <= 0:
        print(f"{spelaren} och {motståndaren} båda faller, det blir oavgjort!")
        strid = False