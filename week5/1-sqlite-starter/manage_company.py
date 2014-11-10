import sqlite3


class Company:
    def __init__(self):
        self.db = sqlite3.connect("company.db")
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()

    def list_employees(self):
        result = self.cursor.execute(''' SELECT id, name, position from employees''')
        for row in result:
            print("{} - {} - {}".format(row["id"], row["name"], row["position"]))

    def montly_spending(self):
        result = self.cursor.execute(''' SELECT montly_salary from employees''')
        montly_spending = 0
        for i in result:
            montly_spending += i["montly_salary"]
        print("The company is spending ${} every month!".format(montly_spending))

    def yearly_spending(self):
        result = self.cursor.execute(''' SELECT montly_salary, yearly_bonus from employees''')
        yearly_spending = 0
        for i in result:
            yearly_spending += 12 * i["montly_salary"] + i["yearly_bonus"]
        print("The company is spending ${} every year!".format(yearly_spending))

    def add_employee(self):
        name = input("name> ")
        montly_salary = input("montly_salary> ")
        yearly_bonus = input("yearly_bonus> ")
        position = input("position> ")
        self.cursor.execute('''INSERT INTO employees(name, montly_salary, yearly_bonus, position)
                  VALUES(?,?,?,?)''', (name, montly_salary, yearly_bonus, position))
        self.db.commit()

    def delete_employee(self, id):
        self.cursor.execute(''' DELETE FROM employees WHERE id = ? ''', (id,))
        self.db.commit()

    def update_employee(self, id):
        name = input("name> ")
        montly_salary = input("montly_salary> ")
        yearly_bonus = input("yearly_bonus> ")
        position = input("position> ")
        self.cursor.execute('''UPDATE employees SET name = ?, montly_salary = ?,
         yearly_bonus = ?, position = ? WHERE id = ?
                  ''', (name, montly_salary, yearly_bonus, position, id))
        self.db.commit()

    def menu(self):
        command = input("Enter command> ").split()
        while command[0] != "Exit":
            if command[0] == "list_employees":
                self.list_employees()
            elif command[0] == "montly_spending":
                self.montly_spending()
            elif command[0] == "yearly_spending":
                self.yearly_spending()
            elif command[0] == "add_employee":
                self.add_employee()
            elif command[0] == "delete_employee" and len(command) >= 2:
                self.delete_employee(command[1])
            elif command[0] == "update_employee" and len(command) >= 2:
                self.update_employee(command[1])
            elif command[0] == "list":
                print(" list_employees\n montly_spending\n yearly_spending\n add_employee\n delete_employee\n update_employee\n list\n Exit")
            else:
                print("Command does not exist!!")
            command = input("Enter command> ").split()

comp = Company()
comp.menu()
