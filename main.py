# THE ULTIMATE SOULELEMENT FINDER, by Jola Oke
# There's No Love Without Chemistry: A periodic table love calculator

import time
import random

# Lists of all the elements
elements = 'Lithium Sodium Potassium Rubidium Cesium Francium Beryllium Magnesium Calcium Strontium Barium Radium Scandium Yttrium Titanium Zirconium Hafnium Rutherfordium Vanadium Niobium Tantalum Dubnium Chromium Molybdenum Tungsten Seaborgium Managanese Technetium Rhenium Bohrium Iron Ruthenium Osmium Hassium Cobalt Rhodium Iridium Nickel Palladium Platinum Copper Silver Gold Zinc Cadmium Mercury Copernicium Lanthanum Cerium Praseodymium Neodymium Promethium Samarium Europium Gadolinium Terbium Dysprosium Holmium Erbium Thulium Ytterbium Lutetium Actinium Thorium Protactinium Uranium Neptunium Plutonium Americium Curium Berkelium Californium Einsteinium Fermium Mendelevium Nobelium Lawrencium Aluminum Gallium Indium Thallium Tin Lead Bismuth Polonium Carbon Nitrogen Oxygen Phosphorus Sulfur Selenium Fluorine Chlorine Bromine Iodine Astatine Helium Neon Argon Krypton Xenon Radon Boron Silicon Germanium Arsenic Antimony Tellurium Meitnerium Damstadtium Roentgenium Ununtrium Flerovium Ununpentium Livermorium Ununseptium Ununoctium'.split()
metals = 'Lithium Sodium Potassium Rubidium Cesium Francium Beryllium Magnesium Calcium Strontium Barium Radium Scandium Yttrium Titanium Zirconium Hafnium Rutherfordium Vanadium Niobium Tantalum Dubnium Chromium Molybdenum Tungsten Seaborgium Managanese Technetium Rhenium Bohrium Iron Ruthenium Osmium Hassium Cobalt Rhodium Iridium Nickel Palladium Platinum Copper Silver Gold Zinc Cadmium Mercury Copernicium Lanthanum Cerium Praseodymium Neodymium Promethium Samarium Europium Gadolinium Terbium Dysprosium Holmium Erbium Thulium Ytterbium Lutetium Actinium Thorium Protactinium Uranium Neptunium Plutonium Americium Curium Berkelium Californium Einsteinium Fermium Mendelevium Nobelium Lawrencium Aluminum Gallium Indium Thallium Tin Lead Bismuth Polonium'.split()
transitionMetals = 'Scandium Yttrium Titanium Zirconium Hafnium Rutherfordium Vanadium Niobium Tantalum Dubnium Chromium Molybdenum Tungsten Seaborgium Managanese Technetium Rhenium Bohrium Iron Ruthenium Osmium Hassium Cobalt Rhodium Iridium Nickel Palladium Platinum Copper Silver Gold Zinc Cadmium Mercury Copernicium'.split()
alkaliMetals = 'Lithium Sodium Potassium Rubidium Cesium Francium'.split()
alkalineEarthMetals = 'Beryllium Magnesium Calcium Strontium Barium Radium'.split()
lanthanides = 'Lanthanum Cerium Praseodymium Neodymium Promethium Samarium Europium Gadolinium Terbium Dysprosium Holmium Erbium Thulium Ytterbium Lutetium'.split()
actinides = 'Actinium Thorium Protactinium Uranium Neptunium Plutonium Americium Curium Berkelium Californium Einsteinium Fermium Mendelevium Nobelium Lawrencium'.split()
postTransitionMetals = 'Aluminum Gallium Indium Thallium Tin Lead Bismuth Polonium'.split()
metalloids = 'Boron Silicon Germanium Arsenic Antimony Tellurium'.split()
nonMetals = 'Carbon Nitrogen Oxygen Phosphorus Sulfur Selenium Fluorine Chlorine Bromine Iodine Astatine Helium Neon Argon Krypton Xenon Radon'.split()
otherNonMetals = 'Carbon Nitrogen Oxygen Phosphorus Sulfur Selenium'.split()
halogens = 'Fluorine Chlorine Bromine Iodine Astatine'.split()
nobleGases = 'Helium Neon Argon Krypton Xenon Radon'.split()
unknown = 'Meitnerium Damstadtium Roentgenium Ununtrium Flerovium Ununpentium Livermorium Ununseptium Ununoctium'.split()
soulelement = [] # The list containing the possible matches for the user

def displayIntro(): # The introduction to the program
    print("We all know that love is all about the chemistry.")
    time.sleep(2.5)
    print("So let's...")
    time.sleep(2)
    print("Get...")
    time.sleep(1.5)
    print("CHEMICAL!\n")
    time.sleep(1)
    print("Have you been searching for that one element?")
    time.sleep(2)
    print("Has the periodic table been unfavorable to you?")
    time.sleep(2)
    print("Well search no more!")
    time.sleep(1)
    print("WELCOME TO THE ULTIMATE SOULELEMENT FINDER")
    time.sleep(1.5)
    print("Today is the day you find true love. Just answer these few questions.")
    time.sleep(1)

def calculating(): # Add dramatic effect to the program when finding the matching element
    print("Calculating...")
    time.sleep(1)
    for i in range(0,random.randint(60,90)): #To give a matrix-like effect
        print(i,'     ',i/120,'     ',i+random.randint(3,9),'     ',i*0.374)
    time.sleep(1)
    print("Parsing...")
    time.sleep(1)
    print("Localizing...")
    time.sleep(1)
    print("Analyzing..")
    time.sleep(1)
    print("Finalizing...\n")
    time.sleep(2)

def findElement(): # Select the element from the soulelement list and tell the user their matching element
    global soulelement
    print("The search is over.")
    time.sleep(1)
    print("Your soulelement has been found.")
    time.sleep(1)
    print("Your one and only is...")
    time.sleep(1)
    print(random.choice(random.choice(soulelement)).upper() + "!") # random.choice is used twice because the first one chooses a list from soulelement, and the second chooses an item from that list chosen
    
def main(): # The main chunk of the program that the user interacts most with.
    # Put the global variables into the scope of the function
    global elements
    global metals
    global transitionMetals
    global alkaliMetals
    global alkalineEarthMetals
    global lanthanides
    global actinides
    global postTransitionMetals
    global metalloids
    global nonMetals
    global otherNonMetals
    global halogens
    global nobleGases
    global unknown
    global soulelement
    
    # The series of questions asked. The soulelement is determined by the answers to these questions
    # Depending on the user input, certain lists will be appended to the soulelements list, and certain lists will be removed from the soulelements list
    print("What is your full name?")
    name = input().title() # .title() capitalizes the first letter of each word in a string
    print("Do you like romanitic, candle-lit dinners?")
    dinner = input().lower()
    if dinner == 'y' or dinner == 'yes' or dinner == 'i do' or dinner == 'yeah' or dinner == 'yep':
        print("Would you wear a colorful and flashy outfit to a dinner date?")
        outfit = input().lower()
        if outfit == 'y' or outfit == 'yes' or outfit == 'i do' or outfit == 'yeah' or outfit == 'yep':
            soulelement.append(halogens)
        else:
            soulelement.append(alkaliMetals)
    else:
        soulelement.append(alkalineEarthMetals)
    print("If you had to, would you have a long-distance relationship?")
    ld = input().lower()
    if ld == 'y' or ld == 'yes' or ld == 'i do' or ld == 'yeah' or ld == 'yep':
        soulelement.append(lanthanides)
    elif ld == 'maybe' or ld == 'i don\'t know' or ld == 'not sure':
        soulelement.append(actinides)
    print("Have you recently been in a relationship?")
    recent = input().lower()
    if recent == 'y' or recent == 'yes' or recent == 'i do' or recent == 'yeah' or recent == 'yep':
        soulelement.append(transitionMetals)
    print("Would you move in and live with your partner?")
    live = input().lower()
    if live == 'n' or live == 'no' or live == 'nope' or live == 'nah':
        soulelement.append(nobleGases)
        if alkaliMetals in soulelement:
            soulelement.remove(alkaliMetals)
        if halogens in soulelement:
            soulelement.remove(halogens)
    if live == 'y' or live == 'yes' or live == 'i do' or live == 'yeah' or live == 'yep':
        if alkaliMetals not in soulelement:
            soulelement.append(alkaliMetals)
        if halogens not in soulelement:
            soulelement.append(halogens)
    print("Do you like to take charge in a relationship?")
    charge = input().lower()
    if charge == 'y' or charge == 'yes' or charge == 'i do' or charge == 'yeah' or charge == 'yep':
        soulelement.append(otherNonMetals)
        for e in soulelement: # Remove any element from soulelements that is a metal
            if e in metals:
                soulelement.remove(e)
    print("Do you want an open relationship?")
    openr = input().lower()
    if openr == 'y' or openr == 'yes' or openr == 'i do' or openr == 'yeah' or openr == 'yep':
        soulelement = metalloids
    print("Would you go on a blind date?")
    blind = input().lower()
    if blind == 'y' or blind == 'yes' or blind == 'i do' or blind == 'yeah' or blind == 'yep':
        soulelement = unknown
    time.sleep(0.5)
    print("Okay, that's it! Please wait a moment.\n")
    time.sleep(1)

    #Show the results
    calculating()
    findElement()

run = True

while run: #Run the program
    displayIntro()
    main()
    time.sleep(1)
    print("\nDo you to play again?")
    # Ask the user if they would like to play the game again
    playAgain = input().lower()
    if playAgain == 'y' or playAgain == 'yes' or playAgain == 'yeah' or playAgain == 'yep' or playAgain == 'play again' or playAgain == 'i do':
        soulelement = [] # Reset the variable
        run = True # Run program again
    else:
        run = False # End program
