from person import Person
from car import Car


class Employee(Person):
    salary = 1000

    def __init__(self, name, money, mood, healthRate, Id, car: Car, email, salary, distanceToWork):
        super(Employee, self).__init__(name, money, mood, healthRate)
        self.car = car
        self.email = email
        if salary > 1000:
            self.salary = salary
        self.distanceToWork = distanceToWork
        self.id = Id

    def work(self, hours):
        if hours == 8:
            self.mood = 'Happy'
        elif hours > 8:
            self.mood = 'Tired'
        else:
            self.mood = 'Lazy'

    def drive(self, velocity):
        self.car.run(velocity, self.distanceToWork)

    def refuel(self, gasAmount=100):
        self.car.fuelRate += gasAmount

    def send_mail(self, to, subject, msg, recevier_name):
        _f = open(f'{recevier_name}.txt', 'w')
        massage = f"From: {self.email} \nTo: {to} \n{subject} \n\nHi,{recevier_name}\n{msg}\nThanks"
        _f.write(massage)
        _f.close

    def __str__(self):
        return f"Name: {self.name}\nId: {self.id}\nMoney: {self.money} \nMood: {self.mood}\nHealth Rate: {self.healthRate}\nCar:\n{self.car}\nEmail: {self.email}\nSalary: {self.salary}\nDistance To Work: {self.distanceToWork} "
