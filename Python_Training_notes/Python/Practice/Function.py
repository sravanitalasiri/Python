class function1():

    def __init__(self,list):
        self.list=list

    def process(self):
        self.list.append(4)
        self.list.append(5)
        self.list.append(6)
        return self.list
List1=[1,2,3]

p=function1([List1])
print(p.process())
print(List1)

k=function1(List1)
print(k.process())
print(List1)

