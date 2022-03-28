import pygame
import sys

class Menu():
	def __init__(self, game):
    ## Reference to our game object so we can have access them
		self.game = game
		self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
		self.run_display = True
		self.cursor_rect = pygame.Rect(0, 0, 30, 30)
		self.offset = - 150

	def draw_cursor(self):
		self.game.draw_text('*', 20, self.cursor_rect.x, self.cursor_rect.y)
	def blit_screen(self):
		self.game.window.blit(self.game.display, (0, 0))
		pygame.display.update()
		self.game.reset_keys()

# By putting 'Menu' in parenthesis tell python we want to inherit the base values
# class Menu we made earlier.
class MainMenu(Menu):
	def __init__(self, game):
		Menu.__init__(self, game)

		# Setting the menu text positions
		self.state = "Start"
		self.startx, self.starty = self.mid_w, self.mid_h + 30
		self.optionsx, self.optionsy = self.mid_w, self.mid_h + 70
		self.creditsx, self.creditsy = self.mid_w, self.mid_h + 110
		self.quitx, self.quity = self.mid_w, self.mid_h + 150
		# This will align the star with the box in question
		self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

	def display_menu(self):
		self.run_display = True
		while self.run_display:
			self.game.check_events()
			self.check_input()
			self.game.display.fill(self.game.BLACK)
			self.game.draw_text('Main Menu', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 35)
			self.game.draw_text("Start Game", 30, self.startx, self.starty)
			self.game.draw_text("Options", 30, self.optionsx, self.optionsy)
			self.game.draw_text("Credits", 30, self.creditsx, self.creditsy)
			self.game.draw_text("Quit", 30, self.quitx, self.quity)
			self.draw_cursor()
			self.blit_screen()


	def move_cursor(self):
		if self.game.DOWN_KEY:
			if self.state == 'Start':
				self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
				self.state = 'Options'
			elif self.state == 'Options':
				self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
				self.state = 'Credits'
			elif self.state == 'Credits':
				self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
				self.state = 'Quit'
			elif self.state == 'Quit':
				self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
				self.state = 'Start'
		elif self.game.UP_KEY:
			if self.state == 'Start':
				self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
				self.state = 'Quit'
			elif self.state == 'Options':
				self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
				self.state = 'Start'
			elif self.state == 'Credits':
				self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
				self.state = 'Options'
			elif self.state == 'Quit':
				self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
				self.state = 'Credits'

	def check_input(self):
		self.move_cursor()
		if self.game.START_KEY:
			if self.state == 'Start':
				self.game.playing = True
			elif self.state == 'Options':
				self.game.curr_menu = self.game.options
			elif self.state == 'Credits':
				self.game.curr_menu = self.game.credits
			elif self.state == 'Quit':
				pygame.quit()
				sys.exit()
			self.run_display = False

class OptionsMenu(Menu):
	def __init__(self, game):
		Menu.__init__(self, game) # Menu baseclass initiator
		self.state = 'Volume'
		self.volx, self.voly = self.mid_w, self.mid_h + 20
		self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
		self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

	def display_menu(self):
		self.run_display = True
		while self.run_display:
			self.game.check_events()
			self.check_input()
			self.game.display.fill((0, 0, 0))
			self.game.draw_text('Options', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
			self.game.draw_text("Volume", 15, self.volx, self.voly)
			self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
			self.draw_cursor()
			self.blit_screen()

	def check_input(self):
		if self.game.BACK_KEY:
			self.game.curr_menu = self.game.main_menu
			self.run_display = False
		elif self.game.UP_KEY or self.game.DOWN_KEY:
			if self.state == 'Volume':
				self.state = 'Controls'
				self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
			elif self.state == 'Controls':
				self.state = 'Volume'
				self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
		elif self.game.START_KEY:
			# TO-DO: Create a volume menu and controls menu
			pass

class CreditsMenu(Menu):
	def __init__(self, game):
		Menu.__init__(self, game)

	def display_menu(self):
		self.run_display = True
		while self.run_display:
			self.game.check_events()
			if self.game.START_KEY or self.game.BACK_KEY:
				self.game.curr_menu = self.game.main_menu
				self.run_display = False
			self.game.display.fill(self.game.BLACK)
			self.game.draw_text('Credits', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
			self.game.draw_text('Made by Pskytta', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
			self.blit_screen()