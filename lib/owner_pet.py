class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        if owner:
            owner.add_pet(self)
        Pet.all.append(self)

    @staticmethod
    def pets():
        return Pet.all

    @classmethod
    def get_sorted_pets(cls):
        return sorted(cls.all, key=lambda pet: pet.name)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only Pet instances can be added")
        self._pets.append(pet)
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)
