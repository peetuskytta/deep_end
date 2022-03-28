from menu import *
import pygame

class Game():
	# pygame iniate function
	def __init__(self):
		pygame.init()

	# Setting up some bool values for keys and gamestate
		self.running, self.playing = True, False
	# Variables for keystrokes
		self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
	# Variables for the canvas size
		self.DISPLAY_W, self.DISPLAY_H = 1280, 720
	# display will create the canvas using pygame.surface
		self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
	# above we have canvas, now we want to show to the user what we have
		self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))

	# Set font.
		self.font_name = '8-BIT WONDER.TTF'
	#self.font_name = pygame.font.get_default_font()
		self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
		self.main_menu = MainMenu(self)
		self.options = OptionsMenu(self)
		self.credits = CreditsMenu(self)
		self.curr_menu = self.main_menu

# Function for game loop
	def game_loop(self):
	# while player is playing we want to see their inputs
		while self.playing:
			self.check_events()
			if self.START_KEY:
				self.playing = False
			self.display.fill(self.BLACK) # this resets the screen
			self.draw_text('Thanks for playing', 50, self.DISPLAY_W / 2, self.DISPLAY_H / 2)
			self.window.blit(self.display, (0,0)) # align window with display
			
		# Now we tell pygame to put out whatever we have to the screen
			pygame.display.update()
		# Reset keys.
			self.reset_keys()

# Player inputs function
	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running, self.playing = False, False
				self.curr_menu.run_display = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					self.START_KEY = True
				if event.key == pygame.K_BACKSPACE:
					self.BACK_KEY = True
				if event.key == pygame.K_DOWN:
					self.DOWN_KEY = True
				if event.key == pygame.K_UP:
					self.UP_KEY = True

# Function to reset the buttons values
	def reset_keys(self):
		self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

# Function to write text on the screen. Self is the reference to 
# the Game to have access to variables in Class Game
	def draw_text(self, text, size, x,y ):
		font = pygame.font.Font(self.font_name,size)
		text_surface = font.render(text, True, self.WHITE)
		
	# rect class has 4 main components: x,y,w,h
		text_rect = text_surface.get_rect()
		text_rect.center = (x,y)
		self.display.blit(text_surface,text_rect)
  