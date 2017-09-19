from sys import exit

global cost
global toppingslist
global pizza
global size
global crust
global name
cost = 0
toppingslist=[]



def start():
    global name
    goahead=int(input("Hi! If you would like to order a pizza, press 1. Otherwise please press 0 to quit."))
    if goahead == 1:
        name = str(input("What is your name?"))
        sizerun()
    elif goahead == 0:
        exit(0)
    else:
        print("Invalid input.")
        start()

def sizerun():
    global cost
    global size
    size=int(input("We have two sizes. A large for $12 and a small for $7. Press 1 for a large, 2 for a small. At any point hit 0 to quit."))
    if size == 1:
        cost=cost+12
        size = str("Large")
        crustrun()
    elif size == 2:
        cost=cost+7
        size = str("Small")
        crustrun()
    elif size == 0:
        exit(0)
    else:
        print ("Invalid input.")
        start()

def crustrun():
    global cost
    global crust
    crust=int(input("What crust would you like? Press 1 for thin, 2 for thick."))
    if crust == 1:
        crust = str("Thin")
        premade()
    elif crust == 2:
        crust = str("Thick")
        premade()
    elif crust == 0:
        exit(0)
    else:
        print ("Invalid input.")
        start()

def premade():
    global cost
    global pizza
    premade=int(input("We have some premade pizzas. Would you like a Margherita for $4 more (press 1)," "\n"
                      "Hawaiian for $6 more (press 2), Californian for $6 more (press 3)" "\n"
                      "Vegetarian for $5 more (press 4) or build your own (press 5)"))
    if premade == 5:
        toppingsrun()
    if premade == 1:
        cost = cost+4
        pizza = str("Margherita")
        endpre()
    if premade == 2:
        cost = cost+6
        pizza = str("Hawaiian")
        endpre()
    if premade == 3:
        cost = cost+6
        pizza = str("Californian")
        endpre()
    if premade == 4:
        cost = cost+5
        pizza = str("Vegetarian")
        endpre()
    elif premade == 0:
        exit(0)
    else:
        print ("Invalid input")
        start()



def toppingsrun():
    global cost
    global toppingslist
    toppings = int(input(("Here is a list of our toppings:""\n"
               "$2 Pepperoni (press 1)""\n"
               "$2 Cheese (press 2)""\n"
               "$2 Mushrooms (press 3)""\n"
               "$3 Bacon (press 4)""\n"
               "$2 Pineapple (press 5)""\n"
               "$3 Sausage (press 6)""\n"
               "$2 Bell Peppers (press 7)" "\n"
               "If you do not wish for any more toppings press 8.""\n"
               "Don't worry, press one topping at a time, you will have a chance to get more.")))
    if toppings == 8:
        endtoppings()
    if toppings == 1:
        cost = cost+2
        toppingslist.append("Pepperoni")
        toppingsrun()
    if toppings == 2:
        cost = cost+2
        toppingslist.append("Cheese")
        toppingsrun()
    if toppings == 3:
        cost = cost+2
        toppingslist.append("Mushrooms")
        toppingsrun()
    if toppings == 4:
        cost = cost+3
        toppingslist.append("Bacon")
        toppingsrun()
    if toppings == 5:
        cost = cost+2
        toppingslist.append("Pineapple")
        toppingsrun()
    if toppings == 6:
        cost = cost+3
        toppingslist.append("Sausage")
        toppingsrun()
    if toppings == 7:
        cost = cost+2
        toppingslist.append("Bell Peppers")
        toppingsrun()
    elif toppings == 0:
        exit (0)
    else:
        print ("Invalid input.")
        start()


def endpre():
    global cost
    global size
    global crust
    global pizza
    global name
    print ("Hi, ", name, "You ordered a", size, pizza, "pizza with", crust, "crust.")
    confirm=int(input("To confirm this press 1, to reorder press 2."))
    if confirm == 1:
        print ("Your total is", cost, "dollars. Thanks for eating with us!")
        exit(0)
    if confirm == 2:
        sizerun()
    else:
        print ("Invalid input.")
        start()

def endtoppings():
    global cost
    global size
    global crust
    global toppingslist
    global name
    print ("Hi, ", name, "You ordered a", size, "pizza with", crust, "crust." "\n"
            "Your pizza toppings were: ", toppingslist)
    confirm=int(input("If you would like to confirm press 1, if you wish to reorder press 2. "))
    if confirm == 1:
        print ("Your total is", cost, "dollars. Thanks for eating with us!")
        exit(0)
    if confirm == 2:
        while len(toppingslist) > 0: toppingslist.pop()
        sizerun()
    else:
        print ("Invalid input.")
        start()

start()



