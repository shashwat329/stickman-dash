import pygame
pygame.init()

# Set up the game window
window = pygame.display.set_mode((800, 300))
pygame.display.set_caption('stickman-dash')
# Load images
dino_img = pygame.image.load('stickman.png')
cactus_img = pygame.image.load('catcus.png')
# Define variables
dino_x = 50
dino_y = 200
dino_speed = 0
cactus_x = 800
cactus_y = 220
cactus_speed = 5
score = 0
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
   
               running = False

    # Move dino
    dino_y += dino_speed
    dino_speed += 0.0005
    if dino_y > 200:
        dino_y = 200
        dino_speed = 0

    # Move cactus
    cactus_x -= cactus_speed
    if cactus_x < -100:
        cactus_x = 800

    # Check for collision
    if cactus_x < dino_x + 60 < cactus_x + 50 and cactus_y < dino_y + 60 < cactus_y + 50:
        running = False

    # Update score
    score += 1

    # Draw images and text
    window.fill((255, 255, 255))
    window.blit(dino_img, (dino_x, dino_y))
    window.blit(cactus_img, (cactus_x, cactus_y))
    font = pygame.font.Font(None, 50)
    text = font.render('Score: ' + str(score), True, (0, 0, 0))
    window.blit(text, (600, 20))

    # Update display
    pygame.display.update()
# End game
font = pygame.font.Font(None, 100)
text = font.render('Game Over', True, (255, 0, 0))
window.blit(text, (200, 100))
font = pygame.font.Font(None, 50)
text = font.render('Score: ' + str(score), True, (0, 0,0))
