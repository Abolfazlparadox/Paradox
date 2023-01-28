from paradox import square
class  point():
    def __init__(self,input1,input2):
        self.x = input1
        self.y = input2
class flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers=[]
    def add_passengers(self,name):
        if self.open():
            return False
        self.passengers.append(name)
        return True
    def open(self):
        return self.capacity - len(self.passengers)
for i in range(10):
    print(f"the square of {i} is {square(i)}")
p=point(2,8)
print(p.x)
print(p.y)
flight1=flight(4)
