from type_pok import Type
import json, random

class Combat(Type):

    def __init__(self):
        Type.__init__(self)
        self.info_json = self.read_json()
        self.pok_rival = self.random_pokemon()
        self.type_rival = self.pok_rival["type"]
        self.pok_player = self.random_pokemon()
        self.puissance_player = self.pok_player["puissance"]


    def attack(self, pv, puissance, type_player, type_enemy, defense):
        if type_player =="normal":
            pokemon_damage = self.normal(type_enemy, puissance)
            self.damage_poke = pokemon_damage * (1 - defense // 200) 
            remaining_life  = pv - self.damage_poke
            print (f"Le pokemon inflige {self.damage_poke} dégats, l'autre avait {pv}HP, il lui reste {remaining_life }HP mais il avait {defense}de def")
            return remaining_life
        
        if type_player =="feu":
            pokemon_damage = self.feu(type_enemy, puissance)
            self.damage_poke = pokemon_damage * (1 - defense // 200) 
            remaining_life  = pv - self.damage_poke
            print (f"Le pokemon inflige {self.damage_poke} dégats, l'autre avait {pv}HP, il lui reste {remaining_life }HP mais il avait {defense}de def")
            return remaining_life 
        
        if type_player =="eau":
            pokemon_damage = self.eau(type_enemy, puissance)
            self.damage_poke = pokemon_damage * (1 - defense // 200) 
            remaining_life  = pv - self.damage_poke
            print (f"Le pokemon inflige {self.damage_poke} dégats, l'autre avait {pv}HP, il lui reste {remaining_life }HP mais il avait {defense}de def")
            return remaining_life 
        
        if type_player =="plante":
            pokemon_damage = self.plante(type_enemy, puissance)
            self.damage_poke = pokemon_damage * (1 - defense // 200) 
            remaining_life  = pv - self.damage_poke
            print (f"Le pokemon inflige {self.damage_poke} dégats, l'autre avait {pv}HP, il lui reste {remaining_life }HP mais il avait {defense}de def")
            return remaining_life 
        
        if type_player =="electrique":
            pokemon_damage = self.electrique(type_enemy, puissance)
            self.damage_poke = pokemon_damage * (1 - defense // 200) 
            remaining_life  = pv - self.damage_poke
            print (f"Le pokemon inflige {self.damage_poke} dégats, l'autre avait {pv}HP, il lui reste {remaining_life }HP mais il avait {defense}de def")
            return remaining_life 

        if type_player =="glace":
            pokemon_damage = self.glace(type_enemy, puissance)
            self.damage_poke = pokemon_damage * (1 - defense // 200) 
            remaining_life  = pv - self.damage_poke
            print (f"Le pokemon inflige {self.damage_poke} dégats, l'autre avait {pv}HP, il lui reste {remaining_life }HP mais il avait {defense}de def")
            return remaining_life 
        
        if type_player =="combat":
            pokemon_damage = self.combat(type_enemy, puissance)
            self.damage_poke = pokemon_damage * (1 - defense // 200) 
            remaining_life  = pv - self.damage_poke
            print (f"Le pokemon inflige {self.damage_poke} dégats, l'autre avait {pv}HP, il lui reste {remaining_life }HP mais il avait {defense}de def")
            return remaining_life 
        
        if type_player =="poison":
            pokemon_damage = self.poison(type_enemy, puissance)
            self.damage_poke = pokemon_damage * (1 - defense // 200) 
            remaining_life  = pv - self.damage_poke
            print (f"Le pokemon inflige {self.damage_poke} dégats, l'autre avait {pv}HP, il lui reste {remaining_life }HP mais il avait {defense}de def")
            return remaining_life 
        
        if type_player =="sol":
            pokemon_damage = self.sol(type_enemy, puissance)
            self.damage_poke = pokemon_damage * (1 - defense // 200) 
            remaining_life  = pv - self.damage_poke
            print (f"Le pokemon inflige {self.damage_poke} dégats, l'autre avait {pv}HP, il lui reste {remaining_life }HP mais il avait {defense}de def")
            return remaining_life 
        
        if type_player =="vol":
            pokemon_damage = self.vol(type_enemy, puissance)
            self.damage_poke = pokemon_damage * (1 - defense // 200) 
            remaining_life  = pv - self.damage_poke
            print (f"Le pokemon inflige {self.damage_poke} dégats, l'autre avait {pv}HP, il lui reste {remaining_life }HP mais il avait {defense}de def")
            return remaining_life 
        
        if type_player =="psy":
            pokemon_damage = self.psy(type_enemy, puissance)
            self.damage_poke = pokemon_damage * (1 - defense // 200) 
            remaining_life  = pv - self.damage_poke
            print (f"Le pokemon inflige {self.damage_poke} dégats, l'autre avait {pv}HP, il lui reste {remaining_life }HP mais il avait {defense}de def")
            return remaining_life 
        
        if type_player =="insecte":
            pokemon_damage = self.eau(type_enemy, puissance)
            self.damage_poke = pokemon_damage * (1 - defense // 200) 
            remaining_life  = pv - self.damage_poke
            print (f"Le pokemon inflige {self.damage_poke} dégats, l'autre avait {pv}HP, il lui reste {remaining_life }HP mais il avait {defense}de def")
            return remaining_life 
                 
        if type_player =="roche":
            pokemon_damage = self.roche(type_enemy, puissance)
            self.damage_poke = pokemon_damage * (1 - defense // 200) 
            remaining_life  = pv - self.damage_poke
            print (f"Le pokemon inflige {self.damage_poke} dégats, l'autre avait {pv}HP, il lui reste {remaining_life }HP mais il avait {defense}de def")
            return remaining_life 
        
        if type_player =="dragon":
            pokemon_damage = self.dragon(type_enemy, puissance)
            self.damage_poke = pokemon_damage * (1 - defense // 200) 
            remaining_life  = pv - self.damage_poke
            print (f"Le pokemon inflige {self.damage_poke} dégats, l'autre avait {pv}HP, il lui reste {remaining_life }HP mais il avait {defense}de def")
            return remaining_life 
        
        if type_player =="tenebre":
            pokemon_damage = self.tenebre(type_enemy, puissance)
            self.damage_poke = pokemon_damage * (1 - defense // 200) 
            remaining_life  = pv - self.damage_poke
            print (f"Le pokemon inflige {self.damage_poke} dégats, l'autre avait {pv}HP, il lui reste {remaining_life }HP mais il avait {defense}de def")
            return remaining_life 
        
        if type_player =="fee":
            pokemon_damage = self.psy(type_enemy, puissance)
            self.damage_poke = pokemon_damage * (1 - defense // 200) 
            remaining_life  = pv - self.damage_poke
            print (f"Le pokemon inflige {self.damage_poke} dégats, l'autre avait {pv}HP, il lui reste {remaining_life }HP mais il avait {defense}de def")
            return remaining_life 
        
    def read_json(self):
        with open('add_json.json', 'r') as json_file:
            data = json.load(json_file)
            return data
        
    def random_pokemon(self):
        random_pokemon = random.choice(self.info_json)
        return {
            'numero': random_pokemon['numero'],
            'nom': random_pokemon['nom'],
            'type': random_pokemon['type'],
            'puissance': random_pokemon['puissance'],
            'pv': random_pokemon['pv'],
            'defense': random_pokemon['defense']
        }
        
    