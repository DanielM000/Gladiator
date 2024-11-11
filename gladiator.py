import random
import time
def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

slow_print("Välkommen till Colosseum! Du är en gladiator som ska strida en motståndare tills en dödas.")
slow_print("Vad är ditt namn unge krigare? ")
spelaren = input()
motståndarna = ["Spartacus", "Flamma", "Priscus", "Spiculus", "Tetraites", "Commodus", "Marcus", "Aurelius", "Decimus", "Gaius", "Maximus", "Verus", "Crixus", "Carpophorus", "Antonius", "Augustus"]
motståndaren = random.choice(motståndarna)
attacker = ["näve", "spark", "svärd", "sköld"]
spelaren_hp = 20
motståndaren_hp = 20
spelaren_sköld = 3
motståndaren_sköld = 3
spelaren_sköld_notis = 1
motståndaren_sköld_notis = 1
slow_print("Vilken svårighetsgrad väljer du, lätt (20 hälsopoäng), medelsvår (15 hälsopoäng eller svår (10 hälsopoäng)?")
svårighetsgrad = input()
if svårighetsgrad == "medelsvår":
    spelaren_hp = 15
elif svårighetsgrad == "svår":
    spelaren_hp = 10
else:
    spelaren_hp = 20
runda = 1
def visa_hp():
    slow_print(f"{spelaren} har just nu {spelaren_hp} hälsopoäng kvar.")
    slow_print(f"{motståndaren} har just nu {motståndaren_hp} hälsopoäng kvar.")
slow_print(f"Din motståndare är {motståndaren}")
strid = True



while strid == True:
    slow_print(f"Runda nummer {runda}")
    visa_hp()
    spelaren_chans = random.randint(1,100)
    motståndaren_chans = random.randint(1,100)
    print("Vill attack väljer du?\n1.Din näve (80% chans för 2 skada)\n2.Din spark (65% chans för 3 skada)\n3.Ditt svärd (50% chans för 5 skada)\n4.Din sköld (går sönder efter 3 svärdsattacker,\nom motståndaren missar så slår du honom med 1 skada)")
    spelaren_attack = input()
    motståndaren_attack = random.choice(attacker)
    if spelaren_attack == "näve" and spelaren_chans <= 80 and spelaren_hp > 0 and not motståndaren_attack == "sköld" or motståndaren_attack == "sköld" and motståndaren_sköld <= 0:
        slow_print(f"{spelaren} slår mot {motståndaren}...")
        slow_print("Och träffar!")
        motståndaren_hp -= 2
    elif spelaren_attack == "näve" and spelaren_chans > 80 and spelaren_hp > 0 and not motståndaren_attack == "sköld" or motståndaren_attack == "sköld" and motståndaren_sköld <= 0:
        slow_print(f"{spelaren} slår mot {motståndaren}...")
        slow_print("Och missar!")
    elif spelaren_attack == "näve" and spelaren_chans <= 80 and spelaren_hp > 0 and motståndaren_attack == "sköld" and motståndaren_sköld > 0:
        slow_print(f"{spelaren} slår mot {motståndaren}...")
        slow_print("Och träffar men den blir blockerad!")
    elif spelaren_attack == "näve" and spelaren_chans > 80 and spelaren_hp > 0 and motståndaren_attack == "sköld" and motståndaren_sköld > 0:
        slow_print(f"{spelaren} slår mot {motståndaren}...")
        slow_print("Och missar!")
        slow_print(f"{motståndaren} slår {spelaren} med skölden!")
        spelaren_hp -= 1
    elif spelaren_attack == "spark" and spelaren_chans <= 65 and spelaren_hp > 0 and not motståndaren_attack == "sköld" or motståndaren_attack == "sköld" and motståndaren_sköld <= 0:
        slow_print(f"{spelaren} sparkar mot {motståndaren}...")
        slow_print("Och träffar!")
        motståndaren_hp -= 3
    elif spelaren_attack == "spark" and spelaren_chans > 65 and spelaren_hp > 0 and not motståndaren_attack == "sköld" or motståndaren_attack == "sköld" and motståndaren_sköld <= 0:
        slow_print(f"{spelaren} sparkar mot {motståndaren}...")
        slow_print("Och missar!")
    elif spelaren_attack == "spark" and spelaren_chans <= 65 and spelaren_hp > 0 and motståndaren_attack == "sköld" and motståndaren_sköld > 0:
        slow_print(f"{spelaren} sparkar mot {motståndaren}...")
        slow_print("Och träffar men den blir blockerad!")
    elif spelaren_attack == "spark" and spelaren_chans > 65 and spelaren_hp > 0 and motståndaren_attack == "sköld" and motståndaren_sköld > 0:
        slow_print(f"{spelaren} sparkar mot {motståndaren}...")
        slow_print("Och missar!")
        slow_print(f"{motståndaren} slår {spelaren} med skölden!")
        spelaren_hp -= 1
    elif spelaren_attack == "svärd" and spelaren_chans <= 50 and spelaren_hp > 0 and not motståndaren_attack == "sköld" or motståndaren_attack == "sköld" and motståndaren_sköld <= 0:
        slow_print(f"{spelaren} svänger sitt svärd mot {motståndaren}...")
        slow_print("Och träffar!")
        motståndaren_hp -= 5
    elif spelaren_attack == "svärd" and spelaren_chans > 50 and spelaren_hp > 0 and not motståndaren_attack == "sköld" or motståndaren_attack == "sköld" and motståndaren_sköld <= 0:
        slow_print(f"{spelaren} svänger sitt svärd mot {motståndaren}...")
        slow_print("Och missar!")
    elif spelaren_attack == "svärd" and spelaren_chans <= 50 and spelaren_hp > 0 and motståndaren_attack == "sköld" and motståndaren_sköld > 0:
        slow_print(f"{spelaren} svänger sitt svärd mot {motståndaren}...")
        slow_print("Och träffar men den blir blockerad!")
        slow_print(f"{motståndaren}s sköld skadas.")
        motståndaren_sköld -= 1
    elif spelaren_attack == "svärd" and spelaren_chans > 50 and spelaren_hp > 0 and motståndaren_attack == "sköld" and motståndaren_sköld > 0:
        slow_print(f"{spelaren} svänger sitt svärd mot {motståndaren}...")
        slow_print("Och missar!")
        slow_print(f"{motståndaren} slår {spelaren} med skölden!")
        spelaren_hp -= 1
    elif spelaren_attack == "sköld" and spelaren_sköld <= 0 and not motståndaren_attack == "sköld":
        slow_print(f"{spelaren} har ingen sköld.")
    elif spelaren_attack == "sköld" and spelaren_sköld <= 0 and motståndaren_attack == "sköld" and motståndaren_sköld <= 0:
        slow_print(f"{spelaren} har ingen sköld.")
        slow_print(f"{motståndaren} slår {spelaren} med skölden!")
        spelaren_hp -= 1
    if motståndaren_attack == "näve" and motståndaren_chans <= 80 and motståndaren_hp > 0 and not spelaren_attack == "sköld" or spelaren_attack == "sköld" and spelaren_sköld <= 0:
        slow_print(f"{motståndaren} slår mot {spelaren}...")
        slow_print("Och träffar!")
        spelaren_hp -= 2
    elif motståndaren_attack == "näve" and motståndaren_chans > 80 and motståndaren_hp > 0 and not spelaren_attack == "sköld" or spelaren_attack == "sköld" and spelaren_sköld <= 0:
        slow_print(f"{motståndaren} slår mot {spelaren}...")
        slow_print("Och missar!")
    elif motståndaren_attack == "näve" and motståndaren_chans <= 80 and motståndaren_hp > 0 and spelaren_attack == "sköld" and spelaren_sköld > 0:
        slow_print(f"{motståndaren} slår mot {spelaren}...")
        slow_print("Och träffar men den blir blockerad!")
    elif motståndaren_attack == "näve" and motståndaren_chans > 80 and motståndaren_hp > 0 and spelaren_attack == "sköld" and spelaren_sköld > 0:
        slow_print(f"{motståndaren} slår mot {spelaren}...")
        slow_print("Och missar!")
        slow_print(f"{spelaren} slår {motståndaren} med skölden!")
        motståndaren_hp -= 1
    elif motståndaren_attack == "spark" and motståndaren_chans <= 65 and motståndaren_hp > 0 and not spelaren_attack == "sköld" or spelaren_attack == "sköld" and spelaren_sköld <= 0:
        slow_print(f"{motståndaren} sparkar mot {spelaren}...")
        slow_print("Och träffar!")
        spelaren_hp -= 3
    elif motståndaren_attack == "spark" and motståndaren_chans > 65 and motståndaren_hp > 0 and not spelaren_attack == "sköld" or spelaren_attack == "sköld" and spelaren_sköld <= 0:
        slow_print(f"{motståndaren} sparkar mot {spelaren}...")
        slow_print("Och missar!")
    elif motståndaren_attack == "spark" and motståndaren_chans <= 65 and motståndaren_hp > 0 and spelaren_attack == "sköld" and spelaren_sköld > 0:
        slow_print(f"{motståndaren} sparkar mot {spelaren}...")
        slow_print("Och träffar men den blir blockerad!")
    elif motståndaren_attack == "spark" and motståndaren_chans > 65 and motståndaren_hp > 0 and spelaren_attack == "sköld" and spelaren_sköld > 0:
        slow_print(f"{motståndaren} sparkar mot {spelaren}...")
        slow_print("Och missar!")
        slow_print(f"{spelaren} slår {motståndaren} med skölden!")
        motståndaren_hp -= 1
    elif motståndaren_attack == "svärd" and motståndaren_chans <= 50 and motståndaren_hp > 0 and not spelaren_attack == "sköld" or spelaren_attack == "sköld" and spelaren_sköld <= 0:
        slow_print(f"{motståndaren} svänger sitt svärd mot {spelaren}...")
        slow_print("Och träffar!")
        spelaren_hp -= 5
    elif motståndaren_attack == "svärd" and motståndaren_chans > 50 and motståndaren_hp > 0 and not spelaren_attack == "sköld" or spelaren_attack == "sköld" and spelaren_sköld <= 0:
        slow_print(f"{motståndaren} svänger sitt svärd mot {spelaren}...")
        slow_print("Och missar!")
    elif motståndaren_attack == "svärd" and motståndaren_chans <= 50 and motståndaren_hp > 0 and spelaren_attack == "sköld" and spelaren_sköld > 0:
        slow_print(f"{motståndaren} svänger sitt svärd mot {spelaren}...")
        slow_print("Och träffar men den blir blockerad!")
        slow_print(f"{spelaren}s sköld skadas.")
        spelaren_sköld -= 1
    elif motståndaren_attack == "svärd" and motståndaren_chans > 50 and motståndaren_hp > 0 and spelaren_attack == "sköld" and spelaren_sköld > 0:
        slow_print(f"{motståndaren} svänger sitt svärd mot {spelaren}...")
        slow_print("Och missar!")
        slow_print(f"{spelaren} slår {motståndaren} med skölden!")
        motståndaren_hp -= 1
    elif motståndaren_attack == "sköld" and motståndaren_sköld <= 0 and not spelaren_attack == "sköld":
        slow_print(f"{motståndaren} har ingen sköld.")
    elif motståndaren_attack == "sköld" and motståndaren_sköld <= 0 and spelaren_attack == "sköld" and spelaren_sköld <= 0:
        slow_print(f"{motståndaren} har ingen sköld.")
        slow_print(f"{spelaren} slår {motståndaren} med skölden!")
        motståndaren_hp -= 1
    if spelaren_attack == "sköld" and motståndaren_attack == "sköld" and spelaren_sköld > 0 and motståndaren_sköld > 0 and spelaren_hp > 0 and motståndaren_hp > 0:
        slow_print(f"Både {spelaren} och {motståndaren} håller upp skölden.")
    if spelaren_sköld <= 0 and spelaren_hp > 0 and spelaren_sköld_notis > 0:
        slow_print(f"{spelaren}s sköld går sönder!")
        spelaren_sköld_notis -= 1
    if motståndaren_sköld <= 0 and motståndaren_hp > 0 and motståndaren_sköld_notis > 0:
        slow_print(f"{motståndaren}s sköld går sönder!")
        attacker.remove("sköld")
        motståndaren_sköld_notis -= 1
    runda += 1
    if spelaren_hp <= 0 and motståndaren_hp > 0:
        slow_print(f"{spelaren} faller, {motståndaren} är segraren!")
        strid = False
    elif motståndaren_hp <= 0 and spelaren_hp > 0:
        slow_print(f"{motståndaren} faller, {spelaren} är segraren!")
        strid = False