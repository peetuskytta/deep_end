from game import Game

# Everything from Game will run when this is called
g = Game()
 
while g.running:
    g.curr_menu.display_menu()
    g.game_loop()