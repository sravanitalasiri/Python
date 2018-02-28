from student import student
from Course import Course
from Faculty import Faculty
from Batch import Batch

Students={}
batchDict={}
class studentSchedular:
    def validate(self,rollNo):
        if rollNo in Students.keys():
            print("Student already exisis")
            return True
        else:
            return False

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

    def addCourse(self,courseName):
        course=Course()
        course.setCourseName(courseName)
        print(course.courseName)

    def addFaculty(self,id,name,courses):
        faculty=Faculty()
        faculty.setId(id)
        faculty.setName(name)
        faculty.setCourseNames(courses)
        print(faculty.id)
        print(faculty.name)
        print(faculty.courseNames)

    def addBatch(self,id,courseName,facultyName,students):
        batch=Batch()
        batch.setId(id)
        batch.setCourseName(courseName)
        batch.setFacultyName(facultyName)
        batch.setBatchStudents(students)
        batchDict.update({id:batch})
        print(batch.id)
        print(batch.courseName)
        print(batch.facultyName)
        print(batch.students)

    def getStudentByRollNo(self,rollNo):
        Student=Students[rollNo]
        print(Student.rollNo)
        print(Student.name)
        print(Student.courseNames)
        return Student

    def getBatchByBatchId(self,id):
        batch=batchDict[id]
        print(batch.id)
        print(batch.courseName)
        print(batch.facultyName)
        print(batch.students)
        return batch

    def getBatchByRollNo(self,rollNo):
        for id in batchDict.keys():
            if rollNo in batchDict[id].students.keys():
                print(batchDict[id].id)
                print(batchDict[id].courseName)
                print(batchDict[id].facultyName)
                print(batchDict[id].students)
                break