#Dictionary

Dict={1:'one'
    ,2:'two'
    ,3:'Three'
    ,4:'Four'
    ,5:'Five'
      }
Dict1 = {1: 'one'
    , 2:{1:'A',2:'B',3:'C'}
    , 3:['e','f','g','h']
        }
                                #create

print(Dict)                     #Read
print(Dict[1])
print(Dict.get(5))
print(Dict.get(6,'Key not found'))
print(Dict1[2][1])
print(Dict1[3][1])

Dict[5]='replace'               #Update
print(Dict)

Dict[6]='insert'
print(Dict)

print('Here')

del Dict[1]                 #delete
print(Dict)

Dict1.clear()
print(Dict1)






