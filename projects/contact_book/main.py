def show_menu():
    print("==== CONTACT BOOK ====\n")
    print("1. Show contacts\n")
    print("2. Add contact\n")
    print("3. Exit\n")

def get_user_option():
    op = int(input("What would you like to do?\n"))
    while op not in [1,2,3]:
        op = int(input("Wrong option. Type a correct one\n"))
    return op


def add_contact(contacts):
    name = input("Type the name\n")
    phone = input("Type the phone\n")
    email = input("Type the email\n")
    city = input("Type the city\n")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "city": city,
    })


def show_contacts(contacts):
    print("==== CONTACT BOOK ====")
    if not contacts:
        print("No contacts found.")
        return
    
    for contact in contacts:
        print(f"\nName : {contact['name']}")
        print(f"Phone : {contact['phone']}")
        print(f"Email : {contact['email']}")
        print(f"City : {contact['city']}\n")
        print("----------------------------")


def main():
    contacts = [
        {
            "name": "Ana",
            "phone": "600111222",
            "email": "Ana123@gmail.com",
            "city": "London"
        },
        {
            "name": "Luis",
            "phone": "600333444",
            "email": "Luis123@gmail.com",
            "city": "Seville"
        },
        {
        "name": "Marta",
        "phone": "600555666",
        "email": "Marta123@gmail.com",
        "city": "Paris"
        }
    ]
    running  = True
    while running :
        show_menu()
        op = get_user_option()
        match op:
            case 1: 
                show_contacts(contacts)
            case 2:
                add_contact(contacts)
                print("Contact successfully added.")
            case 3: 
                running = False
            case _:
                    print("Something went wrong")

if __name__ == "__main__":
    main()