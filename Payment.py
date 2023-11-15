multiplication = lambda x, y: x * y


class Payment:
    def __init__(self):
        self.profit = 0
        self.CURRENCY = "₪"
    def MakePayment(self, costCar, minutes):
        """Calculation of the amount required for payment and checking of correct income of money"""
        try:
            cost = int(multiplication(costCar, minutes)) / 60
            cost = round(cost, 2)
            self.profit += cost
            print(f"The amount to be paid is {self.CURRENCY}{cost}")
            total = float(input("Please insert money"))
            total = round(total, 2)
            while total < cost:
                total += int(input(f"insert more {round(cost - total, 2)} money😒"))
            if total > cost:
                print(f"take change {self.CURRENCY}{-1 * round(cost - total, 2)}")
            print("Thank you and goodbye! We would love to see you again!😘")

        except:
            print("There is no need to pay to take the vehicle for at least a minute")
