import json
#GuardList = {}
#with open('database.txt', 'w') as f:
#    f.write(json.dumps(GuardList))
database = json.loads(open('database.txt').read())#database is now a dict
def save():
    with open('database.txt', 'w') as f:
        f.write(json.dumps(database))

def makeSolider():
    name = input('Enter name\n')
    pazam = input('Enter pazam\n')
    while not (pazam.isdigit() and 0 < int(pazam) < 6):
        print('pazam needs to be a number between 1 and 5')
        pazam = input('Enter pazam\n')
    database[name]=int(pazam)
    save()
    print('Solider added')

def delSolider(name):
    if(name in database):
        del database[name]
        save()
        print('Solider deleted')
    else:
        print('Name does not exist in the pool')

def make(listType):
    sortedList = sorted(database.items(),key= lambda tup: tup[1])
    if(listType == 'pazam'):
        p = int(input('Enter maximum pazam\n'))
        tempList = list(filter(lambda x: x[1] <= p, database.items()))
        sortedList = sorted(tempList,key= lambda tup: tup[1])

    #list1 = sortedList[int(len(sortedList)/2):]
    #list2 = sortedList[:int(len(sortedList)/2)]
    #final = (list2[::-1] + list1)
    final = []
    for i in range(len(sortedList)):
        if(i % 2 == 0):
            final.append(sortedList[i])
        else:
            final = [sortedList[i]] + final
    print('{0} per solider'.format(int(input('Required time?\n'))/len(final)))
    print('Name Pazam')
    for solider in final:
        print('{0} | {1}'.format(solider[0], solider[1]))


def printList():
    print('Name Pazam')
    for solider in database:
        print('{0} | {1}'.format(solider, database[solider]))

print('Welcome to GuardList!')
Welcome = 'add = add a solider to the pool\ndelete = delete a solider from the pool\nmake = Create a new list from the current pool\nlist = List all soliders in the pool\nexit = Will close the program'
print(Welcome)
while True:
    com = input()
    if(com == 'add'):
        makeSolider()
    elif(com == 'delete'):
        delSolider(input('Enter a solider to delete\n'))
    elif(com == 'make'):
        a = input('Do you want to use all soliders or until a specific pazam (pazam)?\n')
        make(a)
    elif(com == 'list'):
        printList()
    elif(com == 'exit'):
        exit()
    else:
        print('Unvalid input!')
        print(Welcome)
