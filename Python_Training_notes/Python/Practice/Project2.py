class Account:
    def __init__(self):
        self.Account_no=""
        self.Amount=""

    def setAccount_no(self,Account_no): #SETTER
        self.Account_no=Account_no
    def getAccount_no(self):      #GETTER
        return self.Account_no

    def setAmount(self,Amount):
        self.Amount=Amount
    def getAmount(self):
        return self.Amount

ICICI={}

class ICICI(Account):


    def create_account(self,Account_no):
        new_account=Account()
        new_account.setAccount_no(Account_no)
        new_account.setAmount(0.00)
        ICICI.update({Account_no:new_account})

    def Deposit_amount(self,Account_no,Amount):
        try:
            if Account_no in ICICI:
                Deposit=Account()
                Deposit.setAccount_no(Account_no)
                Deposit.setAmount(Amount)
                ICICI.update({Account_no:Deposit})
            else:
            except raise InvalidAccountnoException()

        for Account_no in Students.keys():
            Student=Students[rollNo]
            print(Student.rollNo)
            print(Student.name)
            print(Student.courseNames)
            print('----------------------')




from studentSchedular import studentSchedular

class Client:
    def showMenu(self):
        self.StudentSchedular=studentSchedular()
        print("Choose from the Menu below")
        print("1. Create Account")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Exit")

        while(True):
            x = input("Enter the choice :   ")

            if x=="1":
                Account_no=input("Enter the Account no :   ")
                self.StudentSchedular.addStudent(rollNo,name,courses)
                self.StudentSchedular.showAllStudents()

            elif x=="2":
                self.StudentSchedular.showAllStudents()
            elif x=="3":

            else:
                break;


admin=Admin()
admin.showMenu()