class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

def sort_employee_data(employees, sorting_param):
    if sorting_param == 1:
        employees.sort(key=lambda emp: emp.age)
    elif sorting_param == 2:
        employees.sort(key=lambda emp: emp.name)
    elif sorting_param == 3:
        employees.sort(key=lambda emp: emp.salary)
    else:
        print("Invalid sorting parameter.")

def print_employee_data(employees):
    print("Employee ID\tName\tAge\tSalary")
    print("-------------------------------------")
    for emp in employees:
        print(f"{emp.emp_id}\t\t{emp.name}\t{emp.age}\t{emp.salary}")

def main():
    emp1 = Employee("161E90", "Raman", 41, 56000)
    emp2 = Employee("161F91", "Himadri", 38, 67500)
    emp3 = Employee("161F99", "Jaya", 51, 82100)
    emp4 = Employee("171E20", "Tejas", 30, 55000)
    emp5 = Employee("171G30", "Ajay", 45, 44000)

    employees = [emp1, emp2, emp3, emp4, emp5]

    print("Sorting Options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    sorting_param = int(input("Enter the sorting parameter: "))
    sort_employee_data(employees, sorting_param)
    print_employee_data(employees)

if __name__ == "__main__":
    main()
