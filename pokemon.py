import json 
class add_pokemon:
    def json(self):
        pokemon =[
            {"nom": "Floravol", "type": "Plante", "niveau": 1, "Puissance": 45, "PV": 55, "Defense": 50},
            {"nom": "Psykokwak", "type": "Plante", "niveau": 1, "Puissance": 52, "PV": 50, "Defense": 48},
            {"nom": "Rondoudou", "type": "Fée", "niveau": 1, "Puissance": 30, "PV": 90, "Defense": 15},
            {"nom": "Luxio", "type": "Electrique", "niveau": 1, "Puissance": 85, "PV": 60, "Defense": 49},
            {"nom": "Etourvol", "type": "Vol", "niveau": 1, "Puissance": 75, "PV": 55, "Defense": 50},
            {"nom": "Lainergie", "type": "Electrique", "niveau": 1, "Puissance": 55, "PV": 70, "Defense": 55},
            {"nom": "Phanpy", "type": "Sol", "niveau": 1, "Puissance": 60, "PV": 90, "Defense": 60},
            {"nom": "Magicarpe", "type": "Eau", "niveau": 1, "Puissance": 10, "PV": 20, "Defense": 55},
            {"nom": "Gloupti", "type": "Poison", "niveau": 1, "Puissance": 43, "PV": 70, "Defense": 53},
            {"nom": "Baudrive", "type": "Spectre", "niveau": 1, "Puissance": 50, "PV": 90, "Defense": 34}]
        print(pokemon)
pok = add_pokemon()
print(pok.json())