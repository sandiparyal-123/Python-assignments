#MANAGER ,PERSON , EMPLOYEE - 3 classes. employee inherits from person. manager inherits from person and employee. add additional behaviours in manager
"""
Person - name and age
Employee - id + slaary
manager - department 
"""
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_person(self):
        print (f"Name:          {self.name} \nAge:          {self.age}")

class employee(person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee(self):
        super().display_person()
        print (f"Employee ID:   {self.employee_id} \nSalary:        {self.salary}")

class manager(employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display_manager(self):
        super().display_employee()
        print (f"Department:    {self.department}")

while True:
    print ("Choose and option: \n1. Create Person. \n2. Create employee. \n3. Create manager. \n4. Exit program.")
    choice = int(input("Enter Your Choice:  "))

    if choice == 1:
        name = input("Enter name:   ")
        age = int(input("Enter age:     "))
        p1= person(name ,age)
        print("\nPerson Details are:")
        p1.display_person()

    elif choice == 2:
        name = input("Enter name:   ")
        age = int(input("Enter age:     "))
        id = int(input("enter Employee ID:      "))
        salary  = float(input("Enter salary:     "))
        p2= employee(name ,age, id, salary)
        print("\Employee Details are:")
        p2.display_employee()
    
    elif choice == 3:
        name = input("Enter name:   ")
        age = int(input("Enter age:     "))
        id = int(input("enter Employee ID:      "))
        salary  = float(input("Enter salary:     "))
        department = (input("Enter Department:      "))
        p3= manager(name ,age, id, salary , department)
        print("\nManager Details are:")
        p3.display_manager()

    elif choice == 4:
        print ("Goodbye.")
        break
    else:
        print ("Invalid Input, try again.")