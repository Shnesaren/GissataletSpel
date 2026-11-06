
__author__ = "Jonatan Sköld"
__version__ = "1.0.0"
__email__ = "jonatan.skold@elev.ga.dbgy.se"


import random
import os
from bcolors import bcolors
 
os.system('cls')

print(f"""{bcolors.OKGREEN}{bcolors.BOLD}
Välkommen till mitt spel där du ska gissa talet som datorn valt mellan 1-100. Du har 7 försök. \n Tryck {bcolors.WARNING} 0 {bcolors.ENDC} {bcolors.OKGREEN}{bcolors.BOLD} för att avsluta närsomhelst
{bcolors.ENDC}""")
försök = 6
specifika_talet = random.randint(1,100)
while True:
        
        try:

            gissning = int(input(f"\n \n{bcolors.OKCYAN}Gissa talet: {bcolors.ENDC}"))
        except ValueError:
            print(f"{bcolors.FAIL}Endast siffror{bcolors.ENDC}")
            continue


        if gissning == 0:
            print(f"{bcolors.WARNING}Avslutar....{bcolors.ENDC}")
            break
        if gissning == specifika_talet:

            print(f"{bcolors.OKGREEN}Korrekt! Talet var{bcolors.HEADER}", specifika_talet, (bcolors.ENDC))
            köraigen = input(f"{bcolors.OKBLUE}Vill du köra spelet igen? ({bcolors.OKGREEN}J{bcolors.ENDC}{bcolors.OKBLUE}/{bcolors.ENDC}{bcolors.WARNING}N{bcolors.ENDC}{bcolors.OKBLUE}): {bcolors.ENDC}")
            if köraigen == "N" or köraigen == "n":
                print(f"{bcolors.WARNING}Avslutar....{bcolors.ENDC}")
                break
            elif köraigen == "J" or köraigen ==  "j":

                försök = 6
                specifika_talet = random.randint(1, 100)
                continue

        elif gissning > specifika_talet:

            print(f"{bcolors.OKBLUE}Talet är lägre än {bcolors.UNDERLINE}{bcolors.HEADER}{gissning}{bcolors.ENDC} {bcolors.OKBLUE}Du har {bcolors.UNDERLINE}{bcolors.HEADER}{försök}{bcolors.ENDC} {bcolors.OKBLUE}försök kvar{bcolors.ENDC}")
            försök -= 1
        elif gissning < specifika_talet:

            print(f"{bcolors.OKBLUE}Talet är högre än {bcolors.UNDERLINE}{bcolors.HEADER}{gissning}{bcolors.ENDC} {bcolors.OKBLUE}Du har {bcolors.UNDERLINE}{bcolors.HEADER}{försök}{bcolors.ENDC} {bcolors.OKBLUE}försök kvar{bcolors.ENDC}")
            försök -= 1
        if försök == -1:

            print(f"{bcolors.FAIL}{bcolors.BOLD}YOU LOST.{bcolors.ENDC} {bcolors.OKBLUE}Talet var {bcolors.HEADER}{bcolors.BOLD}{bcolors.UNDERLINE}{specifika_talet}{bcolors.ENDC}")
            köraigen = input(f"{bcolors.OKBLUE}Vill du köra spelet igen? ({bcolors.OKGREEN}J{bcolors.ENDC}{bcolors.OKBLUE}/{bcolors.ENDC}{bcolors.WARNING}N{bcolors.ENDC}{bcolors.OKBLUE}): {bcolors.ENDC}")
            if köraigen == "N" or köraigen == "n":

                print(f"{bcolors.WARNING}Avslutar....{bcolors.ENDC}")
                break
            elif köraigen == "J" or köraigen ==  "j":

                försök = 6
                specifika_talet = random.randint(1, 100)
                continue
                
