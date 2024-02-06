class Type: 

    def normal(self, type_rival, damage):
        if type_rival == "roche" or type_rival == "acier":
            damage = damage // 2
            return damage

        elif type_rival == "normal" or type_rival == "feu" or type_rival == "eau" or type_rival == "plante" or type_rival == "electrique" or type_rival == "glace" or type_rival == "combat" or type_rival == "poison" or type_rival == "sol" or type_rival == "vol" or type_rival == "psy" or type_rival == "insecte" or type_rival == "spectre" or type_rival == "dragon" or type_rival == "tenebre" or type_rival == "fee":
            damage = damage
            return damage

    def feu(self, type_rival, damage): 
        if type_rival == "feu" or type_rival == "eau" or type_rival == "roche" or type_rival == "dragon":
            damage = damage // 2
            return damage
            
        elif type_rival == "plante" or type_rival == "glace" or type_rival == "insecte" or type_rival == "acier":
            damage = damage * 2
            return damage
            
        elif type_rival == "normal" or type_rival == "electrique"or type_rival == "combat" or type_rival == "poison" or type_rival == "sol" or type_rival == "vol" or type_rival == "psy" or type_rival == "spectre" or type_rival == "tenebre" or type_rival == "fee":
            damage = damage
            return damage
        
    def eau(self, type_rival, damage): 
        if type_rival == "eau" or type_rival == "plante" or type_rival == "dragon":
            damage = damage // 2
            return damage
            
        elif type_rival == "feu" or type_rival == "sol" or type_rival == "roche":
            damage = damage * 2
            return damage
            
        elif type_rival == "normal" or type_rival == "electrique" or type_rival == "glace" or type_rival == "combat" or type_rival == "poison" or type_rival == "vol" or type_rival == "psy" or type_rival == "insecte" or type_rival == "spectre" or type_rival == "tenebre" or type_rival == "acier" or type_rival == "fee":
            damage = damage
            return damage
        
    def plante(self, type_rival, damage): 
        if type_rival == "feu" or type_rival == "plante" or type_rival == "poison" or type_rival == "vol" or type_rival == "insecte" or type_rival == "dragon" or type_rival == "acier":
            damage = damage // 2
            return damage
            
        elif type_rival == "eau" or type_rival == "sol" or type_rival == "roche":
            damage = damage * 2
            return damage
            
        elif type_rival == "normal" or type_rival == "electrique" or type_rival == "glace" or type_rival == "combat" or type_rival == "psy" or type_rival == "spectre" or type_rival == "tenebre" or type_rival == "fee":
            damage = damage
            return damage
        
    def electrique(self, type_rival, damage): 
        
        if type_rival == "plante" or type_rival == "electrique" or type_rival == "dragon":
            damage = damage // 2
            return damage
            
        elif type_rival == "eau" or type_rival == "vol":
            damage = damage * 2
            return damage
            
        elif type_rival == "normal" or type_rival == "feu" or type_rival == "glace" or type_rival == "combat" or type_rival == "poison" or type_rival == "sol" or type_rival == "psy" or type_rival == "insecte" or type_rival == "roche" or type_rival == "spectre" or type_rival == "tenebre" or type_rival == "acier" or type_rival == "fee":
            damage = damage
            return damage
        
    def glace(self, type_rival, damage): 
        if type_rival == "feu" or type_rival == "eau"  or type_rival == "glace" or type_rival == "acier":
            damage = damage // 2
            return damage
            
        elif type_rival == "plante" or type_rival == "sol" or type_rival == "vol" or type_rival == "dragon":
            damage = damage * 2
            return damage
            
        elif type_rival == "normal" or type_rival == "electrique" or type_rival == "combat" or type_rival == "poison" or type_rival == "psy" or type_rival == "insecte" or type_rival == "roche" or type_rival == "spectre" or type_rival == "tenebre" or type_rival == "fee":
            damage = damage
            return damage

    def combat(self, type_rival, damage): 
        if type_rival == "poison" or type_rival == "vol"  or type_rival == "psy" or type_rival == "insecte" or type_rival == "fee":
            damage = damage // 2
            return damage
            
        elif type_rival == "normal" or type_rival == "glace" or type_rival == "roche" or type_rival == "tenebre" or type_rival == "acier":
            damage = damage * 2
            return damage
            
        elif type_rival == "feu" or type_rival == "eau" or type_rival == "plante" or type_rival == "electrique" or type_rival == "combat" or type_rival == "sol" or type_rival == "dragon":
            damage = damage
            return damage
        
    def poison(self, type_rival, damage):
        if type_rival == "poison" or type_rival == "sol" or type_rival == "roche" or type_rival == "spectre":
            damage = damage // 2
            return damage
            
        elif type_rival == "plante" or type_rival == "fee":
            damage = damage * 2
            return damage
            
        elif type_rival == "normal" or type_rival == "feu" or type_rival == "eau" or type_rival == "electrique" or type_rival == "glace" or type_rival == "combat" or type_rival == "vol" or type_rival == "psy" or type_rival == "insecte" or type_rival == "dragon" or type_rival == "tenebre" or type_rival == "acier":
            damage = damage
            return damage


    def sol(self, type_rival, damage): 
        if type_rival == "plante" or type_rival == "insecte":
            damage = damage // 2
            return damage
            
        elif type_rival == "feu" or type_rival == "electrique" or type_rival == "poison" or type_rival == "roche" or type_rival == "acier":
            damage = damage * 2
            return damage
            
        elif type_rival == "normal" or type_rival == "eau" or type_rival == "electrique" or type_rival == "glace" or type_rival == "combat" or type_rival == "sol" or type_rival == "vol" or type_rival == "psy" or type_rival == "spectre" or type_rival == "dragon" or type_rival == "tenebre" or type_rival == "fee":
            damage = damage
            return damage
        
    def vol(self, type_rival, damage): 
        if type_rival == "electrique" or type_rival == "roche" or type_rival == "acier" :
            damage = damage // 2
            return damage
            
        elif type_rival == "plante" or type_rival == "combat" or type_rival == "insecte":
            damage = damage * 2
            return damage
            
        elif type_rival == "normal" or type_rival == "feu" or type_rival == "eau" or type_rival == "glace" or type_rival == "poison" or type_rival == "sol" or type_rival == "vol" or type_rival == "psy" or type_rival == "spectre" or type_rival == "dragon" or type_rival == "tenebre" or type_rival == "fee":
            damage = damage
            return damage
    
    def psy(self, type_rival, damage): 
        if type_rival == "psy" or type_rival == "acier" :
            damage = damage // 2
            return damage
            
        elif type_rival == "combat" or type_rival == "poison":
            damage = damage * 2
            return damage
            
        elif type_rival == "normal" or type_rival == "feu" or type_rival == "eau" or type_rival == "plante" or type_rival == "electrique" or type_rival == "glace" or type_rival == "sol" or type_rival == "vol" or type_rival == "insecte" or type_rival == "roche"  or type_rival == "spectre" or type_rival == "dragon" or type_rival == "tenebre" or type_rival == "fee":
            damage = damage
            return damage
        
    def insecte(self, type_rival, damage): 
        if type_rival == "feu" or type_rival == "combat" or type_rival == "poison" or type_rival == "vol" or type_rival == "spectre" or type_rival == "acier" or type_rival == "fee":
            damage = damage // 2
            return damage
            
        elif type_rival == "plante" or type_rival == "psy" or type_rival == "tenebre":
            damage = damage * 2
            return damage
            
        elif type_rival == "normal" or type_rival == "eau" or type_rival == "electrique" or type_rival == "glace" or type_rival == "sol" or type_rival == "insecte" or type_rival == "roche" or type_rival == "dragon":
            damage = damage
            return damage
        
    def roche(self, type_rival, damage): 
        if type_rival == "combat" or type_rival == "sol" or type_rival == "acier":
            damage = damage // 2
            return damage
            
        elif type_rival == "feu" or type_rival == "glace" or type_rival == "vol" or type_rival == "insecte":
            damage = damage * 2
            return damage
            
        elif type_rival == "normal" or type_rival == "eau" or type_rival == "plante" or type_rival == "electrique" or type_rival == "poison" or type_rival == "psy" or type_rival == "roche" or type_rival == "spectre" or type_rival == "dragon" or type_rival == "tenebre" or type_rival == "fee":
            damage = damage
            return damage
        
    def spectre(self, type_rival, damage): 
        if type_rival == "tenebre" or type_rival == "acier":
            damage = damage // 2
            return damage
            
        elif type_rival == "psy" or type_rival == "spectre":
            damage = damage * 2
            return damage
            
        elif type_rival == "normal" or type_rival == "feu" or type_rival == "eau" or type_rival == "plante" or type_rival == "electrique" or type_rival == "glace" or type_rival == "combat" or type_rival == "poison" or type_rival == "sol" or type_rival == "vol" or type_rival == "insecte" or type_rival == "roche" or type_rival == "dragon":
            damage = damage
            return damage
        
    def dragon(self, type_rival, damage): 
        if type_rival == "acier":
            damage = damage // 2
            return damage
            
        elif type_rival == "dragon":
            damage = damage * 2
            return damage
            
        elif type_rival == "normal" or type_rival == "feu" or type_rival == "eau" or type_rival == "plante" or type_rival == "electrique" or type_rival == "glace" or type_rival == "combat" or type_rival == "poison" or type_rival == "sol" or type_rival == "vol" or type_rival == "psy" or type_rival == "insecte" or type_rival == "roche" or type_rival == "spectre" or type_rival == "tenebre" or type_rival == "fee":
            damage = damage
            return damage
    
    def tenebre(self, type_rival, damage): 
        if type_rival == "combat" or type_rival == "tenebre" or type_rival == "fee":
            damage = damage // 2
            return damage
            
        elif type_rival == "psy" or type_rival == "spectre":
            damage = damage * 2
            return damage
            
        elif type_rival == "normal" or type_rival == "feu" or type_rival == "eau" or type_rival == "plante" or type_rival == "electrique" or type_rival == "glace" or type_rival == "poison" or type_rival == "sol" or type_rival == "vol" or type_rival == "insecte" or type_rival == "roche" or type_rival == "dragon" or type_rival == "acier":
            damage = damage
            return damage
    
    def fee(self, type_rival, damage): 
        if type_rival == "feu" or type_rival == "poison" or type_rival == "acier":
            damage = damage // 2
            return damage
            
        elif type_rival == "combat" or type_rival == "dragon" or type_rival == "tenebre":
            damage = damage * 2
            return damage
            
        elif type_rival == "normal" or type_rival == "eau" or type_rival == "plante" or type_rival == "electrique" or type_rival == "glace" or type_rival == "sol" or type_rival == "vol" or type_rival == "psy" or type_rival == "insecte" or type_rival == "roche" or type_rival == "spectre" or type_rival == "fee":
            damage = damage
            return damage
        
