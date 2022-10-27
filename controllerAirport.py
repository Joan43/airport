import json
from airport import Airport
import requests

class ControllerAirport():
    def __init__(self):
        self.__airports = {}

    def addAirport(self,iata):

        url = "https://airport-info.p.rapidapi.com/airport"

        querystring = {"iata":iata}

        headers = {
            "X-RapidAPI-Key": "7f1938c1dcmsh87eb2cac0b35970p1ad0dfjsnaf6dbf21dee3",
            "X-RapidAPI-Host": "airport-info.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        if response.status_code == 200:
            if iata in self.__airports:
                return False
            airport = response.json()

            name = airport["name"]
            location = airport["location"]
            city = airport["city"]
            country = airport["country"]
            website = airport["website"]
            phone = airport["phone"]

            self.__airports[iata] = Airport(iata,name,location,city,country,website,phone)
            return True
        return False

    def delAirport(self,iata):
        if iata in self.__airports:
            self.__airports.pop(iata)
            return True
        return False

    def addOperator(self,iata,nameOperator,numPlanes):
        if iata in self.__airports:
            air = self.__airports[iata]
            air.addOperator(nameOperator,numPlanes)
            return True
        return False

    def delOperator(self,iata,nameOperator):
        if iata in self.__airports:
            air = self.__airports[iata]
            air.pop(nameOperator)
            return True
        return False

    def listOperator(nameOperator):
        for iata,nameOperator in self.__airports:
            
        return None
        