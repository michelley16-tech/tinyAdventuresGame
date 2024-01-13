import time


def print_slow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


# tinyAdventureGame Python code


def get_input(options):
    while True:
        choice = input(">> ").strip().lower()
        if choice in options:
            return choice
        print("Invalid choice. Try again.")


def intro():
    print_slow("Welcome to the Tiny Adventure Game!")
    print_slow("You find yourself in a mysterious castle.")
    print_slow("Your goal is to find the treasure hidden deep within the castle.")
    print_slow("Choose your actions wisely, as your decisions will shape your destiny!")


def room_one():
    print_slow("You enter a dark room with two doors.")
    print_slow("One door is on your left, and the other is on your right.")
    print_slow("Which door do you choose? (left/right)")

    choice = get_input(['left', 'right'])

    if choice == 'left':
        print_slow("You chose the left door.")
        room_two()
    else:
        print_slow("You chose the right door.")
        room_three()


def room_two():
    print_slow("You find a room filled with treasure!")
    print_slow("Congratulations! You have found the hidden treasure!")
    print_slow("You win!")


def room_three():
    print_slow("You enter a room with a giant sleeping dragon.")
    print_slow("The dragon wakes up and breathes fire at you!")
    print_slow("What do you do? (fight/escape)")

    choice = get_input(['fight', 'escape'])

    if choice == 'fight':
        print_slow("You try to fight the dragon, but you are no match for its power.")
        print_slow("Game over!")
    else:
        print_slow("You wisely choose to escape from the room.")
        room_one()


def main():
    intro()
    room_one()


if __name__ == "__main__":
    main()
