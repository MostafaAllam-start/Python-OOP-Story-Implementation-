class Car:
    def __init__(self, name, fuelRate, velocity):
        if fuelRate > 0:
            self.fuelRate = fuelRate
        else:
            self.fuelRate = 0
        if 0 < velocity <= 200:
            self.velocity = velocity
        else:
            self.velocity = 0
        self.name = name

    def run(self, newVelocity, distance):
        if newVelocity > 0 and distance > 0:
            if self.fuelRate > 0:
                self.velocity = newVelocity
                print(f"we are move at speed = {self.velocity}.")
                self.fuelRate -= .01 * self.fuelRate * distance
                if self.fuelRate > 0:
                    print('The remaining distance = 0.\nCongratulations you reached your destination!!')
                elif self.fuelRate == 0:
                    print('The remaining distance = 0.\nCongratulations you have reached your destination, but you need to refuel your car!!')
                else:
                    print(f'The remaining distance = {distance - 100}')
                    self.stop()
                    self.fuelRate = 0
            else:
                print('There is not enough fuel to run the car!!')
        elif newVelocity == 0 and distance > 0:
            print('You need to increase the velocity to reach your destination!!')
        else:
            print('Invalid velocity or distance!!')

    def stop(self):
        self.velocity = 0
        print('The car stopped!!')

    def __str__(self):
        return f"Name: {self.name}\nVelocity: {self.velocity}\nFuel Rate: {self.fuelRate}"

