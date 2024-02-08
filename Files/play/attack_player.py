from Files.play.type_pok import Type
class Attack_player(Type):
    
    def __init__(self):
        Type.__init__(self)
        self.remaining_life_enemy = 0
        self.att = False
        
    def pv_start(self,pv):
        if self.att == False:
            self.remaining_life_enemy = pv
            self.att = True
            return self.remaining_life_enemy
        else:
            pass
        
    def attack_p(self, pv, puissance, type_player, type_enemy, defense,name_pok,name_rival):

            if type_player =="normal":
                pokemon_damage = self.normal(type_enemy, puissance)
                damage_poke = pokemon_damage - (defense // 200)
                self.remaining_life_enemy  = pv - damage_poke
                print (f"{name_pok} inflige {damage_poke} dégats,{name_rival} avait {pv} HP, il lui reste {self.remaining_life_enemy }HP mais il avait {defense}de def")
                if self.remaining_life_enemy <= 0:
                    self.remaining_life_enemy = 0
                return self.remaining_life_enemy

            if type_player =="feu":
                pokemon_damage = self.feu(type_enemy, puissance)
                self.damage_poke = pokemon_damage - (defense // 200) 
                self.remaining_life_enemy  = pv - self.damage_poke
                print (f"{name_pok} inflige {self.damage_poke} dégats,{name_rival} avait {pv} HP, il lui reste {self.remaining_life_enemy }HP mais il avait {defense}de def")
                if self.remaining_life_enemy <= 0:
                    self.remaining_life_enemy = 0
                return self.remaining_life_enemy 
            
            if type_player =="eau":
                pokemon_damage = self.eau(type_enemy, puissance)
                self.damage_poke = pokemon_damage - (defense // 200) 
                self.remaining_life_enemy  = pv - self.damage_poke
                print (f"{name_pok} inflige {self.damage_poke} dégats,{name_rival} avait {pv} HP, il lui reste {self.remaining_life_enemy }HP mais il avait {defense}de def")
                if self.remaining_life_enemy <= 0:
                    self.remaining_life_enemy = 0
                return self.remaining_life_enemy 
            
            if type_player =="plante":
                pokemon_damage = self.plante(type_enemy, puissance)
                self.damage_poke = pokemon_damage - (defense // 200) 
                self.remaining_life_enemy  = pv - self.damage_poke
                print (f"{name_pok} inflige {self.damage_poke} dégats,{name_rival} avait {pv} HP, il lui reste {self.remaining_life_enemy }HP mais il avait {defense}de def")
                if self.remaining_life_enemy <= 0:
                    self.remaining_life_enemy = 0
                return self.remaining_life_enemy 
            
            if type_player =="electrique":
                pokemon_damage = self.electrique(type_enemy, puissance)
                self.damage_poke = pokemon_damage - (defense // 200) 
                self.remaining_life_enemy  = pv - self.damage_poke
                print (f"{name_pok} inflige {self.damage_poke} dégats,{name_rival} avait {pv} HP, il lui reste {self.remaining_life_enemy }HP mais il avait {defense}de def")
                if self.remaining_life_enemy <= 0:
                    self.remaining_life_enemy = 0
                return self.remaining_life_enemy 

            if type_player =="glace":
                pokemon_damage = self.glace(type_enemy, puissance)
                self.damage_poke = pokemon_damage - (defense // 200) 
                self.remaining_life_enemy  = pv - self.damage_poke
                print (f"{name_pok} inflige {self.damage_poke} dégats,{name_rival} avait {pv} HP, il lui reste {self.remaining_life_enemy }HP mais il avait {defense}de def")
                if self.remaining_life_enemy <= 0:
                    self.remaining_life_enemy = 0
                return self.remaining_life_enemy 
            
            if type_player =="combat":
                pokemon_damage = self.combat(type_enemy, puissance)
                self.damage_poke = pokemon_damage - (defense // 200) 
                self.remaining_life_enemy  = pv - self.damage_poke
                print (f"{name_pok} inflige {self.damage_poke} dégats,{name_rival} avait {pv} HP, il lui reste {self.remaining_life_enemy }HP mais il avait {defense}de def")
                if self.remaining_life_enemy <= 0:
                    self.remaining_life_enemy = 0
                return self.remaining_life_enemy 
            
            if type_player =="poison":
                pokemon_damage = self.poison(type_enemy, puissance)
                self.damage_poke = pokemon_damage - (defense // 200) 
                self.remaining_life_enemy  = pv - self.damage_poke
                print (f"{name_pok} inflige {self.damage_poke} dégats,{name_rival} avait {pv}HP, il lui reste {self.remaining_life_enemy }HP mais il avait {defense}de def")
                if self.remaining_life_enemy <= 0:
                    self.remaining_life_enemy = 0
                return self.remaining_life_enemy 
            
            if type_player =="sol":
                pokemon_damage = self.sol(type_enemy, puissance)
                self.damage_poke = pokemon_damage - (defense // 200) 
                self.remaining_life_enemy  = pv - self.damage_poke
                print (f"{name_pok} inflige {self.damage_poke} dégats,{name_rival} avait {pv}HP, il lui reste {self.remaining_life_enemy }HP mais il avait {defense}de def")
                if self.remaining_life_enemy <= 0:
                    self.remaining_life_enemy = 0
                return self.remaining_life_enemy 
            
            if type_player =="vol":
                pokemon_damage = self.vol(type_enemy, puissance)
                self.damage_poke = pokemon_damage - (defense // 200) 
                self.remaining_life_enemy  = pv - self.damage_poke
                print (f"{name_pok} inflige {self.damage_poke} dégats,{name_rival} avait {pv}HP, il lui reste {self.remaining_life_enemy }HP mais il avait {defense}de def")
                if self.remaining_life_enemy <= 0:
                    self.remaining_life_enemy = 0
                return self.remaining_life_enemy 
            
            if type_player =="psy":
                pokemon_damage = self.psy(type_enemy, puissance)
                self.damage_poke = pokemon_damage - (defense // 200) 
                self.remaining_life_enemy  = pv - self.damage_poke
                print (f"{name_pok} inflige {self.damage_poke} dégats,{name_rival} avait {pv}HP, il lui reste {self.remaining_life_enemy }HP mais il avait {defense}de def")
                if self.remaining_life_enemy <= 0:
                    self.remaining_life_enemy = 0
                return self.remaining_life_enemy 
            
            if type_player =="insecte":
                pokemon_damage = self.eau(type_enemy, puissance)
                self.damage_poke = pokemon_damage - (defense // 200) 
                self.remaining_life_enemy  = pv - self.damage_poke
                print (f"{name_pok} inflige {self.damage_poke} dégats,{name_rival} avait {pv}HP, il lui reste {self.remaining_life_enemy }HP mais il avait {defense}de def")
                if self.remaining_life_enemy <= 0:
                    self.remaining_life_enemy = 0
                return self.remaining_life_enemy 
                    
            if type_player =="roche":
                pokemon_damage = self.roche(type_enemy, puissance)
                self.damage_poke = pokemon_damage - (defense // 200) 
                self.remaining_life_enemy  = pv - self.damage_poke
                print (f"{name_pok} inflige {self.damage_poke} dégats,{name_rival} avait {pv}HP, il lui reste {self.remaining_life_enemy }HP mais il avait {defense}de def")
                if self.remaining_life_enemy <= 0:
                    self.remaining_life_enemy = 0
                return self.remaining_life_enemy 
            
            if type_player =="spectre":
                pokemon_damage = self.spectre(type_enemy, puissance)
                damage_poke = pokemon_damage - (defense // 200)
                self.remaining_life_player  = pv - damage_poke
                print (f"{name_pok} inflige {damage_poke} dégats,{name_rival} avait {pv} HP, il lui reste {self.remaining_life_player }HP mais il avait {defense}de def")
                if self.remaining_life_player <= 0:
                    self.remaining_life_player = 0
                return self.remaining_life_player
            
            if type_player =="dragon":
                pokemon_damage = self.dragon(type_enemy, puissance)
                self.damage_poke = pokemon_damage - (defense // 200) 
                self.remaining_life_enemy  = pv - self.damage_poke
                print (f"{name_pok} inflige {self.damage_poke} dégats,{name_rival} avait {pv}HP, il lui reste {self.remaining_life_enemy }HP mais il avait {defense}de def")
                if self.remaining_life_enemy <= 0:
                    self.remaining_life_enemy = 0
                return self.remaining_life_enemy 
            
            if type_player =="tenebre":
                pokemon_damage = self.tenebre(type_enemy, puissance)
                self.damage_poke = pokemon_damage - (defense // 200) 
                self.remaining_life_enemy  = pv - self.damage_poke
                print (f"{name_pok} inflige {self.damage_poke} dégats,{name_rival} avait {pv}HP, il lui reste {self.remaining_life_enemy }HP mais il avait {defense}de def")
                if self.remaining_life_enemy <= 0:
                    self.remaining_life_enemy = 0
                return self.remaining_life_enemy 
            
            if type_player =="fee":
                pokemon_damage = self.psy(type_enemy, puissance)
                self.damage_poke = pokemon_damage - (defense // 200) 
                self.remaining_life_enemy  = pv - self.damage_poke
                print (f"{name_pok} inflige {self.damage_poke} dégats,{name_rival} avait {pv}HP, il lui reste {self.remaining_life_enemy }HP mais il avait {defense}de def")
                if self.remaining_life_enemy <= 0:
                    self.remaining_life_enemy = 0
                return self.remaining_life_enemy 
        