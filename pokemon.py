import pygame,sys
class Pokemon:
    # def __init__(self, name, type, hp, level, attack_power, defense):
    #     self.name = name
    #     self.type = type
    #     self.hp = hp
    #     self.level = level
    #     self.attack_power = attack_power
    #     self.defense = defense
    
    def screen(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pokémon")
        self.clock = pygame.time.Clock()

    def pokemon_loop(self):
        self.screen()
        for event in pygame.event.get():
            if event == QUIT :
                pygame.quit()
                sys.exit()
        pygame.display.update()

    # def display_pokemon(self):
    #     img_pokemon = pygame.image.load("images/image-pokemon/pokedex1.png").convert_alpha()
section_pokemon = Pokemon()
section_pokemon.pokemon_loop()