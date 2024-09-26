from settings import *

class Sprite(pygame.sprite.Sprite):
	def __init__(self, pos: tuple, surf: pygame.Surface, groups: pygame.sprite.Group) -> None:
		super().__init__(groups)
		self.image = pygame.transform.scale(surf, (surf.get_width() * SCALE_FACTOR, surf.get_height() * SCALE_FACTOR))
		self.rect = self.image.get_frect(topleft=pos)
