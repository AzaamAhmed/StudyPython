name = "Azaam"
print("Hello Dear " + name + "!") 

""" a = input("Enter number : ")
 print(int(a)*10) """

""" mark = int(input())
if(mark>35):
    print("Pass")
else:
    print("Fail") """
    
    
""" score = int(input("Score : "))
if (score < 35):
    print("Poor Student")
elif (score > 35 and score < 70):
    print("Average Student")
else:
    print("Good Student") """
    
"""     
for i in "APPLE":
    print(i)
    
for i in range (5):
    print(i) """
    
    
""" for i in range (1,11):
    if(i%2 == 0):
        print(i)
        
ec = 0
oc = 0
for i in range (1,84):
    if(i%2 == 0):
        ec = ec + 1
    else:
        oc = oc + 1
print(ec)
print(oc)

for i in range (1,5):
    print()
    for j in range (1,i+1):
        print(j,end="") """
        
        
""" sname = "Azaam"
spassword = "1234"

uname = input("Enter Username : ")
password = input("Enter Password : ")

def validate():
    if( sname == uname and spassword == password):
        print("Login Successful")
    else:
        print("Enter the user credential correctly")
        
validate() """

""" 
class student:
    def __init__(self):
        self.name = "Azaam"
        self.regno = "18095"
    def display(self):
        print("Name: ", self.name)
        print("Reg No: ", self.regno)
        
s1=student()
print(s1.name)
print(s1.regno)
s1.display()
 """


""" class dad():
    def phone(self):
        print("Dad's Phone...")

class mom():
    def sweet (self):
        print("Mom's sweet...")
     
class son(dad,mom):
    def laptop(self):
        print("Son's Laptop...")
        
ram=son()
ram.phone()
ram.sweet() """

""" class emp():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
class Mangr(emp):
    def __init__(self,dept):
        self.dept = dept
        
    def display(self):
        print(self.name, self.salary, self.dept)
        
m1 = Mangr("CSE")
m1.display() """
        
"""         
f = open("fruits.txt", "a")
f.write("Hello\n")
f.write("Azaam\n")

f = open("fruits.txt", "r+")
print(f.read())
 """
 
 
""" 
class computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is :", self.cpu, self.ram)

com1 = computer('i5', 16)
com2 = computer('Ryzen', 8)

# computer.config(com1)
# computer.config(com2)

com1.config()
com2.config()
 """

""" 
class computer:     ##size of the object declared by number of variables and size of each variables
    
    def __init__(self):
        self.name = "Azaam"
        self.age = 23
    
    def update(self):
        self.age = 30
        
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
        
    
c1 = computer()     ##size of the object allocated by construtor
c2 = computer()

c1.name = "Fasreen"
c1.age = 22           ##if the both lines are delleted function became true

if c1.compare(c2):
    print("They are same")
else:
    print("They are not same")

print(c1.name)
print(c1.age)

print(c2.name)
print(c2.age) 
"""

""" 
class car:
    
    wheels = 4            ##class variable
     
    def __init__(self):
         self.mil = 10       ##instance variable
         self.com = "Audi"      ##instance variable

c1 = car()
c2 = car()

car.wheels = 5

c2.com = "BMW"
c1.mil = 8
print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)

 """
""" 
class A:
    def show(self):
        print("in Show A")
        
class B(A):
    pass

a1 = B()
a1.show() """

class Nokia:
    company = "Nokia India"
    website = "www.nokia-india.com"
    
    def contact_details(self):
        print("Address   :  Cherry Road, Salem")
        
class Nokia1100(Nokia):
    def __init__(self):
        self.name = "Nokia 1100"
        self.year = 1998
        
    def product_details(self):
        print("Name      : ", self.name)
        print("Year      : ", self.year)
        print("Company   : ", self.company)
        print("Website   : ", self.website)
        
        
mobile = Nokia1100()
mobile.product_details()
mobile.contact_details()