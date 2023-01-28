import sys
def square(x):
    return x * x
#decorators
def a(f):
    def w():
        print("About to run the function...")
        f()
        print("Don with the function.")
    return w
@a
def hello():
    print("hello")

people= [
    {"name":"a", "house":"t"},
    { "name":"f", "house":"r"},
    { "name":"c", "house":"b"}
]
#def f(person):
#    return person["name"]
#people.sort(key=f)
people.sort(key=lambda person: person["name"])
print(people)

x= int(input())
y= int(input())

try:
   print(result =x/y)
    
except ZeroDivisionError:
    print ("Error : Cannot divide by zero")
    sys.exit(1)

