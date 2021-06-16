class employee:

    def __init__(self,name,age, salary):
        self.name=name
        self.age=age
        self.salary=salary

    def show(self):
        print("name of employe", self.name)
        print("age of employee is ",self.age)
        print("salary of employee is ",self.salary)


e1=employee("shubham",25,2500000000)
e1.show()