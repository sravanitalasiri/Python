#List

List=[1,2,3,4,5,'sre']          #create

print(List)                     #Read
print(List[0])

List.append('append')           #Update
print(List)

List[1]='replace'
print(List)

List.insert(5,'insert')
print(List)

print('Here')

List.pop()                  #delete
print(List)

List.pop(0)
print(List)

del List[1]
print(List)

