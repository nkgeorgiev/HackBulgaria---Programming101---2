import unittest
from Employee import Employee, HourlyEmployee, SalariedEmployee, Manager


class EmployeeTest(unittest.TestCase):
    def test_employee_init_and_get_name(self):
        employee = Employee("test")
        self.assertEqual("test", employee.name)
        self.assertEqual("test", employee.getName())

    def test_hourly_employee_init(self):
        he = HourlyEmployee("test", 10)
        self.assertEqual("test", he.getName())
        self.assertEqual(10, he.hourly_wage)

    def test_hourly_employee_weeklyPay(self):
        he = HourlyEmployee("test", 1)
        self.assertEqual(30.0, he.weeklyPay(30))
        self.assertAlmostEqual(55.0, he.weeklyPay(50))

    def test_salaried_employee_init(self):
        se = SalariedEmployee("test", 52000.0)
        self.assertEqual("test", se.getName())
        self.assertAlmostEqual(52000.0, se.annual_salary)

    def test_salaried_employee_weeklyPay(self):
        se = SalariedEmployee("test", 52000.0)
        self.assertAlmostEqual(1000.0, se.weeklyPay(40))

    def test_manager_init(self):
        manager = Manager("test", 52000.0, 50.0)
        self.assertEqual("test", manager.getName())
        self.assertAlmostEqual(52000.0, manager.annual_salary)
        self.assertAlmostEqual(50.0, manager.weekly_bonus)

    def test_manager_weeklyPay(self):
        manager = Manager("test", 52000.0, 50.0)
        self.assertAlmostEqual(1050.0, manager.weeklyPay(40))

if __name__ == '__main__':
    unittest.main()
