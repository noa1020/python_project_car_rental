from Vehicles import VehiclesMenu
from datetime import datetime
from Payment import Payment

payment = Payment()


class Rentals:
    def __init__(self):
        self.carCount = {
            "car": 1,
            "minibus": 10,
            "motorcycle": 40,
        }
        self.userDetailsByVehicles = {
            "car": {},
            "minibus": {},
            "motorcycle": {}
        }

    def IsAvailable(self, carName):
        """Checking whether the requested vehicle is available"""
        if self.carCount[carName] > 0:
            return True
        return False

    def get_items(self):
        """Returns a list of the names of the existing vehicles"""
        available_items = []
        for item in VehiclesMenu().cars:
            if self.IsAvailable(item.name):
                available_items.append(item.name)
        return available_items

    def taking(self):
        """taking a vehicle"""
        items = "/".join(self.get_items())
        selectedCar = input(f"We currently have in stock:{items} what would you like?")
        try:
            self.IsAvailable(selectedCar)
            idNumber = input("please enter your ID number")
            name = input("please enter your name")
            currentTime = datetime.now()
            self.userDetailsByVehicles[selectedCar][idNumber] = [name, currentTime]
            vehicle = VehiclesMenu().find_car(selectedCar)
            if hasattr(vehicle, 'helmet'):
                print(f"❤️ that the motorcycle comes with {vehicle.helmet} helmets, make sure to return them")
            print("Your order has been accepted, have a nice trip and have a good day!✋")
            self.carCount[selectedCar] -= 1
        except:
            print("the vehicle is not available🥲")

    def returning(self):
        """vehicle return"""
        selectedCar = input("Which vehicle would you like to return?(car/minibus/motorcycle)")
        idNumber = input("please enter your ID number")
        try:
            vehicle = VehiclesMenu().find_car(selectedCar)
            user = self.userDetailsByVehicles[selectedCar][idNumber]
            print(f"💙hello {user[0]} Hope you had a safe trip🤍")
            time_difference = int((datetime.now() - user[1]).total_seconds() / 60)
            payment.MakePayment(vehicle.cost, time_difference)
            self.userDetailsByVehicles[selectedCar].pop(idNumber)
            self.carCount[selectedCar] += 1
        except:
            print("not fount")

    def report(self):
        """Report which vehicles are available in stock"""
        for k, v in self.carCount.items():
            print(f"Vehicle: {k} has: {v} items in stock")

    def Profit(self):
        """Prints the current profit"""
        print(f"Profit: {payment.CURRENCY}{payment.profit}")
