class Employee:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def weeklyPay(self, hours):
        pass


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_wage):
        Employee.__init__(self, name)
        self.hourly_wage = hourly_wage

    def weeklyPay(self, hours):
        wage = 0.0
        if hours > 40:
            wage += 40 * self.hourly_wage
            hours -= 40
            wage += 1.5 * hours * self.hourly_wage
        return wage


class SalariedEmployee(Employee):
    def __init__(self, name, annual_salary):
        Employee.__init__(self, name)
        self.annual_salary = annual_salary

    def weeklyPay(self, hours):
        return self.annual_salary / 52


class Manager(Employee):
    def __init__(self, name, annual_salary, weekly_bonus):
        Employee.__init__(self, name)
        self.annual_salary = annual_salary
        self.weekly_bonus = weekly_bonus

    def weeklyPay(self, hours):
        return self.annual_salary / 52 + self.weekly_bonus

staff = []
staff.append(HourlyEmployee("Morgan, Harry", 30.0))
staff.append(SalariedEmployee("Lin, Sally", 52000.0))
staff.append(Manager("Smith, Mary", 104000.0, 50.0))
for employee in staff:
    hours = int(input("Hours worked by " + employee.getName() + ": "))
    pay = employee.weeklyPay(hours)
    print("Salary: %.2f" % pay)
