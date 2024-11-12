import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.energy = 50

    def play(self):
        if self.energy >= 10:
            self.happiness += 10
            self.energy -= 10
            print(f"{self.name} is playing! Happiness: {self.happiness}, Energy: {self.energy}")
        else:
            print(f"{self.name} is too tired to play.")

    def feed(self):
        self.energy += 20
        print(f"{self.name} has been fed! Energy: {self.energy}")

    def sleep(self):
        self.energy = 100
        print(f"{self.name} is sleeping. Energy restored to {self.energy}.")

def main():
    cat_name = input("Enter your cat's name: ")
    my_cat = Cat(cat_name)

    actions = {
        '1': my_cat.play,
        '2': my_cat.feed,
        '3': my_cat.sleep
    }

    while True:
        print("\nChoose an action:")
        print("1. Play")
        print("2. Feed")
        print("3. Sleep")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice in actions:
            actions[choice]()
        elif choice == '4':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
