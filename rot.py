def my_function():
  print("i am new here")
my_function()

#a function to add numbers
def sum(x, y,z):
  a=x+y+z
  print("the sum is",a)
sum(810,20,46)
sum(26,45,98)

#a function to multiply two numers
def multiply(x,y,z):
  a=x*y*z
  print("the multiplication is equals to",a)
multiply(23, 46, 78)

def sum(q ,w):
   a=q+w
   return a
print(sum(89,105))

#a function to divide two numbers
def div(r,t):
  a=r/t
  print("the division is" ,a)
div(1789,45)

#a function for undefined arguments
def courses(*loos):
  for subject in loos:
    print(subject)
courses("BCOM","BSCIT","OOP2")

def courses(*args):
  for subject in args:
    return subject
print(courses("CCM","CCNA","DSAA","CIST"))

def courses(**kwargs):
  for key,value in kwargs.items():
    print("{}:{}" .format(key,value))
courses(first="big data",second="CCNA",third="HHCA")

#function to define default parameter value
def kenya(county="kajiado"):
  print("i live in" +county)
kenya()
kenya("marsabit")
kenya("moyale")