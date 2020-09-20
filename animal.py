import os, random
import game_configs as gc

from pygame import image, transform
#Create a dictionary for animals with its appearance count
animals_count = dict((a, 0) for a in gc.ASSET_FILES)

#Function to return list of animals which appeared less than twice
def available_animals():
    return [a for a,c in animals_count.items() if c<2]

class Animal:
    def __init__(self, index): #Index to show the image 0-15
        self.index = index
        self.row = index // gc.NUM_TILES_SIDE #0-3 in row1 and so
        self.col = index % gc.NUM_TILES_SIDE #0-3 for col
        self.name = random.choice(available_animals())
        animals_count[self.name] += 1

        self.image_path = os.path.join(gc.ASSET_DIR, self.name)
        self.image = image.load(self.image_path)
        #Transform image to appropriate size after removing margin
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - gc.MARGIN, gc.IMAGE_SIZE - gc.MARGIN))
        
        #In place of image we need to display a box of grey color
        self.box = self.image.copy()
        self.box.fill((200,200,200)) #RGB color to fill
        self.skip = False #Variable to skip printing matched variables

