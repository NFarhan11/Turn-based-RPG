from settings import *
from pytmx.util_pygame import load_pygame
from os.path import join
from support import *

from sprite import Sprite
from entities import Player
from groups import AllSprites

class Game:
	def __init__(self) -> None:
		pygame.init()
		self.display_surf = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption("Turn-based RPG")
		self.clock: pygame.time.Clock = pygame.time.Clock()

		# groups
		self.all_sprites = AllSprites()

		self.import_assets()
		self.setup(self.tmx_maps["world"], "start")

	def import_assets(self) -> None:
		# load world tmx
		self.tmx_maps = {
		"world": load_pygame(join("data", "maps", "world.tmx"))
		}
		# load graphics
		self.overworld_frames = {
		"characters": all_character_import("graphics", "characters")
		}
		print(f"{self.overworld_frames["characters"]=}")

	def setup(self, tmx_map, player_pos) -> None:
		# Layer -> Ground
		for x, y, surf in tmx_map.get_layer_by_name("Ground").tiles():
			Sprite((x * TILE_SIZE * SCALE_FACTOR, y * TILE_SIZE * SCALE_FACTOR), surf, self.all_sprites)
			
		# Layer -> Entities
		for obj in tmx_map.get_layer_by_name("Entities"):
			if obj.name == "Player" and obj.properties["pos"] == player_pos:
				self.player = Player(
					pos=(obj.x, obj.y), 
					frames=self.overworld_frames["characters"]["player"], 
					groups=self.all_sprites)

	def input(self) -> None:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()	

	def update(self, dt) -> None:
		self.all_sprites.update(dt)

	def render(self) -> None:
		self.display_surf.fill("black")
		self.all_sprites.draw(self.player.rect.center)
		pygame.display.update()

	def run(self) -> None:
		while True:
			dt = self.clock.tick() / 1000
			self.input()
			self.update(dt)
			self.render()


if __name__ == '__main__':
	Game().run()

