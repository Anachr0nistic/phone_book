import json
contacts = {}
run = True
name = ""
phone = 0

help_prompt = "add - adds a new contact in NAME PHONENUMBER format\nfind - find a contact via name \nshow - show all contacts\nhelp - reprints the commands like above"
def get_contacts():
    global contacts
    with open('contacts.json', 'r') as f:
        contacts = json.load(f)
        return contacts
    
def add_contact():
    info = input("name and number: ").split()
    name = info[0]
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
    person = input("type name")
    if person in contacts:
        print(f"{person}'s phone number is: {contacts[person]}")
    else:
        print("person could not be found")

def show_contacts():
    global contacts
    contacts = get_contacts()
    for name in contacts:
        print(f"name: {contacts[name]}")

def exit():
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
    
