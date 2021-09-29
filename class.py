class Employee:

    def __init__(self,name,id,salary,dept):
        self.name=name
        self.id= id
        self.salary = salary
        self.dept = dept

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)



emp1=Employee("ruchitha",20512,30000,"delivery operarions")
emp1.displayEmployee()



