class Batch:
    def __init__(self):
        self.id=""
        self.couseName=""
        self.facultyName=""
        self.students= list()

    def setId(self,id):
        self.id=id
    def getId(self):
        return self.id

    def setCourseName(self,courseName):
        self.courseName=courseName

    def getCourseName(self):
        return self.courseName

    def setFacultyName(self,facultyName):
        self.facultyName=facultyName

    def getFacultyName(self):
        return self.facultyName

    def setBatchStudents(self,students):
        self.students=students

    def getBatchStudents(self):
        return self.students

