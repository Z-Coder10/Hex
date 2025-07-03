import pygame
pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Death Ray")

background_image = pygame.transform.scale(
    pygame.image.load("Untitled.jpg").convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)
player = pygame.transform.scale(
    pygame.image.load("player.jpg").convert_alpha(),(200,200)
)
player_rect = player.get_rect(center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2-30))
text = pygame.font.Font(None,36).render("Welcome to the Game!", True, (215,154,100))
text_rect = text.get_rect(center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2+110))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event .type == pygame.QUIT:
                running = False
        display_surface.blit(background_image,(0,0))
        display_surface.blit(player,player_rect)
        display_surface.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    game_loop()