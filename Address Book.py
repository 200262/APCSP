from sys import exit
namelist=[]
agelist=[]
numberlist=[]

def inputuser():
    name=str(input("What is your name?"))
    name=name.capitalize()
    age=str(input("What is your age?"))
    if int(age) > 130:
        print("Please make sure your age is less than 130.")
        action()
    number=str(input("What is your four digit number?"))
    numberlength=len(number)
    if numberlength!=4:
        print("Please make sure your number is four digits.")
        action()
    namelist.append(name)
    agelist.append(age)
    numberlist.append(number)

def recalluser():
    lookup=(str(input("Name you're looking up?")))
    lookup=lookup.capitalize()
    if lookup in namelist:
        index=namelist.index(lookup)
        agefound=agelist[index]
        numberfound=numberlist[index]
        print(str(lookup), "is", agefound, "years old. The number we have for them is", numberfound)
    else:
        print("User not found")


def action():
    run=True
    while run==True:
        whichaction=str(input("Press 1 to input, Press 2 to recall, Press 3 to quit"))
        if whichaction=="1":
            inputuser()
            action()
        elif whichaction=="2":
            recalluser()
            action()
        elif whichaction=="3":
            exit(0)
        else:
            print ("Action not identified.")
            action()

action()










