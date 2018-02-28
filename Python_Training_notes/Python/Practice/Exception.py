try:
    file=open('testfile','r')
except IOError:
    print("Error:    Can\'t find file")
else:
    print('Written content in file successfully')
finally:
    print('Finally block executes always')

#----------

try:
   import sree
except IOError:
    print("Error:    Can\'t find file")
except ImportError:
    print("Error:    No module found")
else:
    print('Module imported successfully')
finally:
    print('Finally block executes always')

#----------


try:
    number = int(input("Enter a number between 0-9   :   "))
except ValueError:
    print("Please enter numbers only")
else:
    print("you entered number ", number)