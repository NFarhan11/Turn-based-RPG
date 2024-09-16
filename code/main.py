from settings import *

class Game:
	def __init__(self):
		pygame.init()
		self.display_surf = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption("Turn-based RPG")

	def input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()	

	def render(self):
		pygame.display.update()

	def run(self):
		while True:
			self.input()
			self.render()


if __name__ == '__main__':
	Game().run()

