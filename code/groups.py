from settings import *

class  AllSprites(pygame.sprite.Group):
	def __init__(self) -> None:
		super().__init__()
		self.display_surf = pygame.display.get_surface()
		self.offset: Vector2 = Vector2()

	def draw(self, player_center: Vector2) -> None:
		self.offset.x = -(player_center[0] - WIDTH / 2)
		self.offset.y = -(player_center[1] - HEIGHT / 2)

		for sprite in self:
			self.display_surf.blit(sprite.image, sprite.rect.topleft + self.offset)
