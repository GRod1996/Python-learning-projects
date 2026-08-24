# Create a dictionary (beginner)
shop_inventory = {"guitars": 2, "drums": 1, "bass": 3}


def main():
    print("Welcome to the music shop! We sell guitars, drums and bass.")

    user_input = input("\nWhat instrument are you looking for?\n").strip().lower()
    for key in shop_inventory:
        if user_input == key:
            print(f"\nI have {shop_inventory[key]} {key} available.")


main()
