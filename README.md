# Create-Your-First-Game-with-Python
> This is a project based course from coursera.  
Expecting to learn some basics of building games using python.

> Starting time : 12:35 PM 17 Sep 2020
## Video 1: Introduction
> Introduction to pygame (a package for gamedevelopment with python).  
The game we are going to build in this project is a image memorization game.
Introduction to Rhyme platform.

## Video 2: Project Setup
> For image assets refer [Kenny](https://www.kenney.nl)'s website.

* Open the project folder which contains the assets in vscode with `code .` in terminal.
* In this folder we will create 3 files (name as you wish):  
  >
   - app.py - To contian the game logic.  
   - game_configs.py - To contain game configs and global constants for our game.  
   - animal.py - To contain our custom class.

## Video 3: Initialization and game loop

* After the initialization the game loop continues to run until user explicitly exits the loop.
* The game loop will have the games logic and also act on users input.
* Lets Start coding.
> app.py
```python
import pygame
from pygame import display, event

pygame.init() # Too load the modules that we will be using in the game

display.set_caption("My Game") # Set caption for game window
# Set size of screen which is a surface object
screen = display.set_mode((512,512)) #Anything to be shown in the window must be put on this object
running = True #Boolean variable to stop game

while running:
    # Pygame events module lets us to get list of keyboard and mouse events
    current_events = event.get()

    for e in current_events:
        #print(e) # Try to see the events happened over our window
        if e.type == pygame.QUIT: # event generated when user closes the game 
            running = False # Stop the game loop
    
print('Goodbye!') #Message to print after quiting the game
```

* Open the terminal in the projects folder and run `python3 app.py` to check the game window and game loop
* **Now we have learned to create ***game window and game loop*** using pygame**

## Video 4: Images, Blit and Flip
* Here we will learn to load and display images in pygame using image module. 
* Before moving to that lets set some constants and create list of asset files for our game
> game_configs.py
```python3
import os

IMAGE_SIZE = 128
SCREEN_SIZE = 512
NUM_TILES_SIDE = 4 # Tiles in game per row
NUM_TILES_TOTAL = 16 # Total tiles in game
MARGIN = 4

ASSET_DIR = 'assets' # Name of directory of assets
# Create a list of asset files
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']

assert len(ASSET_FILES) == 8 #Make sure 8 files present
```
* Now lets show the image with text matched in our window.
> app.py
```python3
...
from pygame import display, event, image
...
#Below screen
matched = image.load('other_assets/matched.png')
screen.blit(matched, (0, 0))
display.flip()
```
* Now we have learned to **load images** and **update images in screen** and then to the display.

## Video 5: Animal Class
* Now we will work on our Animal class to create a name and index for each animal image. Each animal image must be instantiated twice.
> animal.py
```python3
import os, random
import game_configs as gc
from animal import Animal

from pygame import image, transform
#Create a dictionary for animals with its count
animals_count = dict((a, 0) for a in gc.ASSET_FILES)

#Function to return list of animals which appeared less than twice
def available_animals():
    return [a for a,c in animals_count.items() if c<2]

class Animal:
    def __init__(self, index): #index(0-15) to show the image
        self.index = index
        self.row = index // gc.NUM_TILES_SIDE #0-3 in row1 and so on
        self.col = index % gc.NUM_TILES_SIDE #0-3 for col
        self.name = random.choice(available_animals()) #Choose a animal from list randomly
        animals_count[self.name] += 1 #Increase the count for that animal

        self.image_path = os.path.join(gc.ASSET_DIR, self.name) #Image path
        self.image = image.load(self.image_path) #Loading the image using pygame
        #Transform image to appropriate size after removing margin
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))
        
        #In place of image we need to display a box of grey color
        self.box = self.image.copy()
        self.box.fill((200,200,200)) #RGB color to fill
        self.skip = False #Variable to skip printing matched variables
```
* Now we have defined the Animal class

## Video 6: Displaying Animal Images
* Lets start working on our game logic.
> Creating a list of images  
`tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]`

> Fill screen with grey color and place all the images on the screen.
`screen.fill((255,255,255))`

> Set images in the screen with height and width
```python3
for tile in tiles:
  screen.blit(tile.image, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
display.flip()
```
* Congratulations now you have created the ***game loop, game window, placed the images on the window***.

## Video 7: Handling Mouse Events
* Get the index of the image by mouseclick
```python3
def find_index(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return index
    
if e.type == pygame.MOUSEBUTTONDOWN:
  mouse_x, mouse_y = pygame.mouse.get_pos()
  #print(mouse_x,mouse_y)
  index = find_index(mouse_x, mouse_y)
  print(index)
  ```
* Now we have got the index of the image clicked

## Displaying Recent Images
* To display the last two tiles selected we need to have a list of selected tiles.
`current_images = []`
* Updating current_images to the last two images(index) clicked in the mouse handling.
```python3
if len(current_images) > 2:
  current_images = current_images[1:]
```
* Showing only last two images and checking if both images are same
```python3
for i, tile in enumerate(tiles):
        image_i = tile.image if i in current_images else tile.box
        if not tile.skip:
            screen.blit(image_i, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))

    if len(current_images) == 2:
        idx1, idx2 = current_images
        if tiles[idx1].name == tiles[idx2].name:
            tiles[idx1].skip = True
            tiles[idx2].skip = True

    display.flip()
```

## Video 9: Final Touches
*

Finished at 7 PM 17 Sep
