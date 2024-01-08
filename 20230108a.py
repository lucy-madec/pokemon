# Vanny 

# Importer les modules
import pygame
import button
pygame.init()

# Créer la fenêtre principale
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokémon")

# Variables du jeu
game_paused = False
menu_state = "main"

# Définir la police
font = pygame.font.SysFont("arial", 45)

# Définir la couleur
TEXT_COL = (255, 255, 255)

#Télécharger les images
logo_img = pygame.image.load("images/images-menu/menu1.png").convert()
resume_img = pygame.image.load("images/images-menu/button_video.png").convert()
options_img = pygame.image.load("images/images-menu/button_options.png").convert()
quit_img = pygame.image.load("images/images-menu/button_quit.png").convert()
video_img = pygame.image.load('images/images-menu/button_video.png').convert()
audio_img = pygame.image.load('images/images-menu/button_audio.png').convert()
keys_img = pygame.image.load('images/images-menu/button_keys.png').convert()
back_img = pygame.image.load('images/images-menu/button_back.png').convert()

# Créer les boutons
resume_button = button.Button(304, 125, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)
# logo_button = button.Button()

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

# Créer la boucle principale
run = True
while run:

  screen.fill((52, 78, 91))

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
      if options_button.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
      if video_button.draw(screen):
        print("Video Settings")
      if audio_button.draw(screen):
        print("Audio Settings")
      if keys_button.draw(screen):
        print("Change Key Bindings")
      if back_button.draw(screen):
        menu_state = "main"
  else:
    draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

  # Events
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()