import json 
class add_pokemon:
    def json(self):
        pokemon =[
            {"Nom": "Floravol", "Type": "Plante", "Niveau": 1, "Puissance": 45, "PV": 55, "Defense": 50},
            {"Nom": "Psykokwak", "Type": "Plante", "Niveau": 1, "Puissance": 52, "PV": 50, "Defense": 48},
            {"Nom": "Rondoudou", "Type": "Fée", "Niveau": 1, "Puissance": 30, "PV": 90, "Defense": 15},
            {"Nom": "Luxio", "Type": "Electrique", "Niveau": 1, "Puissance": 85, "PV": 60, "Defense": 49},
            {"Nom": "Etourvol", "Type": "Vol", "Niveau": 1, "Puissance": 75, "PV": 55, "Defense": 50},
            {"Nom": "Lainergie", "Type": "Electrique", "Niveau": 1, "Puissance": 55, "PV": 70, "Defense": 55},
            {"Nom": "Phanpy", "Type": "Sol", "Niveau": 1, "Puissance": 60, "PV": 90, "Defense": 60},
            {"Nom": "Magicarpe", "Type": "Eau", "Niveau": 1, "Puissance": 10, "PV": 20, "Defense": 55},
            {"Nom": "Gloupti", "Type": "Poison", "Niveau": 1, "Puissance": 43, "PV": 70, "Defense": 53},
            {"Nom": "Baudrive", "Type": "Spectre", "Niveau": 1, "Puissance": 50, "PV": 90, "Defense": 34}]
        print(pokemon)
pok = add_pokemon()
print(pok.json())