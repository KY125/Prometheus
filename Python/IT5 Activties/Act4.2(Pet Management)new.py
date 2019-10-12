def add_pet():
    petList.append([input("Enter pet name: "),int(input("Enter pet age: ")),input("Enter pet specie: "),input("Enter pet breed: "),input("Enter pet gender: "),int(input("Enter pet price: "))])

def find_pet(name):
    list_count = 0
    found = []

    if name.isdigit() is True:
        name = int(name)
        if name > len(petList)-1:
              found.append(['Index out of Range!'])
        else:
            found.append(petList[name])
            return found
    else:
        for x in petList:
            if name in x:
                found.append(petList[list_count])
            list_count += 1

    if not found:
            found.append(['Not Found!'])
    return found
        #petList[find_pet]

def get_index(i):
    list_count = 0
    for x in petList:
        if i in x:
           return list_count
        list_count += 1
        #petList[find_pet]

def insert_pet():
    res = ''
    name = input("Enter name of pet to move: ")

    for x in petList:
        if name in x:
            res += name
    if res == '':
        print('Name does not exist!')
    else:
        x=get_index(name)
        index = int(input("Enter position: "))
        petList.insert(index, petList[x])
        if index == 0:
            petList.pop(x+1)
        else:
            petList.pop(x)

petList = [['bogart',9,'dog','chowchow','m',2000],['art',2,'cat','siopao','f',250],['bob',5,'dog','askal','m',2500],['don',1,'rat','siomai','f',500]]

choice = ''
while choice != 't':
    choice = input("[A]dd - Allow user to add pet name in a list.\n"
                   "[I]nsert - Insert pet’s name to a specific position of a list.\n"
                   "[S]earch - Display found pet’s name after searching from a list. {Search by index and by value}\n"
                   "[E]dit - Modify pet’s name to an existing element from a list. {Edit by index and by value}\n"
                   "[V]iew - View all data in a list. Also, do the following:\n"
                   "[D]elete - Erase pet’s name from a list.\n"
                   "[C]ount - Display the total size of n list.\n"
                   "[T]erminate - Terminate the entire program.\n\n>>").lower()
    print('\n')
    if choice == 'a':
        add_pet()
        print('\n\n')
    # if choice == 'i':
    #     insert_pet()
    #     print('\n\n')
    # if choice == 's':
    #     find = input('Search: ')
    #     # print('\n'.join(map(str,find_pet(find))))
    #     display(find_pet(find))
    #     print('\n\n')
    # if choice == 'e':
    #     edit_pet()
    #     print('\n\n')
    # if choice == 'v':
    #     display(petList)
    #     menu = ''
    #     while menu!= 'e':
    #         menu = input('\n[1]View by specie'
    #                 '\n[2]View by breed'
    #                 '\n[3]View by gender'
    #                 '\n[4]Expensive Pet'
    #                 '\n[5]Eldest Pet'
    #                 '\n[E]xit'
    #                 '\n>>').lower()
    #         if menu == '1':
    #             display(sorted(petList,key=itemgetter(2)))
    #         if menu == '2':
    #             display(sorted(petList,key=itemgetter(3)))
    #         if menu == '3':
    #             display(sorted(petList,key=itemgetter(4)))
    #         if menu == '4':
    #             display(reversed(sorted(petList,key=itemgetter(5))))
    #         if menu == '5':
    #             display(reversed(sorted(petList,key=itemgetter(1))))
    #     print('\n\n')
    # if choice == 'd':
    #     remove_pet()
    #     print('\n\n')
    # if choice == 'c':
    #     print(f'There are {len(petList)} animals.')
    # print('\n\n')
    print(petList)