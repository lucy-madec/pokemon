from type import Type
class Combat(Type):

    def __init__(self):
        Type.__init__(self)
  
    def attaque(self, pv, puissance, type_player, type_enemy, defense):
        if type_player =="feu":
            pokemon_damage = self.feu()
