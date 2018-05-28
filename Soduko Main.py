#Cross Product Function
def cross(A, B):
    tempList = []
    for a in A:
        for b in B:
            tempList.append(a+b)
    return (tempList)

#Setting Up
digits = '123456789'
rows = 'ABCDEFGHI'
columns = digits
squares = cross(rows, columns)
count = 0

#Creating unitList
unitList = []

tempOne = []
for x in columns:
    tempOne.append(cross(rows,x))

tempTwo = []
for x in rows:
    tempTwo.append(cross(x, columns))

tempThree = []
for x in ('ABC', 'DEF', 'GHI'):
    for z in ('123', '456', '789'):
        tempThree.append(cross(x,z))

unitList = tempOne + tempTwo + tempThree

#Creating Peers and Units Dictionaries
peers = dict()
units = dict()

for x in squares:
    temp = []
    for u in unitList:
        units[x] = temp
        if x in u:
            temp.append(u)
        units.update(x=temp)

for x in squares:
    peers[x] = (set(sum(units[x], []))-set([x]))


#Assign Function
def assign(values, square, answer):
    toRemove = values[square].replace(answer, '')
    for x in toRemove:
        if not (eliminate(values, square, x)):
            return False
    return values

#Eliminate Function
def eliminate(values, square, answer):
    if answer not in values[square]:
        return values
    values[square] = values[square].replace(answer, '')
    if len (values[square]) == 0:
        return False
    elif len(values[square]) == 1:
        x = values[square]
        if not all(eliminate(values, z, x) for z in peers[square]):
            return False
    for x in units[square]:
        options = [square for square in x if answer in values[square]]
        if len(options)==0:
            return False
        elif len(options)==1:
            if not (assign(values, options[0], answer)):
                return False
    return values

#Going from string format to dict format
def gridtodict(grid):
    values = dict()
    for square in squares:
        values[square] = digits
    for square, answer in gridvalues(grid).items():
        if answer in digits and not assign(values, square, answer):
            return False
    return values

def gridvalues(grid):
    things = [x for x in grid if x in digits or x in '0.']
    assert len(things) == 81
    return dict(zip(squares, things))

#Display in grid format

def display(values):
    max = 0
    for square in squares:
        length = len(values[square])
        if length > max:
            max = length
    width = max +1
    line = '+'.join(['-'*(width*3)]*3)
    for x in rows:
        print (''.join(values[x+y].center(width)+('|' if y in '36' else '') for y in columns))
        if x in 'CF':
            print (line)
    print

#assigns a value and tests if this value is correct (backbone of program)

def search(x):
    global count
    global please
    count += 1
    if x is False:
        return False
    if all(len(x[s]) == 1 for s in squares):
        return x
    #finds square with least amount of possible values
    if please == 'y' and count > 4:
        print(display(x))
        please = 'n'
    n,s = min((len(x[s]), s) for s in squares if len(x[s]) > 1)
    return some(search(assign(x.copy(), s, d)) for d in x[s])

#used to return part of a list that is correct
def some(seq):
    for x in seq:
        if x:
            return x
    return False

#call function
def solve(grid):
    return (search(gridtodict(grid)))

gridinput=str(input('Please type out your problem from left to right. Use a period to represent a blank space.'))
please = str(input('Do you want a hint? Enter y or n'))
want = str(input('Do you want the full solution? Enter y or n'))

if want == 'y':
    display(solve(gridinput))
if want == 'n':
    solve(gridinput)


#Credit to http://norvig.com/sudoku.html for inspiration/structure and some + search functions as well as certain lines in other functions
