import pygame
pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adding image and background image")

background_image = pygame.transform.scale(
    pygame.image.load("Untitled.jpg").convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)
player = pygame.transform.scale(
    pygame.image.load("player.jpg").convert_alpha(),(200,200)
)
player_rect = player.get_rect(center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2-30))
text = pygame.font.Font(None,36).render("Welcome to the Game!", True, (215,200,224))