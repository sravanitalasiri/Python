class student:
    def __init__(self):
        self.name=""
        self.rollNo=""
        self.courseNames=""

    def setName(self,name): #SETTER
        self.name=name
    def getName(self):      #GETTER
        return self.name

    def setRollNo(self,rollNo):
        self.rollNo=rollNo
    def getRollNo(self):
        return self.rollNo

    def setCourseNames(self,courseNames):
        self.courseNames=courseNames
    def getCourseNames(self):
        return self.courseNames
