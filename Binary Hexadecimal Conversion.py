from sys import exit

def start():
    global decimal
    choice=str(input("Press 1 to convert binary to decimal, 2 for decimal to binary, 3 for hex to decimal,\n" +"4 for decimal to hex, 5 for binary to hex, 6 for hex to binary, 7 to quit"))
    if choice=="1":
        binary=str(input("What binary number would you like to convert?"))
        binary_to_decimal(binary)
        print(decimal)
        start()
    elif choice=="2":
        decimal=int(input("What decimal number would you like to convert?"))
        decimal_to_binary(decimal)
        start()
    elif choice=="3":
        hexa=str(input("Hexadecimal number?"))
        hexadecimal_to_decimal(hexa)
        print (decimal)
        start()
    elif choice=="4":
        decimal=int(input("Decimal number?"))
        decimal_to_hexadecimal(decimal)
        start()
    elif choice=="5":
        binary=int(input("Binary number?"))
        binary_to_hexadecimal(binary)
        start()
    elif choice=="6":
        hexa=(input("Hexadecimal number?"))
        hexadecimal_to_binary(hexa)
        start()
    elif choice=="7":
        exit(0)
    else:
        print("Action not identified")
        start()

def binary_to_decimal(binary):
    global decimal
    decimal=0
    binary=str(binary)
    for i in range(0, len(binary)):
        if (int(binary[i:i+1])!=0 and int(binary[i:i+1])!=1):
            print ("Your number isn't in binary")
            start()
        else:
            tempInt=int(binary[i:i+1])
            power=len(binary)-i-1
            decimal=decimal+tempInt*(2**power)

def decimal_to_binary(decimal):
    binary=[]
    s=("")
    while decimal > 0:
        binary.append(decimal%2)
        decimal=int(decimal/2)
    for i in reversed(binary):
        s = s+str(i)
    print (s)

def hexadecimal_to_decimal(hexa):
    global decimal
    hexa=hexa.capitalize()
    decimal=0
    for i in range(0, len(hexa)):
        tempInt=int(hexa[i:i+1], 16)
        power=len(hexa)-i-1
        decimal=decimal+tempInt*(16**power)

def decimal_to_hexadecimal(decimal):
    decimal=hex(decimal)
    print(decimal[2:])

def binary_to_hexadecimal(binary):
    binary_to_decimal(binary)
    number=decimal
    decimal_to_hexadecimal(number)

def hexadecimal_to_binary(hexa):
    global decimal
    hexa=str(hexa)
    hexadecimal_to_decimal(hexa)
    number=decimal
    decimal_to_binary(number)

start()
