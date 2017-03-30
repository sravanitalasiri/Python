class Parent:
                parentattri =100;
                def __init__(self):
                                print("from the parent construtor ")
                
                def parentMethod(self):
                                print('Calling parent method')

                def setAttr(self, attr):
                                Parent.parentAttr = attr

                def getAttr(self):
                                print("Parent attribute :", Parent.parentAttr)

class Child(Parent):
                def __init__(self):
                                super(Child, self).__init__()
                                print("Calling child constructor")

                def childMethod(self):
                                print('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
