from studentSchedular import studentSchedular

class Admin:
    def showMenu(self):
        self.StudentSchedular=studentSchedular()
        print("Choose from the Menu below")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Add Course")
        print("4. Add Faculty")
        print("5. Add Batch")
        print("6. Get Student by Roll No")
        print("7. Get Batch By Id")
        print("8. Get batch details by roll no")
        print("9. Exit")

        while(True):
            x = input("Enter the choice")

            if x=="1":
                while(True):
                    rollNo=input("enter the roll no")
                    if(self.StudentSchedular.validate(rollNo)):
                        continue
                    else:
                        break
                name=input("enter the name")
                cnt=input("enter the no of courses")
                courses=[]
                for i in range(0,int(cnt)):
                    course=input("enter the course name")
                    courses.append(course)
                self.StudentSchedular.addStudent(rollNo,name,courses)
                self.StudentSchedular.showAllStudents()

            elif x=="2":
                self.StudentSchedular.showAllStudents()

            elif x=="3":
                courseName=input("enter the course name")
                self.StudentSchedular.addCourse(courseName)

            elif x=="4":
                id=input("enter the id")
                name=input("enter the name")
                cnt = input("enter the no of courses")
                courses = []
                for i in range(0, int(cnt)):
                    course = input("enter the course name")
                    courses.append(course)
                self.StudentSchedular.addFaculty(id,name,courses)

            elif x=="5":
                id=input("enter the batch id")
                courseName=input("enter the course name")
                facultyName=input("enter the faculty name")

                self.StudentSchedular.showAllStudents()
                num = input("enter the no of students  you want to enter")
                students={}
                for cnt in range(0,int(num)):
                    rollNo=input("enter the roll no")
                    students.update({rollNo:self.StudentSchedular.getStudentByRollNo(rollNo)})
                self.StudentSchedular.addBatch(id,courseName,facultyName,students)

            elif x=="6":
                rollNo=input("enter the roll no")
                self.StudentSchedular.getStudentByRollNo(rollNo)

            elif x=="7":
                id=input("enter the batch id")
                self.StudentSchedular.getBatchByBatchId(id)

            elif x=="8":
                rollNo = input("enter the roll no")
                self.StudentSchedular.getBatchByRollNo(rollNo)

            else:
                break;


admin=Admin()
admin.showMenu()