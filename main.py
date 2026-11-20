import json
contacts = {}
run = True
name = ""
phone = 0

help_prompt = "add - adds a new contact in NAME PHONENUMBER format\nfind - find a contact via name \nshow - show all contacts\nhelp - reprints the commands like above"
def get_contacts():
    """Henter kontaktoplysningerne fra 'contacts.json'
    """
    global contacts
    with open('contacts.json', 'r') as f:
        contacts = json.load(f)
        return contacts
    
def add_contact():
    """Tager et input som er mellemrumssepareret ved navn og nummer. 
        
       Nummeret må gerne have mellemrum, men ikke landkoder.
       Mellemrummet af tallene fjernes og gemmes i en JSON fil.
    """
    info = input("name and number: ").split()
    name = info[0].lower()
    info.pop(0)
    phone = "".join(info)
    try:
        int(phone)
        if len(phone) == 8:
            contacts[name] = phone
            with open("contacts.json", "w") as f:
                json.dump(contacts, f)
            print(f"Contact {name} has been added as {phone}.")

        elif len(phone) != 8:
            print(f'{phone} is invald\nnumbers must be 8 digits') 
    except:
        print("phone numbers must be integer(s)")


def find_contact():
    """Finder telefonnummeret af en person. Første navn kræves kun.

       Dette betyder at flere brugere kan ikke have samme navn, så
       eventuelt brug denne funktion til at finde brugernavne kun. 

    """
    contacts = get_contacts()
    person = input("type name").lower()
    if person in contacts:
        print(f"{person}'s phone number is: {contacts[person]}")
    else:
        print("person could not be found")

def show_contacts():
    """Printer kontakterne ud gennem get_contacts() i formatet [rækkefølge]. [bruger]: [nummer]
    """
    i = 0
    contacts = get_contacts()
    for name in contacts:
        i += 1
        print(f"{i}. {name}: {contacts[name]}")

def exit():
    """Afslutter programmet ved at lukke while-lykken
    """
    global run
    
    run = False

commands = {
"add":add_contact,
"find":find_contact,
"show":show_contacts,
"exit":exit,
"help": lambda: print(help_prompt)
}

print("type your command")

while run:
    command = input()
    try:
        commands[command]()
    except:
        print("command does not exist.\ntry 'help' for help. ")
print("process ended")
    
