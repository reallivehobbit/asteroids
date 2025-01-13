import pygame
import sys
from constants import *
from player import Player 
from asteroidfield import *
from shot import Shot


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	Shot.containers = (shots, updatable, drawable)

	asteroid_field = AsteroidField()

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)



	print("Starting asteroids!")
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return		

		for sprite in updatable:
			sprite.update(dt)

		screen.fill((0, 0, 0))
		
		
		for sprite in drawable:
			sprite.draw(screen)



		for asteroid in asteroids:
			if player.collision_check(asteroid):
				print("Game over!")
				sys.exit()

			for shot in shots:
				if asteroid.collision_check(shot):
					shot.kill()
					asteroid.split()

		pygame.display.flip()
		time = clock.tick(60)
		dt = time/1000

if __name__ == "__main__":
	main()

