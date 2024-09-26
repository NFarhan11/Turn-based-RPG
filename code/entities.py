from settings import *

class Entity(pygame.sprite.Sprite):
	def __init__(self, pos: tuple, frames: dict, groups: pygame.sprite.Group) -> None:
		super().__init__(groups)

		# graphics
		self.frame_index: float = 0
		self.frames:dict = frames
		self.facing_direction = "down"

		# movement
		self.direction: Vector2 = Vector2()
		self.speed: float = 250

		# sprite setup
		print(f"{self.frames=}")
		self.image = self.frames[self.get_state()][self.frame_index]
		self.image = pygame.transform.scale(self.image, (self.image.get_width() * SCALE_FACTOR, self.image.get_height() * SCALE_FACTOR))
		self.rect = self.image.get_frect(center=pos)

	def animate(self, dt: float) -> None:
		self.frame_index += ANIMATION_SPEED * dt
		self.image = self.frames[self.get_state()][int(self.frame_index % len(self.frames[self.get_state()]))]
		self.image = pygame.transform.scale(self.image, (self.image.get_width() * SCALE_FACTOR, self.image.get_height() * SCALE_FACTOR))

	def get_state(self):
		moving = bool(self.direction)  # if player is moving
		if moving:
			if self.direction.x != 0:
				self.facing_direction = "right" if self.direction.x > 0 else "left"
			if self.direction.y != 0:
				self.facing_direction = "down" if self.direction.y > 0 else "up"
		return f"{self.facing_direction}{"" if moving else "_idle"}"  # if idle put _idle


class Player(Entity):
	def __init__(self, pos: tuple, frames: dict, groups: pygame.sprite.Group) -> None:
		super().__init__(pos, frames, groups)

	def input(self) -> None:
		keys = pygame.key.get_pressed()
		input_vector: Vector2 = Vector2()
		if keys[pygame.K_w]: input_vector.y -= 1
		if keys[pygame.K_s]: input_vector.y += 1
		if keys[pygame.K_a]: input_vector.x -= 1
		if keys[pygame.K_d]: input_vector.x += 1
		self.direction = input_vector

	def move(self, dt: float) -> None:
		self.rect.center += self.direction * self.speed * dt

	def update(self, dt: float) -> None:
		self.input()
		self.move(dt)
		self.animate(dt)
