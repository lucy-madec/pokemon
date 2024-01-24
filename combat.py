from type_pok import Type
import json, random

class Combat(Type):
    
    def __init__(self):
        Type.__init__(self)
        # self.info_json = self.read_json()
        # self.pok_rival = 
        self.type_rival = self.pok_rival["type"]
        # self.pok_player = 
        self.puissance_player = self.pok_player["puissance"]

    def attack(self, pv, puissance, type_player, type_enemy, defense):
        
        with open('choix.json', 'r') as choix_file:
            choix_data = json.load(choix_file)
        if choix_data:
            pokemon_dict = choix_data[0]
            rival_dict = choix_data[1]

            name_pokemon= pokemon_dict["nom"]
            type_pokemon = pokemon_dict["type"]
            puissance_pokemon = pokemon_dict["puissance"]
            pv_pokemon = pokemon_dict["pv"]
            defense_pokemon = pokemon_dict["defense"]
            
            name_rival = rival_dict["nom"]
            type_rival = rival_dict["type"]
            puissance_rival = rival_dict["puissance"]
            pv_rival = rival_dict["pv"]
            defense_rival = rival_dict["defense"]

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
         