# Importer les modules
import pygame, time
pygame.init()

# Ecran principal
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokémon")

# Fonctions principales du menu
def afficher_menu(screen):
    running = True
    clock = pygame.time.Clock()
    start_time = time.time()

    
    while running:
        white = "#ffffff"
        screen.fill(white)
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time < 2 :
            img_logo =  pygame.image.load("images/images-menu/menu1.png").convert_alpha() 
            L_img_logo, H_img_logo = img_logo.get_size()                    
            img_logo = pygame.transform.scale(img_logo, (L_img_logo, H_img_logo))            
            x =(screen_width - L_img_logo)//2
            y = (screen_height - H_img_logo)//2
            screen.blit(img_logo, (x, y))
        else:
            break

        pygame.display.flip()
        clock.tick(60)

def afficher_options(screen): 

    running = True
    clock = pygame.time.Clock()
    
    img_back = pygame.image.load("images/images-menu/menu2.jpg").convert()

  

    while running:      

        white = "#ffffff"
        grey = "#3c3c3c"
        option_radius = 10
        screen.blit(img_back, (0,0)) 
        font = pygame.font.Font(None, 30)
      
        menu_play = font.render("PLAY", True, grey)
        menu_add = font.render("ADD POKEMON", True, grey)
        menu_pokedex = font.render("POKEDEX", True, grey)
        menu_quit = font.render("QUIT", True, grey)
        
        pygame.draw.rect(screen, white, (50, 100, 200, 50), border_radius=option_radius)
        screen.blit(menu_play, (60, 110))

        pygame.draw.rect(screen, white, (50, 200, 200, 50), border_radius=option_radius)
        screen.blit(menu_add, (60, 210))

        pygame.draw.rect(screen, white, (50, 300, 200, 50), border_radius=option_radius)
        screen.blit(menu_pokedex, (60, 310))

        pygame.draw.rect(screen, white, (50, 400, 200, 50), border_radius=option_radius)
        screen.blit(menu_quit, (60, 410))


        # Pour l'exemple, quittez le jeu si la touche "Escape" est pressée
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False


        # pygame.display.flip()
        pygame.display.update()
        clock.tick(60)

def main():
    afficher_menu(screen)
    afficher_options(screen)

    pygame.quit()

if __name__ == "__main__":
    main()
