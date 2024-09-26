from os import walk
from os.path import join
from settings import *


def import_image(*path: str, alpha: bool = True, format: str = 'png') -> pygame.Surface:
	"""
	Do: Loads a single image from a specified file path.

	Return: Surface.
	"""
	full_path = join(*path) + f'.{format}'
	surf = pygame.image.load(full_path).convert_alpha() if alpha else pygame.image.load(full_path).convert()
	return surf


def import_tilemap(cols: int, rows: int, *path: str) -> dict:
	"""
	Do: Loads a tilemap (or spritesheet) and splits it into smaller tiles based on the number of columns and rows.
	
	Return: Dictionary where the keys are (column, row) coordinates of each tile,
	and the values are the corresponding tile surfaces.

	{ (column, row): Surface }
	"""
	frames = {}
	surf = import_image(*path)
	cell_width, cell_height = surf.get_width() / cols, surf.get_height() / rows
	for col in range(cols):
		for row in range(rows):
			cutout_rect = pygame.Rect(col * cell_width, row * cell_height,cell_width,cell_height)
			cutout_surf = pygame.Surface((cell_width, cell_height))
			cutout_surf.fill('green')
			cutout_surf.set_colorkey('green')
			cutout_surf.blit(surf, (0,0), cutout_rect)
			frames[(col, row)] = cutout_surf
	return frames


def character_importer(cols: int, rows: int, *path: str) -> dict[str, list]:
	"""
	Do: Imports a character's spritesheet and organizes the frames into animations for 
	different directions (down, left, right, up), including idle animations.

	Return: { direction: list of col Surfaces }
	"""
	frame_dict = import_tilemap(cols, rows, *path)
	new_dict = {}
	for row, direction in enumerate(('down', 'left', 'right', 'up')):
		new_dict[direction] = [frame_dict[(col, row)] for col in range(cols)]
		new_dict[f"{direction}_idle"] = [frame_dict[(0, row)]]
	return new_dict


def all_character_import(*path: str) -> dict:
	"""
	Imports all character spritesheets from a folder and organizes their animations using the character_importer function.
	A dictionary where the keys are the names of the characters (from the filenames), and the values are dictionaries containing the animations for each direction.
	"""
	new_dict = {}
	for _, _, image_names in walk(join(*path)):
		for image in image_names:
			image_name = image.split(".")[0]
			new_dict[image_name] = character_importer(4, 4, *path, image_name)
	return new_dict