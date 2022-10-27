class Airport:
    def __init__(self,iata,name,location,city,country,website,phone):
        self.__iata = iata
        self.__name = name
        self.__location = location
        self.__city = city
        self.__country = country
        self.__website = website
        self.__phone = phone
        self.__flightOperators = {}

    def getIata(self):
        self.__iata

    def getName(self):
        self.__name

    def getLocation(self):
        self.__location
    
    def getCity(self):
        self.__city
    
    def getCountry(self):
        self.__country

    def getPhone(self):
        self.__phone

    def getFlightOperators(self):
        self.__flightOperators

    def addOperator(self,nameOperator,numPlanes):
        self.__flightOperators[nameOperator] = numPlanes