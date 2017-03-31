# CRUD on Dictonary

#Creation of Dictonary 
dict = {'Name': 'Nilesh1','Name': 'Zara', 'Age': 7, 'Class': 'First','Name': 'Sachin1',}
print(dict);
print("Dictonary All items ", dict.items())

#Updatiopn
dict['Name']="Rajat"
dict['Age']=25

print("After updating",dict.items())

dict1 =dict.copy();
print("Copy of dict ", dict1)

#Deleting 
del dict['Name']; 
print("After Deleting ",dict.items())

dict.clear();     # remove all entries in dict
print("After clearing all value ",dict.items())

dict1 =dict.copy();
print("Copy of dict ", dict1)
