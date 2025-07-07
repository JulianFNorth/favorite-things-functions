import json

def display_favs(favorites):
    return "Your favorites:\n" + "\n".join(f"{cat}: {fav}" for cat, fav in favorites.items())

def type_category(favorites):
    category = ''
    while category not in favorites:
        category = input("What category would you like to input? ")
        if category not in favorites:
            print("Category not available!\n")
    return f"My favorite for this is: {favorites[category]}"

def new_category(favorites):
    choice = ''
    while choice.lower() not in ['y', 'yes', 'n', 'no']:
        choice = input("Would you like to add a new category (y/n)? ")
        if choice.lower() not in ['y', 'yes', 'n', 'no']:
            print("Please enter a valid choice!")
    if choice.lower() in ['y', 'yes']:
        add_category(favorites)

def update_fav(favorites):
    cat = ''
    while cat not in favorites:
        cat = input("What is the category? ")
        if cat not in favorites:
            print("Category not found!\n")

    fav = input("What is your new favorite? ")
    favorites[cat] = fav
    print("Updated!")

def delete_fav(favorites):
    cat = ''
    while cat not in favorites:
        cat = input("What is the category? ")
        if cat not in favorites:
            print("Category not found!\n")

    del favorites[cat]
    print("Deleted!")

def add_category(favorites):
    cat = input("What is your new category? ")
    fav = input("What is your favorite? ")
    if cat in favorites:
        print("Category already exists!")
    else:
        favorites[cat] = fav
    print("\nHere are all your favorites:")
    for cat, fav in favorites.items():
        print(f"{cat}: {fav}")
    return favorites

def main():
    playing = True
    try:
        with open ("favorites.json", "r") as favorites:
            favorites = json.load(favorites)
    except: favorites = {}

    while True:
        print("\nWhat would you like to do?")
        print("Options: lookup / add / update / delete / show / quit")
        choice = input("Enter your choice: ").lower().strip()

        if choice == 'lookup':
            print(type_category(favorites))
        elif choice == 'add':
            new_category(favorites)
        elif choice == 'update':
            update_fav(favorites)
        elif choice == 'delete':
            delete_fav(favorites)
        elif choice == 'show':
            print(display_favs(favorites))
        elif choice == 'quit':
            print("See you later!")
            break
        else:
            print("Invalid option. Please try again.")
    with open ("favorites.json", "w") as file:
        json.dump(favorites, file)

if __name__ == "__main__":
    main()