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

    font_menu = pygame.font.Font(None, 36) 

    options = ["PLAY", "ADD POKEMON", "POKEDEX", "QUIT"]
  

    while running:      

        white = "#ffffff"
        screen.blit(img_back, (0,0)) 
      
        pygame.draw.rect(screen, white, (50, 100, 200, 50))
        pygame.draw.rect(screen, white, (50, 200, 200, 50))
        pygame.draw.rect(screen, white, (50, 300, 200, 50))
        pygame.draw.rect(screen, white, (50, 400, 200, 50))

        for i, option_text in enumerate(options):

            text_render = font_menu.render(option_text, True, (0, 0, 0))  # Couleur du texte: noir
            text_rect = text_render.get_rect(center=(screen_width // 2, 125 + i * 150))  # Position du texte centré

            screen.blit(text_render, text_rect)

        # Code pour gérer les interactions avec les options du menu ici

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
