import pakuri
from pakuri import Pakuri

class Pakudex():

    all_pakuri = []
    pakuri_count = 0
    species_array = []

    def __init__(self, capacity = 20):
        self.capacity = capacity

    def get_size(self):
        return len(self.all_pakuri)

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if len(self.all_pakuri) > 0:
            return [pakuri.get_species() for pakuri in self.all_pakuri]

    def get_stats(self,species):
        for pakuri in self.all_pakuri:
            if pakuri.get_species() == species:
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]

    def sort_pakuri(self):
        if len(self.all_pakuri) > 0:
            self.all_pakuri.sort()

    def add_pakuri(self, species):
        if any(pakuri.get_species() == species for pakuri in self.all_pakuri):
            return False
        else:
            self.all_pakuri.append(Pakuri(species))
            self.pakuri_count += 1
            #print(self.all_pakuri)
            #print(len(self.all_pakuri))
            #print("capactity:", self.capacity)
            #print("count:", self.pakuri_count)
            return True

    def evolve_species(self, species):
        for pakuri in self.all_pakuri:
            if pakuri.get_species() == species:
                pakuri.evolve()
                return True
        return False





