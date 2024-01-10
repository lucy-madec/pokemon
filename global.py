import pygame
class Global:

    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pokémon")
        self.clock = pygame.time.Clock()
        self.white = "#ffffff"
        self.grey = "#3c3c3c"   
        self.orange = "#ff6702"
        self.black = "#0e0f10"
        self.blue = "#375daa"
        self.police_c1 = pygame.font.Font("Pokemon Classic.ttf",10)
        self.police_c2 = pygame.font.Font("Pokemon Classic.ttf",15)        
        self.police_p1 = pygame.font.Font("Pixeled.ttf", 16)

    #def text  
    def text_c1(self,text, color, x, y):
        text_surface = self.police_c2.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def text_c2(self,text, color, x, y):
        text_surface = self.police_c1.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def text_p1(self,text, color, x, y):
        text_surface = self.police_p1.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    #def image
    def img_back(self,name,path,x,y):
        name =  pygame.image.load(path).convert_alpha()
        L_name, H_name = name.get_size()
        img_logo = pygame.transform.scale(img_logo, (L_name,H_name))
        x =(self.screen_width - L_name)//2
        y = (self.screen_height - H_name)//2
        self.screen.blit(name, (x, y))
    
    def img_pokemon(self,name,path,x,y):
        pass

        
    
