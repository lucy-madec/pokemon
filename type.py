class Type: 

    def __init__(self, type, damage): 
        self.type = type
        self.damage = damage

    def normal(self, type, damage):
        if type == "normal" or type == "feu" or type == "eau" or type == "plante" or type == "electrique" or type == "sol" or type == "vol" or type == "insecte":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
        
    def feu(self, type, damage): 
        if type == "feu" or type == "eau":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "plante" or type == "insecte":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "elec" or type == "sol" or type == "vol":
            damage = damage
            print(damage)
            print(type)
            return damage
        
    def eau(self, type, damage): 
        if type == "eau" or type == "plante":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "feu" or type == "sol":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "electrique" or type == "vol" or type == "insecte":
            damage = damage
            print(damage)
            print(type)
            return damage
        
    def plante(self, type, damage): 
        if type == "plante" or type == "feu" or type == "sol" or type == "insecte":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "eau" or type == "sol":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "" or type == "elec" or type == "sol" or type == "vol":
            damage = damage
            print(damage)
            print(type)
            return damage
        
    def electrique(self, type, damage): 
        
        if type == "plante" or type == "electrique":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "eau" or type == "vol":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "feu" or type == "insecte":
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
            
        elif type == "normal" or type == "electrique" or type == "combat" or type == "poison" or type == "psy" or type == "insecte" or type == "roche" or type == "spectre":
            damage = damage
            print(damage)
            print(type)
            return damage

    def combat(self, type, damage): 
        if type == "poison" or type == "vol"  or type == "psy" or type == "insecte":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "poison" or type == "vol" or type == "psy" or type == "insecte":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "feu" or type == "eau" or type == "plante" or type == "electrique" or type == "combat" or type == "sol":
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
            
        elif type == "feu" or type == "electrique":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "eau" or type == "sol" or type == "vol":
            damage = damage
            print(damage)
            print(type)
            return damage

    # def fee(self, type, damage): 
    #     if type == "feu" or type == "eau":
    #         damage = damage // 2
    #         print(damage)
    #         print(type)
    #         return damage
            
    #     elif type == "plante" or type == "insecte":
    #         damage = damage * 2
    #         print(damage)
    #         print(type)
    #         return damage
            
    #     elif type == "normal" or type == "elec" or type == "sol" or type == "vol":
    #         damage = damage
    #         print(damage)
    #         print(type)
    #         return damage
        
    # def poison(self, type, damage): 
    #     if type == "feu" or type == "eau"  or type == "glace" or type == "acier":
    #         damage = damage // 2
    #         print(damage)
    #         print(type)
    #         return damage
            
    #     elif type == "plante" or type == "sol" or type == "vol" or type == "dragon":
    #         damage = damage * 2
    #         print(damage)
    #         print(type)
    #         return damage
            
    #     elif type == "normal" or type == "electrique" or type == "combat" or type == "poison" or type == "psy" or type == "insecte" or type == "roche" or type == "spectre":
    #         damage = damage
    #         print(damage)
    #         print(type)
    #         return damage


    def sol(self, type, damage): 
        if type == "plante" or type == "insecte":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "feu" or type == "electrique":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "eau" or type == "sol":
            damage = damage
            print(damage)
            print(type)
            return damage

    def vol(self, type, damage): 
        if type == "electrique":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "plante" or type == "insecte":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "feu" or type == "eau" or type == "sol":
            damage = damage
            print(damage)
            print(type)
            return damage
        
    # def psy(self, type, damage): 
    #     if type == "plante" or type == "insecte":
    #         damage = damage // 2
    #         print(damage)
    #         print(type)
    #         return damage
            
    #     elif type == "feu" or type == "electrique":
    #         damage = damage * 2
    #         print(damage)
    #         print(type)
    #         return damage
            
    #     elif type == "normal" or type == "eau" or type == "sol":
    #         damage = damage
    #         print(damage)
    #         print(type)
    #         return damage
        
    # def insecte(self, type, damage): 
    #     if type == "plante" or type == "insecte":
    #         damage = damage // 2
    #         print(damage)
    #         print(type)
    #         return damage
            
    #     elif type == "feu" or type == "electrique":
    #         damage = damage * 2
    #         print(damage)
    #         print(type)
    #         return damage
            
    #     elif type == "normal" or type == "eau" or type == "sol":
    #         damage = damage
    #         print(damage)
    #         print(type)
    #         return damage
        

    # def roche(self, type, damage): 
    #     if type == "plante" or type == "insecte":
    #         damage = damage // 2
    #         print(damage)
    #         print(type)
    #         return damage
            
    #     elif type == "feu" or type == "electrique":
    #         damage = damage * 2
    #         print(damage)
    #         print(type)
    #         return damage
            
    #     elif type == "normal" or type == "eau" or type == "sol":
    #         damage = damage
    #         print(damage)
    #         print(type)
    #         return damage
        
    # def spectre(self, type, damage): 
    #     if type == "plante" or type == "insecte":
    #         damage = damage // 2
    #         print(damage)
    #         print(type)
    #         return damage
            
    #     elif type == "feu" or type == "electrique":
    #         damage = damage * 2
    #         print(damage)
    #         print(type)
    #         return damage
            
    #     elif type == "normal" or type == "eau" or type == "sol":
    #         damage = damage
    #         print(damage)
    #         print(type)
    #         return damage
        
    # def dragon(self, type, damage): 
    #     if type == "plante" or type == "insecte":
    #         damage = damage // 2
    #         print(damage)
    #         print(type)
    #         return damage
            
    #     elif type == "feu" or type == "electrique":
    #         damage = damage * 2
    #         print(damage)
    #         print(type)
    #         return damage
            
    #     elif type == "normal" or type == "eau" or type == "sol":
    #         damage = damage
    #         print(damage)
    #         print(type)
    #         return damage




    def tenebre(self, type, damage): 
        if type == "combat" or type == "ténèbre" or type == "acier":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "psy" or type == "spectre":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "feu" or type == "eau" or type == "plante"  or type == "electrique"  or type == "glace" or type == "poison"  or type == "sol"  or type == "vol":
            damage = damage
            print(damage)
            print(type)
            return damage
        
    def acier(self, type, damage): 
        if type == "plante" or type == "insecte":
            damage = damage // 2
            print(damage)
            print(type)
            return damage
            
        elif type == "feu" or type == "electrique":
            damage = damage * 2
            print(damage)
            print(type)
            return damage
            
        elif type == "normal" or type == "eau" or type == "sol":
            damage = damage
            print(damage)
            print(type)
            return damage


    
    
    