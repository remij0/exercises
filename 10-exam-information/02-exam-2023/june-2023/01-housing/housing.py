import re
from abc import ABC, abstractmethod

class Person:
    @staticmethod
    def is_valid_name(name):
        pattern = r"^[a-zA-Z]+(?: [a-zA-Z]+)+$"
        return bool(re.fullmatch(pattern, name))
    
    def __init__(self, id, name, is_a_student):
        self.id = id
        self._name = name
        self.is_a_student = is_a_student

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not self.is_valid_name(value):
            raise ValueError("Invalid name.")
        self._name = value
    
class Residence(ABC):
    def __init__(self, address, area, number_of_rooms):
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self._occupants = {}

    @property
    def number_of_occupants(self):
        return len(self._occupants)
    
    @property
    def maximum_occupants(self):
        person_per_area = self.area // 20
        person_per_room = self.number_of_rooms * 2
        return int(min(person_per_area, person_per_room))
    
    def register_resident(self, person):
        if len(self._occupants) >= self.maximum_occupants:
            raise RuntimeError("Not enough room in residence.")
        self._occupants[person.id] = person

    def unregister_resident(self, id):
        if id in self._occupants:
            del self._occupants[id]
    
    @property
    def resident_names(self):
        return [person.name for person in self._occupants.values()]
    
    @abstractmethod
    def calculate_value(self):
        pass

class Villa(Residence):
    def __init__(self, address, area, number_of_rooms, garage_capacity):
        super().__init__(address, area, number_of_rooms)
        self.garage_capacity = garage_capacity

    def calculate_value(self):
        return (25000 * self.number_of_rooms) + (2100 * self.area) + (10000 * self.garage_capacity)
    
class StudentKot(Residence):
    def __init__(self, address, area, number_of_rooms):
        super().__init__(address, area, number_of_rooms == 1)

    def register_resident(self, person):
        if not person.is_a_student:
            raise ValueError("Only students can register in a student kot.")
        super().register_resident(person)
    
    def calculate_value(self):
        return 150000 + (750 * self.area)
