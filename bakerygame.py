breads = [["Basic Loaves", 1], ["French Baguette", 2], ["Sourdough", 5]]
pastries = [["Basic Pastries", 1]]

class Bakery:
    def __init__(self, name):
        self.name = name
        print(f"\n{self.name}, now open for business!\n")
        self.menu = []

class Baker:
    def __init__(self, name):
        self.name = name
        print(f"\nNew baker, named {self.name}, reporting for duty!\n")
        self.skills = {"Bread": 5, "Pastries": 1}

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
        print("What do you want to make?\n")
        while len(planned_items) < 8:
            running2 = 1
            for skill in baker.skills:
                print(f"{running2}. {skill}")
                running2 += 1
            print()
            try:
                your_choice2 = int(input("Choice: "))
            except ValueError:
                print("Invalid choice")
                continue
            print()
            if your_choice2 == 1:
                print("Which bread?\n")
                running4 = 1
                sketchy2 = []
                for bread_opt in breads:
                    if baker.skills["Bread"] >= bread_opt[1]:
                        print(f"{running4}. {bread_opt[0]}")
                        sketchy2.append(bread_opt[0])
                        running4 += 1
                your_choice5 = int(input("\nChoice: ")) - 1
                print(f"\nAdded {sketchy2[your_choice5]} to the menu.\n")
                planned_items.append(sketchy2[your_choice5])
            elif your_choice2 == 2:
                #print(pastries)
                #print()
                #planned_items.append(pastries[0])
                print("Which pastries?\n")
                running5 = 1
                sketchy3 = []
                for pastry_opt in pastries:
                    if baker.skills["Pastries"] >= pastry_opt[1]:
                        print(f"{running5}. {pastry_opt[0]}")
                        sketchy3.append(pastry_opt[0])
                        running5 += 1
                your_choice6 = int(input("\nChoice: ")) - 1
                print(f"\nAdded {sketchy3[your_choice6]} to the menu.\n")
                planned_items.append(sketchy3[your_choice6])
            else:
                print("Invalid choice")
        #print(planned_items)
        bakery.menu = planned_items
        print("The new menu is:\n")
        print(bakery.menu)
        print()
        if "Run the bakery" not in possible_actions:
            possible_actions.insert(0, "Run the bakery")
    elif action_chosen == "Attend bakery school":
        print("What would you like to do?\n\n1. Learn a new skill\n2. Practice a known skill\n")
        your_choice3 = int(input("Choice: "))
        print()
        if your_choice3 == 1:
            print("Sorry, this has not yet been implemented\n")
        elif your_choice3 == 2:
            running3 = 1
            sketchy = []
            for skill2 in baker.skills:
                print(f"{running3}. {skill2}")
                sketchy.append(skill2)
                running3 += 1
            print()
            your_choice4 = int(input("Choice: "))
            print(f"\nYou learned about {sketchy[your_choice4 - 1]}\n")
            baker.skills[sketchy[your_choice4 - 1]] += 1
            print(baker.skills)
            print()
            
    elif action_chosen == "Run the bakery":
        print(bakery.menu)
        print()
    elif action_chosen == "Exit":
        ongoing = False
