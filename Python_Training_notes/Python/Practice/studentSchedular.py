from student import student

Students={}

class studentSchedular:


    def addStudent(self,rollNo,name,courseNames):
        Student=student()
        Student.setRollNo(rollNo)
        Student.setName(name)
        Student.setCourseNames(courseNames)
        Students.update({rollNo:Student})

    def showAllStudents(self):
        for rollNo in Students.keys():
            Student=Students[rollNo]
            print(Student.rollNo)
            print(Student.name)
            print(Student.courseNames)
            print('----------------------')
