class Faculty:
    def __init__(self):
        self.id=""
        self.name=""
        self.courseNames=""

    def setId(self,id):
        self.id=id
    def getId(self):
        return self.id

    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name

    def setCourseNames(self,courseNames):
        self.courseNames=courseNames
    def getCourseNames(self):
        return self.courseNames