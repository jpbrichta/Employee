#Employee class example
#JP Brichta 2018

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayEmployee(self):
      print ("Name : " + self.name + ", Salary: " + str(self.salary))
      
#---- Main part of code ----
empList = [] #an empty list

done = 1 #counter variable for while loop

while(done > 0):
  tempEmp = Employee(input('Enter the employee name: '), int(input('Enter the employee salary (enter 0 when done): ')))
  if tempEmp.salary == 0:
    done = 0
    Employee.empCount -= 1
  else:
    empList.append(tempEmp) #adds the Employee to the Employee list
  
for i in range(len(empList)):
  empList[i].displayEmployee()
  
print ('Total Employee: ' + str(Employee.empCount))
