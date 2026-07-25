###############
###
###     "Run the Bakery!"
###
###     A game loosely based on the "Build a Food Ordering App"
###     and "Garden Simulator Text Based Game" projects from Dataquest's
###     "Fundamentals of Python and Generative AI" Skill Path
###
###############



breads = [["Basic Loaves", 1], ["French Baguette", 2], ["Sourdough", 5]]
pies = [["Basic Pies", 1], ["Fruit Pies", 2], ["Key Lime Pies", 2], ["Lemon Meringue Pies", 3]]
cakes = [["Basic Cakes", 1], ["Cheesecakes", 4]]
pastries = [["Basic Pastries", 1], ["Fruit Pastries", 2], ["Nut Pastries", 4], ["Croissants", 5]]

class Bakery:
    def __init__(self, name):
        self.name = name
        print(f"\n{self.name}, now open for business!\n")
        self.menu = []

class Baker:
    def __init__(self, name):
        self.name = name
        print(f"\nNew baker, named {self.name}, reporting for duty!\n")
        self.skills = {"Bread": 5, "Pies": 1}

print("Welcome to Run the Bakery!\n")

b1name = input("What is your name? ")

baker = Baker(b1name)

b2name = input("What is your bakery's name? ")

bakery = Bakery(b2name)

ongoing = True

possible_actions = ["Attend bakery school", "Plan a new menu", "Exit"]

while ongoing:
    print("What do you want to do today?\n")
    running = 1
    for action in possible_actions:
        print(f"{running}. {action}")
        running += 1
    print()
    try:
        your_choice = int(input("Choice: "))
    except ValueError:
        print("Invalid choice")
        continue
    print()
    action_chosen = possible_actions[your_choice - 1]
    print(action_chosen)
    print()
    if action_chosen == "Plan a new menu":
        planned_items = []
        planned_items_dict = {}
        print("What do you want to make?\n")
        while len(planned_items) < 8:
            running2 = 1
            sketchy4 = []
            for skill in baker.skills:
                print(f"{running2}. {skill}")
                sketchy4.append(skill)
                running2 += 1
            print()
            try:
                your_choice2 = int(input("Choice: "))
            except ValueError:
                print("Invalid choice")
                continue
            print()
            if sketchy4[your_choice2 - 1] == "Bread":
                print("Which bread?\n")
                running4 = 1
                sketchy2 = []
                for bread_opt in breads:
                    if baker.skills["Bread"] >= bread_opt[1]:
                        print(f"{running4}. {bread_opt[0]}")
                        sketchy2.append(bread_opt[0])
                        running4 += 1
                try:
                    your_choice5 = int(input("\nChoice: ")) - 1
                except ValueError:
                    print("Invalid choice")                    
                try:
                    print(f"\nAdded {sketchy2[your_choice5]} to the menu.\n")
                    planned_items.append(sketchy2[your_choice5])
                    if sketchy2[your_choice5] in planned_items_dict:
                        planned_items_dict[sketchy2[your_choice5]] += 1
                    else:
                        planned_items_dict[sketchy2[your_choice5]] = 1
                except IndexError:
                    print("Invalid choice")
                #print(planned_items_dict)
            elif sketchy4[your_choice2 - 1] == "Pies":
                print("Which pies?\n")
                running5 = 1
                sketchy3 = []
                for pie_opt in pies:
                    if baker.skills["Pies"] >= pie_opt[1]:
                        print(f"{running5}. {pie_opt[0]}")
                        sketchy3.append(pie_opt[0])
                        running5 += 1
                your_choice6 = int(input("\nChoice: ")) - 1
                try:
                    print(f"\nAdded {sketchy3[your_choice6]} to the menu.\n")
                    planned_items.append(sketchy3[your_choice6])
                    if sketchy3[your_choice6] in planned_items_dict:
                        planned_items_dict[sketchy3[your_choice6]] += 1
                    else:
                        planned_items_dict[sketchy3[your_choice6]] = 1
                except IndexError:
                    print("Invalid choice")
            elif sketchy4[your_choice2 - 1] == "Cakes":
                print("Which cakes?\n")
                running6 = 1
                sketchy5 = []
                for cake_opt in cakes:
                    if baker.skills["Cakes"] >= cake_opt[1]:
                        print(f"{running6}. {cake_opt[0]}")
                        sketchy5.append(cake_opt[0])
                        running6 += 1
                your_choice8 = int(input("\nChoice: ")) - 1
                try:
                    planned_items.append(sketchy5[your_choice8])
                    if sketchy5[your_choice8] in planned_items_dict:
                        planned_items_dict[sketchy5[your_choice8]] += 1
                    else:
                        planned_items_dict[sketchy5[your_choice8]] = 1
                    print(f"\nAdded {sketchy5[your_choice8]} to the menu.\n")
                except IndexError:
                    print("Invalid choice")
            elif sketchy4[your_choice2 - 1] == "Pastries":
                print("Which pastries?\n")
                running8 = 1
                sketchy7 = []
                for pastry_opt in pastries:
                    if baker.skills["Pastries"] >= pastry_opt[1]:
                        print(f"{running8}. {pastry_opt[0]}")
                        sketchy7.append(pastry_opt[0])
                        running8 += 1
                your_choice9 = int(input("\nChoice: ")) - 1
                try:
                    planned_items.append(sketchy7[your_choice9])
                    if sketchy7[your_choice9] in planned_items_dict:
                        planned_items_dict[sketchy7[your_choice9]] += 1
                    else:
                        planned_items_dict[sketchy7[your_choice9]] = 1
                    print(f"\nAdded {sketchy7[your_choice9]} to the menu.\n")
                except IndexError:
                    print("Invalid choice")
            else:
                print("Invalid choice")
        bakery.menu = planned_items_dict
        print("The new menu is:\n")
        print(bakery.menu)
        #print(planned_items_dict)
        print()
        if "Run the bakery" not in possible_actions:
            possible_actions.insert(0, "Run the bakery")
    elif action_chosen == "Attend bakery school":
        print("What would you like to do?\n\n1. Learn a new skill\n2. Practice a known skill\n")
        your_choice3 = int(input("Choice: "))
        print()
        if your_choice3 == 1:
            running7 = 1
            sketchy6 = []
            newskills = ["Cakes", "Pastries"]
            print("Skills to choose from:\n")
            for skill3 in newskills:
                if skill3 not in baker.skills:
                    print(f"{running7}. {skill3}")
                    sketchy6.append(skill3)
                    running7 += 1
            if running7 == 1:
                print("Sorry, there are no new skills available.\n")
            else:
                your_choice7 = int(input("\nChoice: ")) - 1
                #print(your_choice7)
                baker.skills[sketchy6[your_choice7]] = 1
                print(f"\nYou learned {sketchy6[your_choice7]}.")
                print()
        elif your_choice3 == 2:
            running3 = 1
            sketchy = []
            for skill2 in baker.skills:
                print(f"{running3}. {skill2}")
                sketchy.append(skill2)
                running3 += 1
            print()
            your_choice4 = int(input("Choice: "))
            try:
                baker.skills[sketchy[your_choice4 - 1]] += 1
                print(f"\nYou learned about {sketchy[your_choice4 - 1]}\n")
            except IndexError:
                print("\nInvalid choice\n")
            print(baker.skills)
            print()
        else:
            print("Invalid choice\n")
            
    elif action_chosen == "Run the bakery":
        print(bakery.menu)
        print()
    elif action_chosen == "Exit":
        ongoing = False
