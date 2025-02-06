import pygame
import pygame_menu
import random
import time

# Main Menu
mainmenu = True

# Window size
window_x = 1000 ; window_y = 1000

# FPS (frames per second) controller
# object to help track time
fps = pygame.time.Clock()

# Main menu theme (pygame_menu)
theme = pygame_menu.themes.THEME_DARK.copy()
theme.title_font = pygame_menu.font.FONT_8BIT
theme.widget_font = pygame_menu.font.FONT_8BIT

# Set periodic boundaries
periodic = [True]

# Set random walls
random_walls = [True]

def init():
    # Initialising pygame
    pygame.init()

    # Initialise game window
    pygame.display.set_caption('Exploring Space')
    # Hide cursor here
    #pygame.mouse.set_visible(False)
    game_window = pygame.display.set_mode((window_x, window_y))
    return game_window

def update(game_window):
    # displaying score countinuously
    show_score(1, white, 'times new roman', 20, game_window)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(1)

def random_int():
	n = random.randint(0,1)*2 -1
	return n

def random_pos(offset = 0):
    pos = [random.randrange(1 + 10*offset, (window_x//10)) * 10 - 10*offset,
           random.randrange(1 + 10*offset, (window_y//10)) * 10 - 10*offset]
    return pos

# displaying Score function
def show_score(choice, color, font, size, game_window):

	# creating font object score_font
	score_font = pygame.font.SysFont(font, size)
	
	# create the display surface object
	# score_surface
	score_surface = score_font.render('Score : ' + str(score), True, color)
	
	# create a rectangular object for the text
	# surface object
	score_rect = score_surface.get_rect()
	
	# displaying text
	game_window.blit(score_surface, score_rect)


# game over function
def game_over(game_window):

	# creating font object my_font
	my_font = pygame.font.SysFont('times new roman', 50)
	
	# creating a text surface on which text
	# will be drawn
	game_over_surface = my_font.render(
		'Your Score is : ' + str(score), True, red)
	
	# create a rectangular object for the text
	# surface object
	game_over_rect = game_over_surface.get_rect()
	
	# setting position of the text
	game_over_rect.midtop = (window_x/2, window_y/4)
	
	# blit will draw the text on screen
	game_window.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	
	# after 2 seconds we will quit the program
	time.sleep(2)
	
	# deactivating pygame library
	pygame.quit()
	
	# quit the program
	quit()

def congratulations(game_window):

	my_font = pygame.font.SysFont('times new roman', 40)
	surface = my_font.render(
		'Congratulations, you completed the game!', True, green)
	rect = surface.get_rect()
	
	# setting position of the text
	rect.midtop = (window_x/2, window_y/4)
	
	# blit will draw the text on screen
	game_window.blit(surface, rect)
	pygame.display.flip()
	
	# after 2 seconds we will quit the program
	time.sleep(2)
	
	# deactivating pygame library
	pygame.quit()
	
	# quit the program
	quit()

def set_periodic(str, value):
	periodic[0] = value

def set_walls(str, value):
	random_walls[0] = value

def unset_options():
	random_walls[0] = False
	periodic[0] = True
