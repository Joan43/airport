from importlib import import_module
from controllerAirport import ControllerAirport

controller = ControllerAirport()

def menu():
    print("AIRPORT DATABASE")
    print("----------------------------")
    print("1.- Import an airport.")
    print("2.- Delete an airport.")
    print("3.- Add a flight operator to an airport.")
    print("4.- Delete a flight operator from an airport.")
    print("5.- List airports by operators.")
    print("6.- List number of planes by operator - (by airport / all).")
    print("7.- Exit.")

def readIata():
    while True:
        iata = input("IATA: ")
        if len(iata) == 3:
            if iata.isalpha():
                return iata

def addAirport():
    iata = readIata()
    if controller.addAirport(iata):
        print("Yes!")
    else:
        print("No!")

def delAirport():
    iata = readIata()
    if controller.delAirport(iata):
        print("Yes!")
    else:
        print("No!")

def addOperator():
    iata = readIata()
    nameOperator = input("Name operator: ")
    numPlanes = int(input("Num planes: "))
    if controller.addOperator(iata,nameOperator,numPlanes):
        print("Yes!")
    else:
        print("No!")

def delOperator():
    iata = readIata()
    nameOperator = input("Name operator: ")
    if controller.delOperator(iata,nameOperator):
        print("Yes!")
    else:
        print("No!")

def listOperators():
    nameOperator = input("Name operator: ")
    result = controller.listOperators(nameOperator)
    if result != None:
        print(result)
    else:
        print("No!")

while True:
    menu()
    opt = int(input("Choose option: "))
    if opt == 1:
        addAirport()
    if opt == 2:
        delAirport()
    if opt == 3:
        addOperator()
    if opt == 4:
        delOperator()
    if opt == 5:
        listOperators()
    if opt == 7:
        print("Exit!!")
        break