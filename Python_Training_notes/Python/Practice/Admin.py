from studentSchedular import studentSchedular

class Admin:
    def showMenu(self):
        self.StudentSchedular=studentSchedular()
        print("Choose from the Menu below")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Exit")

        while(True):
            x = input("Enter the choice :   ")

            if x=="1":

                rollNo=input("Enter the roll no :   ")
                name=input("Enter the name  :   ")
                cnt=input("Enter the no of courses  :   ")
                courses=[]
                for i in range(0,int(cnt)):
                    course=input("Enter the course name :   ")
                    courses.append(course)
                self.StudentSchedular.addStudent(rollNo,name,courses)
                self.StudentSchedular.showAllStudents()

            elif x=="2":
                self.StudentSchedular.showAllStudents()

            else:
                break;


admin=Admin()
admin.showMenu()