class Office:
    name = 'ITI'
    employeesNum = 0

    def __init__(self, name, employees):
        self.name = name
        self.employees = employees
        Office.employeesNum += len(employees)

    def get_all_employees(self):
        return [str(i) for i in self.employees]

    def hire(self, employee):
        self.employees.append(employee)
        Office.change_emps_num(1)

    def fire(self, empId):
        for i in range(len(self.employees)):
            if self.employees[i].id == empId:
                self.employees.pop(i)
                Office.change_emps_num(-1)
                break

    def get_employee(self, empId):
        for i in self.employees:
            if i.id == empId:
                return i

    def deduct(self, empId, deduction):
        for i in range(len(self.employees)):
            if self.employees[i].id == empId:
                self.employees[i].salary -= deduction
                break

    def reward(self, empId, reward):
        for i in range(len(self.employees)):
            if self.employees[i].id == empId:
                self.employees[i].salary += reward
                break

    def check_lateness(self, empId, moveHour):
        for i in range(len(self.employees)):
            if self.employees[i].id == empId:
                if Office.calculate_lateness(9, moveHour, self.employees[i].distanceToWork,
                                             self.employees[i].car.velocity):
                    print(f"{self.employees[i].name} is late deduce 10 from his salary!!")
                    self.deduct(empId, 10)
                else:
                    print(f"{self.employees[i].name} is not late reward him with adding 10 to his salary!!")
                    self.reward(empId, 10)
                break

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        return 0 if targetHour - (moveHour + (distance / velocity)) >= 0 else 1

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum += num

    def __str__(self):
        s = "Office Name: " + str(self.name) + '\n' + "Employees'Data:\n\n"
        for i in self.employees:
            s = s + str(i) + '\n---------------\n'
        return s

