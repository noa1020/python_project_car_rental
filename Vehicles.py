class Vehicles:
    def __init__(self, name, Seats, cost):
        self.name = name
        self.numberOfSeats = Seats
        self.cost = cost


class Motorcycle(Vehicles):
    def __init__(self, name, Seats, cost):
        Vehicles.__init__(self, name, Seats, cost)
        self.helmet = 2


class VehiclesMenu:

    def __init__(self):
        self.pricesDict = {}
        with open('car-prices.txt') as carPrices:
            for line in carPrices.readlines():
                parts = line.split(":")
                vehicle = parts[0]
                price = int(parts[1])
                self.pricesDict[vehicle] = price
        self.cars = [
            Vehicles("car", 5, self.pricesDict["car"]),
            Vehicles("minibus", 12, self.pricesDict["minibus"]),
            Motorcycle("motorcycle", 1, self.pricesDict["motorcycle"])
        ]

    def Manager(self, increase):
        """Multiply all prices by a certain amount"""
        self.cars = [Vehicles(car.name, car.numberOfSeats, float(car.cost) * float(increase)) for car in self.cars
                     if car.name != "motorcycle"]
        self.cars.append(Motorcycle("motorcycle", 1, float(self.pricesDict["motorcycle"]) * float(increase)))

    def find_car(self, order_name):
        """Returning the Vehicle object by its name"""
        for item in self.cars:
            if item.name == order_name:
                return item
        return None

    def Report(self):
        """Printing the catalog"""
        for car in self.cars:
            print(f"vehicle: {car.name}, numer of seats: {car.numberOfSeats}, price:{car.cost}")
