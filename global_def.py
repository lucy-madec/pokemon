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
        self.yellow = "#ffcc01"
        self.green = "#488030"
        self.brown = "#e09828"
        self.pink = "#f8a8b0"
        self.police_c1 = pygame.font.Font("Pokemon Classic.ttf",10)
        self.police_c2 = pygame.font.Font("Pokemon Classic.ttf",15)  
        self.police_c3 = pygame.font.Font("Pokemon Classic.ttf",50)
        self.police_c4 = pygame.font.Font("Pokemon Classic.ttf",5)  
        self.police_c5 = pygame.font.Font("Pokemon Classic.ttf",35)    
        self.police_c6 = pygame.font.Font("Pokemon Classic.ttf", 12)    
        self.police_p1 = pygame.font.Font("Pixeled.ttf", 16)
        self.lst_name = []
        
#def text  
    def text_c1(self,text, color, x, y):
        text_surface = self.police_c1.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def text_c2(self,text, color, x, y):
        text_surface = self.police_c2.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def text_c3(self,text, color, x, y):
        text_surface = self.police_c3.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def text_c4(self,text, color, x, y):
        text_surface = self.police_c4.render(text, True, color)
        self.screen.blit(text_surface, (x, y))
        
    def text_c5(self,text, color, x, y):
        text_surface = self.police_c5.render(text, True, color)
        self.screen.blit(text_surface, (x, y))
    
    def text_c6(self,text, color, x, y):
        text_surface = self.police_c6.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def text_p1(self,text, color, x, y):
        text_surface = self.police_p1.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

#def image
    def img_pokemon(self,name,path,a,b,x,y):
        name = pygame.image.load(path)
        name = name.convert_alpha()
        name = pygame.transform.scale(name,(a,b))        
        self.screen.blit(name,(x,y))
        
    def img_back(self,name,path):
        name =  pygame.image.load(path).convert_alpha()
        L_name, H_name = name.get_size()
        name = pygame.transform.scale(name, (L_name,H_name))
        x =(self.screen_width - L_name)//2
        y = (self.screen_height - H_name)//2
        self.screen.blit(name, (x, y))
    
# def rectangle        
        # Rectangle 
    def rect(self,nom, x1,y1,x2,y2):   
        nom = pygame.Rect(x1,y1,x2,y2)

              # Rectangle Radius
    def rect_radius(self,radius,color,x1,y1,x2,y2):
        r = radius
        pygame.draw.rect(self.screen,color,(x1,y1,x2,y2),border_radius = r)

# Liste
    def addd_name(self,name):
        self.add_name.append(name)
        print(self.add_name)
