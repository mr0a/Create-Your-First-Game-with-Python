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
