import random
import time
def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()
slow_print("Välkommen till Colosseum! Du är en gladiator som ska strida en motståndare tills en dödas.")
slow_print("Vad är ditt namn ung krigare? ")
spelaren = input()
motståndarna = ["Spartacus", "Flamma", "Priscus", "Spiculus", "Tetraites", "Commodus", "Marcus", "Aurelius", "Decimus", "Gaius", "Maximus", "Verus", "Crixus", "Carpophorus", "Antonius", "Augustus"]
motståndaren = random.choice(motståndarna)
attacker = ["näve", "spark", "svärd"]
chans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
spelaren_hp = 20
motståndaren_hp = 20
runda = 1
def visa_hp():
    slow_print(f"{spelaren} har just nu {spelaren_hp} hälsopoäng kvar.")
    slow_print(f"{motståndaren} har just nu {motståndaren_hp} hälsopoäng kvar.")
slow_print(f"Din motståndare är {motståndaren}")
strid = True

while strid == True:
    slow_print(f"Runda nummer {runda}")
    visa_hp()
    spelaren_chans = random.choice(chans)
    motståndaren_chans = random.choice(chans)
    slow_print("Vill du attackera med din näve (80% chans för 2 skada) eller med din spark (65% chans för 3 skada) eller med ditt svärd (50% chans för 5 skada)? ")
    spelaren_attack = input()
    motståndaren_attack = random.choice(attacker)
    if spelaren_attack == "näve" and spelaren_chans <= 80 and spelaren_hp > 0:
        slow_print(f"{spelaren} slår mot {motståndaren}...")
        slow_print("Och träffar!")
        motståndaren_hp -= 2
    elif spelaren_attack == "näve" and spelaren_chans > 80 and spelaren_hp > 0:
        slow_print(f"{spelaren} slår mot {motståndaren}...")
        slow_print("Och missar!")
    elif spelaren_attack == "spark" and spelaren_chans <= 65 and spelaren_hp > 0:
        slow_print(f"{spelaren} sparkar mot {motståndaren}...")
        slow_print("Och träffar!")
        motståndaren_hp -= 3
    elif spelaren_attack == "spark" and spelaren_chans > 65 and spelaren_hp > 0:
        slow_print(f"{spelaren} sparkar mot {motståndaren}...")
        slow_print("Och missar!")
    elif spelaren_attack == "svärd" and spelaren_chans <= 50 and spelaren_hp > 0:
        slow_print(f"{spelaren} svänger sitt svärd mot {motståndaren}...")
        slow_print("Och träffar!")
        motståndaren_hp -= 5
    elif spelaren_attack == "svärd" and spelaren_chans > 50 and spelaren_hp > 0:
        slow_print(f"{spelaren} svänger sitt svärd mot {motståndaren}...")
        slow_print("Och missar!")
    if motståndaren_attack == "näve" and motståndaren_chans <= 80 and motståndaren_hp > 0:
        slow_print(f"{motståndaren} slår mot {spelaren}...")
        slow_print("Och träffar!")
        spelaren_hp -= 2
    elif motståndaren_attack == "näve" and motståndaren_chans > 80 and motståndaren_hp > 0:
        slow_print(f"{motståndaren} slår mot {spelaren}...")
        slow_print("Och missar!")
    elif motståndaren_attack == "spark" and motståndaren_chans <= 65 and motståndaren_hp > 0:
        slow_print(f"{motståndaren} sparkar mot {spelaren}...")
        slow_print("Och träffar!")
        spelaren_hp -= 3
    elif motståndaren_attack == "spark" and motståndaren_chans > 65 and motståndaren_hp > 0:
        slow_print(f"{motståndaren} sparkar mot {spelaren}...")
        slow_print("Och missar!")
    elif motståndaren_attack == "svärd" and motståndaren_chans <= 50 and motståndaren_hp > 0:
        slow_print(f"{motståndaren} svänger sitt svärd mot {spelaren}...")
        slow_print("Och träffar!")
        spelaren_hp -= 5
    elif motståndaren_attack == "svärd" and motståndaren_chans > 50 and motståndaren_hp > 0:
        slow_print(f"{motståndaren} svänger sitt svärd mot {spelaren}...")
        slow_print("Och missar!")
    runda += 1
    if spelaren_hp <= 0 and motståndaren_hp > 0:
        slow_print(f"{spelaren} faller, {motståndaren} är segraren!")
        strid = False
    elif motståndaren_hp <= 0 and spelaren_hp > 0:
        slow_print(f"{motståndaren} faller, {spelaren} är segraren!")
        strid = False