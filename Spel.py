print("""
    Hej och välkommen till mitt spel där du ska gissa talet.
    Du skriver en siffra mellan 1-100, får du fel så säger datorn högre eller lägre.
    Du får 7 chanser.
    """)
import random
import os 
os.system('cls')
while True:
    try:

        specifikatalet = random.randint(1,100)
        print(specifikatalet)
        försök = 6
        gissning = int(input("Skriv det tal du gissar att datorn valt: "))
        if gissning > specifikatalet:
            print("Talet är lägre än",int(gissning), ".Du  har ",försök, " försök kvar.")
            försök -= 1
        elif gissning < specifikatalet:
            print("Talet är högre än",int(gissning), ".Du har ",försök, " försök kvar.")
            försök -= 1 
        elif gissning == specifikatalet:
            print("Korrekt! Talet var", int(specifikatalet))
            svar = input()
            if svar == "Nej" or svar == "nej":
                break
            elif svar == "ja" or svar == "Ja":
                continue


            
    except ValueError:
        print("Felaktig inmatning, du måste skriva en siffra")
        continue
    try: 
        andragissning = int(input("Fortsätt gissa: "))
        if andragissning > specifikatalet:
            print("Talet är lägre än",int(andragissning), ".Du  har ", försök, " försök kvar.")
            försök -= 1
        elif andragissning < specifikatalet:
            print("Talet är högre än",int(andragissning), ".Du  har ", försök, " försök kvar.")
            försök -= 1
        elif andragissning == specifikatalet:
            print("Korrekt! Talet var", int(specifikatalet))
            break
    except ValueError:
        print("Felaktig inmatning, du måste skriva en siffra")

    try:        
        tredjegissning = int(input("Fortsätt gissa: "))
        if tredjegissning > specifikatalet:
            print("Talet är lägre än",int(tredjegissning), ".Du  har ", försök, " försök kvar.")
            försök -= 1
        elif tredjegissning < specifikatalet:
            print("Talet är högre än",int(tredjegissning), ".Du  har ", försök, " försök kvar.")
            försök -= 1
        elif tredjegissning == specifikatalet:
            print("Korrekt! Talet var", int(specifikatalet))  
            break
    except ValueError:
        print("Felaktig inmatning, du måste skriva en siffra")



    try:
        fjärdegissning = int(input("Fortsätt gissa: "))
        if fjärdegissning > specifikatalet:
            print("Talet är lägre än",int(fjärdegissning), ".Du  har ", försök, " försök kvar.")
            försök -= 1
        elif fjärdegissning < specifikatalet:
            print("Talet är högre än",int(fjärdegissning), ".Du  har ", försök, " försök kvar.")
            försök -= 1
        elif tredjegissning == specifikatalet:
            print("Korrekt! Talet var", int(specifikatalet)) 
            break
    except ValueError:
        print("Felaktig inmatning, du måste skriva en siffra")
    try:
        femtegissning = int(input("Fortsätt gissa: "))
        if femtegissning > specifikatalet:
            print("Talet är lägre än",int(femtegissning), ".Du  har ", försök, " försök kvar.")
            försök -= 1
        elif femtegissning < specifikatalet:
            print("Talet är högre än",int(femtegissning), ".Du  har ", försök, " försök kvar.")
            försök -= 1
        elif femtegissning == specifikatalet:
            print("Korrekt! Talet var", int(specifikatalet)) 
            break
    except ValueError:
        print("Felaktig inmatning, du måste skriva en siffra")
    try:   
        Sjättegissning = int(input("Fortsätt gissa: "))
        if Sjättegissning > specifikatalet:
            print("Talet är lägre än",int(Sjättegissning), ".Du  har ", försök, " försök kvar.")
            försök -= 1
        elif Sjättegissning < specifikatalet:
            print("Talet är högre än",int(Sjättegissning), ".Du  har ", försök, " försök kvar.")
            försök -= 1
        elif Sjättegissning == specifikatalet:
            print("Korrekt! Talet var", int(specifikatalet)) 
            break
    except ValueError:
            print("Felaktig inmatning, du måste skriva en siffra")
    try:
        sjundegissning = int(input("Fortsätt gissa: "))
        if sjundegissning > specifikatalet:
            print("Talet är lägre än",int(sjundegissning), ".Du  har ", försök, " försök kvar.")
            försök -= 1
        elif sjundegissning < specifikatalet:
            print("Talet är högre än",int(sjundegissning), ".Du  har ", försök, " försök kvar.")
            försök -= 1
            
        elif sjundegissning == specifikatalet:
            print("Korrekt! Talet var", int(specifikatalet)) 
            break
        elif not sjundegissning == specifikatalet: 
            print("Du förlorade, talet var", int(specifikatalet), ". Vill du köra igen, Ja/Nej: ")
            svar = input()
            if svar == "Ja" or svar == "ja":
                continue
            elif svar == "Nej" or svar == "nej":
                break
        if försök == 0:
            print("Du har förlorat, talet var", specifikatalet)
            break
    except ValueError:
        print("Felaktig inmatning, du måste skriva en siffra")
        
        