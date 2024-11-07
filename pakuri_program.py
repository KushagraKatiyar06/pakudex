from pakudex import Pakudex
from pakuri import Pakuri


def menu():
    print("Pakudex Main Menu")
    print("-" * 17)
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit\n")


def main():
    p = Pakudex()

    print("Welcome to Pakudex: Tracker Extraordinaire!")

    while True:
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
        except ValueError:
            print("Please enter a valid size.")
            capacity = int(input("Enter max capacity of the Pakudex: "))

        if capacity < 1:
            print("Please enter a valid size.")
        else:
            p.capacity = capacity
            print(f"The Pakudex can hold {p.capacity} species of Pakuri.\n")
            break

    while True:
        while True:
            try:
                menu()
                selection = int(input("What would you like to do? "))
                break
            except ValueError:
                print("Unrecognized menu selection!\n")
        print()

        if selection == 1:
            if len(p.all_pakuri) < 1:
                print("No Pakuri in Pakudex yet!\n")
            else:
                species_array = p.get_species_array()
                print("Pakuri In Pakudex:")
                count = 0
                for species in species_array:
                    count += 1
                    print(f"{count}. {species}")
                print()

        elif selection == 2:
            species = input("Enter the name of the species to display: ")
            species_list = p.get_species_array()

            if len(p.all_pakuri) > 0:
                if species in species_list:
                    for pakuri in p.all_pakuri:
                        if pakuri.get_species() == species:
                            stats = p.get_stats(species)
                            print(f"Species: {species}")
                            print(f"Attack: {stats[0]}")
                            print(f"Defense: {stats[1]}")
                            print(f"Speed: {stats[2]}\n")
                else:
                    print("Error: No such Pakuri!\n")
            else:
                print("Error: No such Pakuri!\n")


        elif selection == 3:
            if p.pakuri_count >= p.capacity:
                print("Error: Pakudex is full!\n")
            else:
                species = input("Enter the name of the species to add: ")
                if any(pakuri.species == species for pakuri in p.all_pakuri):
                    print("Error: Pakudex already contains this species!\n")
                else:
                    p.add_pakuri(species)
                    print(f"Pakuri species {species} successfully added!\n")

        elif selection == 4:
            species = input("Enter the name of the species to evolve: ")
            species_list = p.get_species_array()
            if len(p.all_pakuri) > 0:
                if species in species_list:
                    p.evolve_species(species)
                    print(f"{species} has evolved!\n")
                else:
                    print("Error: No such Pakuri!\n")
            else:
                print("Error: No such Pakuri!\n")


        elif selection == 5:
            p.sort_pakuri()
            print("Pakuri have been sorted!\n")

        elif selection == 6:
            print("Thanks for using Pakudex! Bye!")
            break

        else:
            print("Unrecognized menu selection!")


if __name__ == "__main__":
    main()


