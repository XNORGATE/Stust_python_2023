class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self):
        hours_worked = self.emp_salary / 50
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            salary = self.emp_salary + overtime_amount
        else:
            salary = int(self.emp_salary)
        return salary

    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)

example = Employee("SMITH", "E7698", 55000, "OPERATIONS")
example.emp_assign_department("IT")
example.print_employee_details()
print(example.calculate_emp_salary())