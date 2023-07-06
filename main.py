import random

#Main Vars
game = False
element_guessed = False
elements = [
    {'name': 'Hydrogen', 'symbol': 'H', 'atomic_number': 1, 'type': 'Nonmetal'},
    {'name': 'Helium', 'symbol': 'He', 'atomic_number': 2, 'type': 'Noble gas'},
    {'name': 'Lithium', 'symbol': 'Li', 'atomic_number': 3, 'type': 'Alkali metal'},
    {'name': 'Beryllium', 'symbol': 'Be', 'atomic_number': 4, 'type': 'Alkaline earth metal'},
    {'name': 'Boron', 'symbol': 'B', 'atomic_number': 5, 'type': 'Metalloid'},
    {'name': 'Carbon', 'symbol': 'C', 'atomic_number': 6, 'type': 'Nonmetal'},
    {'name': 'Nitrogen', 'symbol': 'N', 'atomic_number': 7, 'type': 'Nonmetal'},
    {'name': 'Oxygen', 'symbol': 'O', 'atomic_number': 8, 'type': 'Nonmetal'},
    {'name': 'Fluorine', 'symbol': 'F', 'atomic_number': 9, 'type': 'Halogen'},
    {'name': 'Neon', 'symbol': 'Ne', 'atomic_number': 10, 'type': 'Noble gas'},
    {'name': 'Sodium', 'symbol': 'Na', 'atomic_number': 11, 'type': 'Alkali metal'},
    {'name': 'Magnesium', 'symbol': 'Mg', 'atomic_number': 12, 'type': 'Alkaline earth metal'},
    {'name': 'Aluminum', 'symbol': 'Al', 'atomic_number': 13, 'type': 'Post-transition metal'},
    {'name': 'Silicon', 'symbol': 'Si', 'atomic_number': 14, 'type': 'Metalloid'},
    {'name': 'Phosphorus', 'symbol': 'P', 'atomic_number': 15, 'type': 'Nonmetal'},
    {'name': 'Sulfur', 'symbol': 'S', 'atomic_number': 16, 'type': 'Nonmetal'},
    {'name': 'Chlorine', 'symbol': 'Cl', 'atomic_number': 17, 'type': 'Halogen'},
    {'name': 'Argon', 'symbol': 'Ar', 'atomic_number': 18, 'type': 'Noble gas'},
    {'name': 'Potassium', 'symbol': 'K', 'atomic_number': 19, 'type': 'Alkali metal'},
    {'name': 'Calcium', 'symbol': 'Ca', 'atomic_number': 20, 'type': 'Alkaline earth metal'},
    {'name': 'Scandium', 'symbol': 'Sc', 'atomic_number': 21, 'type': 'Transition metal'},
    {'name': 'Titanium', 'symbol': 'Ti', 'atomic_number': 22, 'type': 'Transition metal'},
    {'name': 'Vanadium', 'symbol': 'V', 'atomic_number': 23, 'type': 'Transition metal'},
    {'name': 'Chromium', 'symbol': 'Cr', 'atomic_number': 24, 'type': 'Transition metal'},
    {'name': 'Manganese', 'symbol': 'Mn', 'atomic_number': 25, 'type': 'Transition metal'},
    {'name': 'Krypton', 'symbol': 'Kr', 'atomic_number': 36, 'type': 'Noble gas'},
    {'name': 'Cobalt', 'symbol': 'Co', 'atomic_number': 27, 'type': 'Transition metal'},
    {'name': 'Nickel', 'symbol': 'Ni', 'atomic_number': 28, 'type': 'Transition metal'},
    {'name': 'Copper', 'symbol': 'Cu', 'atomic_number': 29, 'type': 'Transition metal'},
    {'name': 'Zinc', 'symbol': 'Zn', 'atomic_number': 30, 'type': 'Transition metal'},
    {'name': 'Gallium', 'symbol': 'Ga', 'atomic_number': 31, 'type': 'Post-transition metal'},
    {'name': 'Germanium', 'symbol': 'Ge', 'atomic_number': 32, 'type': 'Metalloid'},
    {'name': 'Arsenic', 'symbol': 'As', 'atomic_number': 33, 'type': 'Metalloid'},
    {'name': 'Selenium', 'symbol': 'Se', 'atomic_number': 34, 'type': 'Nonmetal'},
    {'name': 'Bromine', 'symbol': 'Br', 'atomic_number': 35, 'type': 'Halogen'},
    {'name': 'Krypton', 'symbol': 'Kr', 'atomic_number': 36, 'type': 'Noble gas'},
    {'name': 'Rubidium', 'symbol': 'Rb', 'atomic_number': 37, 'type': 'Alkali metal'},
    {'name': 'Strontium', 'symbol': 'Sr', 'atomic_number': 38, 'type': 'Alkaline earth metal'},
    {'name': 'Yttrium', 'symbol': 'Y', 'atomic_number': 39, 'type': 'Transition metal'},
    {'name': 'Zirconium', 'symbol': 'Zr', 'atomic_number': 40, 'type': 'Transition metal'},
    {'name': 'Niobium', 'symbol': 'Nb', 'atomic_number': 41, 'type': 'Transition metal'},
    {'name': 'Molybdenum', 'symbol': 'Mo', 'atomic_number': 42, 'type': 'Transition metal'},
    {'name': 'Technetium', 'symbol': 'Tc', 'atomic_number': 43, 'type': 'Transition metal'},
    {'name': 'Ruthenium', 'symbol': 'Ru', 'atomic_number': 44, 'type': 'Transition metal'},
    {'name': 'Rhodium', 'symbol': 'Rh', 'atomic_number': 45, 'type': 'Transition metal'},
    {'name': 'Palladium', 'symbol': 'Pd', 'atomic_number': 46, 'type': 'Transition metal'},
    {'name': 'Silver', 'symbol': 'Ag', 'atomic_number': 47, 'type': 'Transition metal'},
    {'name': 'Cadmium', 'symbol': 'Cd', 'atomic_number': 48, 'type': 'Transition metal'},
    {'name': 'Indium', 'symbol': 'In', 'atomic_number': 49, 'type': 'Post-transition metal'},
    {'name': 'Tin', 'symbol': 'Sn', 'atomic_number': 50, 'type': 'Post-transition metal'},
    {'name': 'Antimony', 'symbol': 'Sb', 'atomic_number': 51, 'type': 'Metalloid'},
    {'name': 'Tellurium', 'symbol': 'Te', 'atomic_number': 52, 'type': 'Metalloid'},
    {'name': 'Iodine', 'symbol': 'I', 'atomic_number': 53, 'type': 'Halogen'},
    {'name': 'Xenon', 'symbol': 'Xe', 'atomic_number': 54, 'type': 'Noble gas'},
    {'name': 'Cesium', 'symbol': 'Cs', 'atomic_number': 55, 'type': 'Alkali metal'},
    {'name': 'Barium', 'symbol': 'Ba', 'atomic_number': 56, 'type': 'Alkaline earth metal'},
    {'name': 'Lanthanum', 'symbol': 'La', 'atomic_number': 57, 'type': 'Lanthanide'},
    {'name': 'Cerium', 'symbol': 'Ce', 'atomic_number': 58, 'type': 'Lanthanide'},
    {'name': 'Praseodymium', 'symbol': 'Pr', 'atomic_number': 59, 'type': 'Lanthanide'},
    {'name': 'Neodymium', 'symbol': 'Nd', 'atomic_number': 60, 'type': 'Lanthanide'},
    {'name': 'Promethium', 'symbol': 'Pm', 'atomic_number': 61, 'type': 'Lanthanide'},
    {'name': 'Samarium', 'symbol': 'Sm', 'atomic_number': 62, 'type': 'Lanthanide'},
    {'name': 'Europium', 'symbol': 'Eu', 'atomic_number': 63, 'type': 'Lanthanide'},
    {'name': 'Gadolinium', 'symbol': 'Gd', 'atomic_number': 64, 'type': 'Lanthanide'},
    {'name': 'Terbium', 'symbol': 'Tb', 'atomic_number': 65, 'type': 'Lanthanide'},
    {'name': 'Dysprosium', 'symbol': 'Dy', 'atomic_number': 66, 'type': 'Lanthanide'},
    {'name': 'Holmium', 'symbol': 'Ho', 'atomic_number': 67, 'type': 'Lanthanide'},
    {'name': 'Erbium', 'symbol': 'Er', 'atomic_number': 68, 'type': 'Lanthanide'},
    {'name': 'Thulium', 'symbol': 'Tm', 'atomic_number': 69, 'type': 'Lanthanide'},
    {'name': 'Ytterbium', 'symbol': 'Yb', 'atomic_number': 70, 'type': 'Lanthanide'},
    {'name': 'Lutetium', 'symbol': 'Lu', 'atomic_number': 71, 'type': 'Lanthanide'},
    {'name': 'Hafnium', 'symbol': 'Hf', 'atomic_number': 72, 'type': 'Transition metal'},
    {'name': 'Tantalum', 'symbol': 'Ta', 'atomic_number': 73, 'type': 'Transition metal'},
    {'name': 'Tungsten', 'symbol': 'W', 'atomic_number': 74, 'type': 'Transition metal'},
    {'name': 'Rhenium', 'symbol': 'Re', 'atomic_number': 75, 'type': 'Transition metal'},
    {'name': 'Osmium', 'symbol': 'Os', 'atomic_number': 76, 'type': 'Transition metal'},
    {'name': 'Iridium', 'symbol': 'Ir', 'atomic_number': 77, 'type': 'Transition metal'},
    {'name': 'Platinum', 'symbol': 'Pt', 'atomic_number': 78, 'type': 'Transition metal'},
    {'name': 'Gold', 'symbol': 'Au', 'atomic_number': 79, 'type': 'Transition metal'},
    {'name': 'Mercury', 'symbol': 'Hg', 'atomic_number': 80, 'type': 'Transition metal'},
    {'name': 'Thallium', 'symbol': 'Tl', 'atomic_number': 81, 'type': 'Post-transition metal'},
    {'name': 'Lead', 'symbol': 'Pb', 'atomic_number': 82, 'type': 'Post-transition metal'},
    {'name': 'Bismuth', 'symbol': 'Bi', 'atomic_number': 83, 'type': 'Post-transition metal'},
    {'name': 'Polonium', 'symbol': 'Po', 'atomic_number': 84, 'type': 'Metalloid'},
    {'name': 'Astatine', 'symbol': 'At', 'atomic_number': 85, 'type': 'Halogen'},
    {'name': 'Radon', 'symbol': 'Rn', 'atomic_number': 86, 'type': 'Noble gas'},
    {'name': 'Francium', 'symbol': 'Fr', 'atomic_number': 87, 'type': 'Alkali metal'},
    {'name': 'Radium', 'symbol': 'Ra', 'atomic_number': 88, 'type': 'Alkaline earth metal'},
    {'name': 'Actinium', 'symbol': 'Ac', 'atomic_number': 89, 'type': 'Actinide'},
    {'name': 'Thorium', 'symbol': 'Th', 'atomic_number': 90, 'type': 'Actinide'},
    {'name': 'Protactinium', 'symbol': 'Pa', 'atomic_number': 91, 'type': 'Actinide'},
    {'name': 'Uranium', 'symbol': 'U', 'atomic_number': 92, 'type': 'Actinide'},
    {'name': 'Neptunium', 'symbol': 'Np', 'atomic_number': 93, 'type': 'Actinide'},
    {'name': 'Plutonium', 'symbol': 'Pu', 'atomic_number': 94, 'type': 'Actinide'},
    {'name': 'Americium', 'symbol': 'Am', 'atomic_number': 95, 'type': 'Actinide'},
    {'name': 'Curium', 'symbol': 'Cm', 'atomic_number': 96, 'type': 'Actinide'},
    {'name': 'Berkelium', 'symbol': 'Bk', 'atomic_number': 97, 'type': 'Actinide'},
    {'name': 'Californium', 'symbol': 'Cf', 'atomic_number': 98, 'type': 'Actinide'},
    {'name': 'Einsteinium', 'symbol': 'Es', 'atomic_number': 99, 'type': 'Actinide'},
    {'name': 'Fermium', 'symbol': 'Fm', 'atomic_number': 100, 'type': 'Actinide'},
    {'name': 'Mendelevium', 'symbol': 'Md', 'atomic_number': 101, 'type': 'Actinide'},
    {'name': 'Nobelium', 'symbol': 'No', 'atomic_number': 102, 'type': 'Actinide'},
    {'name': 'Lawrencium', 'symbol': 'Lr', 'atomic_number': 103, 'type': 'Transition metal'},
    {'name': 'Rutherfordium', 'symbol': 'Rf', 'atomic_number': 104, 'type': 'Transition metal'},
    {'name': 'Dubnium', 'symbol': 'Db', 'atomic_number': 105, 'type': 'Transition metal'},
    {'name': 'Seaborgium', 'symbol': 'Sg', 'atomic_number': 106, 'type': 'Transition metal'},
    {'name': 'Bohrium', 'symbol': 'Bh', 'atomic_number': 107, 'type': 'Transition metal'},
    {'name': 'Hassium', 'symbol': 'Hs', 'atomic_number': 108, 'type': 'Transition metal'},
    {'name': 'Meitnerium', 'symbol': 'Mt', 'atomic_number': 109, 'type': 'Transition metal'},
    {'name': 'Darmstadtium', 'symbol': 'Ds', 'atomic_number': 110, 'type': 'Transition metal'},
    {'name': 'Roentgenium', 'symbol': 'Rg', 'atomic_number': 111, 'type': 'Transition metal'},
    {'name': 'Copernicium', 'symbol': 'Cn', 'atomic_number': 112, 'type': 'Transition metal'},
    {'name': 'Nihonium', 'symbol': 'Nh', 'atomic_number': 113, 'type': 'Post-transition metal'},
    {'name': 'Flerovium', 'symbol': 'Fl', 'atomic_number': 114, 'type': 'Post-transition metal'},
    {'name': 'Moscovium', 'symbol': 'Mc', 'atomic_number': 115, 'type': 'Post-transition metal'},
    {'name': 'Livermorium', 'symbol': 'Lv', 'atomic_number': 116, 'type': 'Post-transition metal'},
    {'name': 'Tennessine', 'symbol': 'Ts', 'atomic_number': 117, 'type': 'Post-transition metal'},
    {'name': 'Oganesson', 'symbol': 'Og', 'atomic_number': 118, 'type': 'Noble gas'}]
element = random.choice(elements)
element_name = element['name']
ask_user = ""
guessing = True
guess_prompt = [
"I believe in you! Make your guess: ", 
"You got this. Whats your guess?: ", 
"Don't waste any time! Let's make a guess!: ", 
"You won't know unless you try. Try making a guess! ", 
"You're gonna get it on this one! Let's guess!: "]
mistakes = 0
max_mistakes = 2


def check_guess(guess):
    global game
    global element_name
    global element_guessed
    global guessing
    global mistakes
    global max_mistakes
    #regular comparison 
    if guess == element_name and guessing == True and element_guessed == False:
        print("\nGood job, you got it!")
        element_guessed = True
        guessing = False
        game = False
    #spell check algorithm
    if len(guess) == len(element_name) and element_guessed == False:
        for i in range(min(len(guess), len(element_name))):
            if guess[i].lower() != element_name[i].lower():
                mistakes += 1
            if mistakes > max_mistakes:
                break
        if mistakes <= max_mistakes:
            print("\nYou're close! Maybe check if your spelling is correct?")
            mistakes = 0
        else:
            mistakes = 0
    if guess != element_name and game == True and guessing == False:
        print("\nThats not quite correct, try again maybe?")

#main guess runtime
def guess_element():
    global game
    global element_name
    global guessing
    global element_guessed
    if game == True and element_guessed == False:
        for i in range (5):
            if i == 0:
                print("\nYour first two hints are:\n  This element is a " + element['type'] + 
                "\n  The name of this element is " + str(len(element_name)) + " letters long\n ")
                check_guess(input(random.choice(guess_prompt)))
            if game == True and i == 1:
                print("\nHint #" + str(i + 1) + "\nThis element has an atomic number of " + str(element['atomic_number']))
                check_guess(input(random.choice(guess_prompt)))
            if game == True and i == 2:
                print("\nHint #" + str(i + 1) + "\nThis element starts with the letter " + element_name[0])
                check_guess(input(random.choice(guess_prompt)))
            if game == True and i == 3:
                print("\nHint #" + str (i + 1) + "\nFinal hint, the symbol for this element is " + element['symbol'])
                check_guess(input(random.choice(guess_prompt)))
            if i == 4 and element_guessed == False:
                print("\nGood try, " + element_name + " was actually the element, maybe you'll have better luck next time!")
                game = False
                guessing = False

#Main Game Loop
def main_loop():
    global game
    while game == True:
        guess_element()
    print("Thanks for playing, have a great day!")

#Starting Prompt
ask_user = input("Welcome to Element Guesser!\n\nA fun guessing game where you use hints in order to figure out the random element!\n\n• You will receive 5 total hints progressively revealing more about the element\n• You will have 4 total attempts to guess the element\n• If you're not sure on the element, press the [Enter] key to get the next hint\n\n[For the best experience, try not to use a periodic table]\n\nWould you like to play? [Yes/No]: ")
if ask_user == "Yes":
    game = True
elif ask_user == "No":
    print("\nThats alright :(")

main_loop()
