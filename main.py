from Rentals import Rentals
from Vehicles import VehiclesMenu
vehiclesMenu = VehiclesMenu()
rentals = Rentals()
off = True
while off:
    print("🎉Welcome to the Vehicles Rental!🎉")
    chosen = input("press:\n1 for taking \n2 for returning\n3 for change prices \n4 for menu\n5 for display profit\n"
                   "6 for display stock \n7 for turn off the machine")
    if chosen == '1':
        rentals.taking()
    elif chosen == '2':
        rentals.returning()
    elif chosen == '3':
        vehiclesMenu.Manager(float(input("Enter the price increase percentage (for example 1.1)")))
    elif chosen == '4':
        vehiclesMenu.Report()
    elif chosen == '5':
        rentals.Profit()
    elif chosen == '6':
        rentals.report()
    elif chosen == '7':
        off = False
        print("good bye 😴😴😴")

