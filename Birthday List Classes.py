birthArray = {}
birthMonths = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']

class Person():
    def __init__(self):
        self.name = ''
        self.birthYear = 0
        self.birthMonth = ''
        self.birthDate = 0
    def createPerson(self):
        self.name = (input("Name?")).upper()
        self.birthDate = int(input("Date?"))
        self.birthYear = int(input("Year?"))
        self.birthMonth = input("Month?")
        if self.birthMonth.upper() not in birthMonths:
            print ('Your month is not valid. Try again.')
            self.createPerson()
    def addEntry(self):
        birthArray[self.name] = [self.birthYear, self.birthMonth, self.birthDate]

def recallName():
        name=input("Name to be recalled?")
        name=name.upper()
        for i in birthArray:
            if i == name:
                print (birthArray[i])

def endOption():
    finalOption = input("Thanks for using. Are you sure you would like to end?")
    if finalOption.lower() == 'no':
        main()

def main():
    choice = input('Press A to add a new entry, B to search for information, anything else to quit')
    if choice.upper() == 'A':
        new = Person()
        new.createPerson()
        new.addEntry()
        main()
    if choice.upper() == 'B':
        recallName()
        main()
    else:
        endOption()

main()


