"""
    @author Grace Keane

    SnakeApplication - class that created the actual snake game and functionality.
"""

import random
import sys
from pygame.locals import *
# Need to import the snake appearance class for colors, sizing ect.
from SnakeAppearance import *

def main():
	global CLOCK, SCREEN, FONT

	pygame.init()
	CLOCK = pygame.time.Clock()
	SCREEN = pygame.display.set_mode((Width_window, height_window))
	FONT = pygame.font.Font('freesansbold.ttf', 18)
	pygame.display.set_caption('Snake')
	showStartScreen()

	while True:
        # Calling function
		runGame()
		showGameOverScreen()

# Function to run the game
def runGame():
	# Set a random starting point in the game
	startx = random.randint(5, cell_width - 6)
	starty = random.randint(5, cell_height - 6)
	global worm
	worm = [{'x' : startx, 'y' : starty}, {'x': startx - 1, 'y':starty}, {'x':startx - 2, 'y':starty}]
	direction = UP

    # Assigning a random location for the food to spawn
	food = getRandomLocation()

	while True:
		for event in pygame.event.get():
            # When dead -> stop game
			if event.type == QUIT:
				terminate()

            # Assigning the movement
			elif event.type == KEYDOWN:
				if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
					direction = LEFT
				elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
					direction = RIGHT
				elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
					direction = UP
				elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
					direction = DOWN

		# Check Collision with edges
		if worm[HEAD]['x'] == -1 or worm[HEAD]['x'] == cell_width or worm[HEAD]['y'] == -1 or worm[HEAD]['y'] == cell_height:
			return
		# Check Collision with snake's body
		for wormBody in worm[1:]:
			if wormBody['x'] == worm[HEAD]['x'] and wormBody['y'] == worm[HEAD]['y']:
				return
		# Check Collision with food
		if worm[HEAD]['x'] == food['x'] and worm[HEAD]['y'] == food['y']:
			# Ger another random location for the food when hit a food
			food = getRandomLocation()
		else:
			del worm[-1]

		# Move the Snake
		if direction == UP:
			newHead = {'x': worm[HEAD]['x'], 'y': worm[HEAD]['y'] - 1}
		elif direction == DOWN:
			newHead = {'x': worm[HEAD]['x'], 'y': worm[HEAD]['y'] + 1}
		elif direction == RIGHT:
			newHead = {'x': worm[HEAD]['x'] + 1, 'y': worm[HEAD]['y']}
		elif direction == LEFT:
			newHead = {'x': worm[HEAD]['x'] - 1, 'y': worm[HEAD]['y']}
		worm.insert(0, newHead)

		# Drawing the game Screen
		SCREEN.fill(BGCOLOR)
		drawWorm(worm)
		drawfood(food)
		drawScore((len(worm) - 3) * 10)
		pygame.display.update()
		CLOCK.tick(FPS)

# Calculate the score of the game
def getTotalScore():
	# Determined by how lange the snake/ worm is
	return ((len(worm) - 3) * 10)


def drawPressKeyMsg():
	pressKeyText = FONT.render('Tap anywhere to play SNAKE!', True,WHITE)
	pressKeyRect = pressKeyText.get_rect()
	pressKeyRect.center = (Width_window - 200, height_window - 100)
	SCREEN.blit(pressKeyText, pressKeyRect)

def checkForKeyPress():
	if len(pygame.event.get(QUIT)) > 0:
		terminate()
	keyUpEvents = pygame.event.get(KEYUP)

	if len(keyUpEvents) == 0:
		return None
	if keyUpEvents[0].key == K_ESCAPE:
		terminate()
	return keyUpEvents[0].key

# Start screen
def showStartScreen():
	titlefont = pygame.font.Font('freesansbold.ttf', 100)
	titleText = titlefont.render('SNAKE', True,YELLOW)
	while True:
		# Assigning location of text
		SCREEN.fill(BGCOLOR)
		titleTextRect = titleText.get_rect()
		titleTextRect.center = (Width_window / 2, height_window / 2)
		SCREEN.blit(titleText, titleTextRect)

		drawPressKeyMsg()
		if checkForKeyPress():
			# Start the game
			pygame.event.get()
			return
		pygame.display.update()
		CLOCK.tick(FPS)

def terminate():
	pygame.quit()
	sys.exit()

def getRandomLocation():
	# Assigning a random location for the food to be spawned
	return {'x': random.randint(0, cell_width - 1), 'y': random.randint(0, cell_height - 1)}

def showGameOverScreen():
	gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
	gameOverText = gameOverFont.render('GAME OVER', True, BLACK)
	gameOverRect = gameOverText.get_rect()

	totalscoreFont = pygame.font.Font('freesansbold.ttf', 40)
	totalscoreText = totalscoreFont.render('Total Score: %s' % (getTotalScore()), True, RED)
	totalscoreRect = totalscoreText.get_rect()
	totalscoreRect.midtop = (Width_window /2, 150)

	gameOverRect.midtop = (Width_window /2, 30)

	SCREEN.fill(BGCOLOR)
	SCREEN.blit(gameOverText, gameOverRect)
	SCREEN.blit(totalscoreText, totalscoreRect)
	drawPressKeyMsg()
	pygame.display.update()
	pygame.time.wait(1000)
	checkForKeyPress()

	while True:
		if checkForKeyPress():
			pygame.event.get()
			return

# Printing the score to the screen and accessing the score var
def drawScore(score):
	scoreText = FONT.render('Score: %s' % (score), True, BLACK)
	scoreRect = scoreText.get_rect()
	scoreRect.center = (Width_window  - 100, 40)
	SCREEN.blit(scoreText, scoreRect)

# Printing the snake/ worm to the the screen
# Worm is 1 cell high and wide
def drawWorm(worm):
	x = worm[HEAD]['x'] * size_cell
	y = worm[HEAD]['y'] * size_cell
	wormHeadRect = pygame.Rect(x, y, size_cell, size_cell)
	pygame.draw.rect(SCREEN, RED, wormHeadRect)

	for coord in worm[1:]:
		x = coord['x'] * size_cell
		y = coord['y'] * size_cell
		wormSegmentRect = pygame.Rect(x, y, size_cell, size_cell)
		pygame.draw.rect(SCREEN, WHITE, wormSegmentRect)

def drawfood(coord):
	# Drawing the food
	# Food is one cell high and wide
	x = coord['x'] * size_cell
	y = coord['y'] * size_cell
	appleRect = pygame.Rect(x, y, size_cell, size_cell)
	pygame.draw.rect(SCREEN, YELLOW, appleRect)

if __name__ == '__main__':
	main()