# enter your code here to solve the transporation assignment
# voer hier je code in om de vervoersvraag op te lossen
import re
from abc import ABC, abstractmethod

class Passenger:

    @staticmethod
    def is_valid_name(name):
        pattern = r"^[a-zA-Z]+(?: [a-zA-Z]+)+$"

        return bool(re.fullmatch(pattern, name))
    
    def __init__(self, id, name, money):
        self.id = id
        self._name = name
        self.money = money

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not self.is_valid_name(value):
            raise ValueError("Invalid name.")
        
        self._name
    
class Vehicle(ABC):

    def __init___(self, license_plate, amout_of_seats):
        self.license_plate = license_plate
        self.amount_of_seats = amout_of_seats
        self._occupants = {}

    @property
    def number_of_occupants(self):
        return len(self._occupants)
    
    @property
    @abstractmethod
    def maximum_occupants(self):
        pass

    def add_passenger(self, passenger):
        self._occupants[passenger.id] = passenger

    def remove_passenger(self, passenger):
        if passenger.id in self._occupants:
            del self._occupants[passenger.id]

    def remove_all_passengers(self):
        self._occupants = {}

    @property
    def occupant_names(self):
        return [passenger.name for passenger in self._occupants.values()]
    
class Taxi(Vehicle):

    def __init__(self, license_plate, amout_of_seats):
        super().__init__(license_plate, amout_of_seats)
        self.is_available = True

    @property
    def maximum_occupants(self):
        return self.amount_of_seats
    
    def pickup(self, passengers, distance):
        if self.is_available == False:
            raise ValueError("Taxi is currently unavailable.")
        elif len(passengers) > self.amount_of_seats:
            raise ValueError("Number of passengers exceeds the maximum for taxi.")
        
        fare = max(5, 1 + distance)
        
        first_passenger = passengers[0]

        if first_passenger.money < fare:
            raise RuntimeError("Passenger does not have enough money.")
        first_passenger.money -= fare

        for passenger in passengers:
            self.add_passenger(passenger)
        self.is_available == False

    def dropoff(self):
        self.remove_all_passengers()
        self.is_available == True

class Buss(Vehicle):

    def __init__(self, license_plate, amout_of_seats):
        super().__init__(license_plate, amout_of_seats)

    @property
    def maximum_occupants(self):
        return self.amount_of_seats * 2
    
    def board(self, passenger):
        if self.number_of_occupants + 1 > self.maximum_occupants:
            raise RuntimeError("Bus is full.")
        
        fare = 2

        if passenger.money < fare:
            raise RuntimeError("Passenger does not have enough money.")
        passenger.money -= fare
    
        self.add_passenger(passenger)

    def disembark(self, passenger):
        self.remove_passenger(passenger)