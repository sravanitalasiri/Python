class function1():

    def __init__(self,Roll_no,Name,course_no,courses,course):
        self.Roll_no=Roll_no
        self.Name=Name
        self.course_no=course_no
        self.courses=courses
        self.course=course

    def get_input(self):
        self.Roll_no=input('Enter Roll no    :   ')
        self.Name=input('Enter name          :   ')
        self.course_no=int(input('Enter no of cousers you wish to enter  :   '))
        self.course=[]
        for x in range(self.course_no):
            self.courses=input('Enter course name    :   ')
            self.course.append(self.courses)

    def put_output(self):
        print(self.Roll_no)
        print(self.Name)
        print(self.course)

k=function1(100,'sree',3,'math',[])
k.get_input()
k.put_output()