# 1. Base Class (Abstraction & Encapsulation)
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.__emp_id = emp_id          # Private
        self._name = name               # Protected
        self._basic_salary = basic_salary

    def get_details(self):
        return f"{self.__emp_id} | {self._name}"

    def calculate_salary(self):
        pass # To be overridden

# 2. Derived Classes (Inheritance & Polymorphism)
class PermanentEmployee(Employee):
    def __init__(self, emp_id, name, basic_salary, bonus):
        super().__init__(emp_id, name, basic_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self._basic_salary + self.bonus

class ContractEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours):
        super().__init__(emp_id, name, hourly_rate)
        self.hours = hours

    def calculate_salary(self):
        return self._basic_salary * self.hours

# 3. Payroll System (Management)
class PayrollSystem:
    def show_payroll(self, employees):
        for emp in employees:
            print(f"Employee: {emp.get_details()} | Salary: ${emp.calculate_salary()}")

# --- Main Program ---
# Creating objects
emp1 = PermanentEmployee(1, "Alice", 5000, 500)
emp2 = ContractEmployee(2, "Bob", 50, 160)

# Demonstrating Runtime Polymorphism
staff = [emp1, emp2]
payroll = PayrollSystem()
payroll.show_payroll(staff)