import pygame
from pygame import display, event, image
import game_configs as gc
from animal import Animal
from time import sleep

def find_index(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return index

pygame.init() # Too load the modules that we will be using in the game

display.set_caption("My Game") # Set caption for game window
screen = display.set_mode((512,512)) # This will return a screen which is a surface object. Anything to be shown in the window must be put on this object

matched = image.load('other_assets/matched.png') #This returns a surface element
#Use blit method to show a screen object over other screen object
#screen.blit(matched, (0, 0)) # Updating the screen
#This image is 512*512 hence fits entire screen
#Use flip() to update the screen to display
display.flip()

running = True #Boolean variable to stop game
#Instantiating Animal class
tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]
current_images = []

while running:
    # Pygame events module lets us to get list of keyboard and mouse events
    current_events = event.get()

    for e in current_events:
        #print(e)
        if e.type == pygame.QUIT: # event generated when user closes the game 
            running = False # Stop the game loop
        # Handling ESC key press
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
        
        #Handling Mouse events
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #print(mouse_x,mouse_y)
            index = find_index(mouse_x, mouse_y)
            if index not in current_images:
                current_images.append(index)
            if len(current_images) > 2:
                current_images = current_images[1:]
    screen.fill((255,255,255))

    total_skipped = 2

    for i, tile in enumerate(tiles):
        image_i = tile.image if i in current_images else tile.box
        if not tile.skip:
            screen.blit(image_i, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
        else:
            total_skipped += 1

    display.flip()


    if len(current_images) == 2:
        idx1, idx2 = current_images
        if tiles[idx1].name == tiles[idx2].name:
            tiles[idx1].skip = True
            tiles[idx2].skip = True
            sleep(0.4)
            screen.blit(matched, (0, 0))
            display.flip()
            sleep(0.4)
            current_images = []
            print(total_skipped)

        if total_skipped == len(tiles):
            running = False

print('Goodbye!')
