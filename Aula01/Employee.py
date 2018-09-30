class Employee():
    # in this case the only param obrigatorio is the employeeName
    def __init__(self, employeeName, taxDeductions=1, maritalStatus="single"):
        self.employeeName = employeeName
        self.taxDeductions = taxDeductions
        self.maritalStatus = maritalStatus

    def __str__(self):
        return "{0},{2},{1}".format(self.employeeName, self.taxDeductions, self.maritalStatus)


x = Employee("J")
y = Employee("M", 2)
z = Employee("Ma", maritalStatus="married")
for p in [x, y, z]:
    print("{0},{2},{1}".format(p.employeeName, p.taxDeductions, p.maritalStatus))

x.taxDeductions = 3
for p in [x, y, z]:
    print(p)
