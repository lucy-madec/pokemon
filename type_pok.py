class Type: 

    def __init__(self, type_rival, damage): 
        self.type_rival = type_rival
        self.damage = damage

    def normal(self):
        if self.type_rival == "roche" or self.type_rival == "acier":
            self.damage = self.damage // 2
            print(self.damage)
            print(self.type_rival)
            return self.damage

        elif type == "normal" or type == "feu" or type == "eau" or type == "plante" or type == "electrique" or type == "glace" or type == "combat" or type == "poison" or type == "sol" or type == "vol" or type == "psy" or type == "insecte" or type == "spectre" or type == "dragon" or type == "tenebres" or type == "fee":
            self.damage = self.damage
            print(self.damage)
            print(self.type_rival)
            return self.damage

    def feu(self, type, damage): 
        if type == "feu" or type == "eau" or type == "roche" or type == "dragon":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "plante" or type == "glace" or type == "insecte" or type == "acier":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "electrique"or type == "combat" or type == "poison" or type == "sol" or type == "vol" or type == "psy" or type == "spectre" or type == "tenebres" or type == "fee":
            damage = damage
            print(damage)
            print(type)
            return damage
        
    def eau(self, type, damage): 
        if type == "eau" or type == "plante" or type == "dragon":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "feu" or type == "sol" or type == "roche":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "electrique" or type == "glace" or type == "combat" or type == "poison" or type == "vol" or type == "psy" or type == "insecte" or type == "spectre" or type == "tenebres" or type == "acier" or type == "fee":
            damage = damage
            print(damage)
            print(type)
            return damage
        
    def plante(self, type, damage): 
        if type == "feu" or type == "plante" or type == "poison" or type == "vol" or type == "insecte" or type == "dragon" or type == "acier":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "eau" or type == "sol" or type == "roche":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "electrique" or type == "glace" or type == "combat" or type == "psy" or type == "spectre" or type == "tenebres" or type == "fee":
            damage = damage
            print(damage)
            print(type)
            return damage
        
    def electrique(self, type, damage): 
        
        if type == "plante" or type == "electrique" or type == "dragon":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "eau" or type == "vol":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "feu" or type == "glace" or type == "combat" or type == "poison" or type == "sol" or type == "psy" or type == "insecte" or type == "roche" or type == "spectre" or type == "tenebres" or type == "acier" or type == "fee":
            damage = damage
            print(damage)
            print(type)
            return damage
        
    def glace(self, type, damage): 
        if type == "feu" or type == "eau"  or type == "glace" or type == "acier":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "plante" or type == "sol" or type == "vol" or type == "dragon":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "electrique" or type == "combat" or type == "poison" or type == "psy" or type == "insecte" or type == "roche" or type == "spectre" or type == "tenebres" or type == "fee":
            damage = damage
            print(damage)
            print(type)
            return damage

    def combat(self, type, damage): 
        if type == "poison" or type == "vol"  or type == "psy" or type == "insecte" or type == "fee":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "glace" or type == "roche" or type == "tenebres" or type == "acier":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "feu" or type == "eau" or type == "plante" or type == "electrique" or type == "combat" or type == "sol" or type == "dragon":
            damage = damage
            print(damage)
            print(type)
            return damage
        
    def poison(self, type, damage):
        if type == "poison" or type == "sol" or type == "roche" or type == "spectre":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "plante" or type == "fee":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "feu" or type == "eau" or type == "electrique" or type == "glace" or type == "combat" or type == "vol" or type == "psy" or type == "insecte" or type == "dragon" or type == "tenebres" or type == "acier":
            damage = damage
            print(damage)
            print(type)
            return damage


    def sol(self, type, damage): 
        if type == "plante" or type == "insecte":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "feu" or type == "electrique" or type == "poison" or type == "roche" or type == "acier":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "eau" or type == "electrique" or type == "glace" or type == "combat" or type == "sol" or type == "vol" or type == "psy" or type == "spectre" or type == "dragon" or type == "tenebres" or type == "fee":
            damage = damage
            print(damage)
            print(type)
            return damage
        
    def vol(self, type, damage): 
        if type == "electrique" or type == "roche" or type == "acier" :
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "plante" or type == "combat" or type == "insecte":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "feu" or type == "eau" or type == "glace" or type == "poison" or type == "sol" or type == "vol" or type == "psy" or type == "spectre" or type == "dragon" or type == "tenebres" or type == "fee":
            damage = damage
            print(damage)
            print(type)
            return damage
    
    def psy(self, type, damage): 
        if type == "psy" or type == "acier" :
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "combat" or type == "poison":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "feu" or type == "eau" or type == "plante" or type == "electrique" or type == "glace" or type == "sol" or type == "vol" or type == "insecte" or type == "roche"  or type == "spectre" or type == "dragon" or type == "tenebres" or type == "fee":
            damage = damage
            print(damage)
            print(type)
            return damage
        
    def insecte(self, type, damage): 
        if type == "feu" or type == "combat" or type == "poison" or type == "vol" or type == "spectre" or type == "acier" or type == "fee":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "plante" or type == "psy" or type == "tenebres":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "eau" or type == "electrique" or type == "glace" or type == "sol" or type == "insecte" or type == "roche" or type == "dragon":
            damage = damage
            print(damage)
            print(type)
            return damage
        
    def roche(self, type, damage): 
        if type == "combat" or type == "sol" or type == "acier":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "feu" or type == "glace" or type == "vol" or type == "insecte":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "eau" or type == "plante" or type == "electrique" or type == "poison" or type == "psy" or type == "roche" or type == "spectre" or type == "dragon" or type == "tenebres" or type == "fee":
            damage = damage
            print(damage)
            print(type)
            return damage
    
    def dragon(self, type, damage): 
        if type == "acier":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "dragon":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "feu" or type == "eau" or type == "plante" or type == "electrique" or type == "glace" or type == "combat" or type == "poison" or type == "sol" or type == "vol" or type == "psy" or type == "insecte" or type == "roche" or type == "spectre" or type == "tenebres" or type == "fee":
            damage = damage
            print(damage)
            print(type)
            return damage
    
    def tenebres(self, type, damage): 
        if type == "combat" or type == "tenebres" or type == "fee":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "psy" or type == "spectre":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "feu" or type == "eau" or type == "plante" or type == "electrique" or type == "glace" or type == "poison" or type == "sol" or type == "vol" or type == "insecte" or type == "roche" or type == "dragon" or type == "acier":
            damage = damage
            print(damage)
            print(type)
            return damage
    
    def fee(self, type, damage): 
        if type == "feu" or type == "poison" or type == "acier":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "combat" or type == "dragon" or type == "tenebres":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "eau" or type == "plante" or type == "electrique" or type == "glace" or type == "sol" or type == "vol" or type == "psy" or type == "insecte" or type == "roche" or type == "spectre" or type == "fee":
            damage = damage
            print(damage)
            print(type)
            return damage