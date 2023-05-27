class Employee:
    def __init__(self, name, salary, experience):
        self.name = name
        self.salary = salary
        self.experience = experience

    def get_salary_with_bonus(self):
        bonus = 0

        if self.experience < 1:
            bonus = 0.05  # 5% бонус
        elif self.experience >= 1 and self.experience <= 3:
            bonus = 0.1  # 10% бонус
        else:
            bonus = 0.15  # 15% бонус

        salary_with_bonus = self.salary + (self.salary * bonus)
        return salary_with_bonus
    
    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Salary: {self.salary}\n' \
               f'Expense: {self.experience}\n' \

emp_name = input("Name: ")
emp_salary = float(input("Salary: "))
emp_exp = float(input("Experience: "))
employee = Employee(emp_name, emp_salary, emp_exp)
print(employee)
print(f'Salary with bonus: {employee.get_salary_with_bonus()}')