1. Short description of the app, what is it about, how can it be run:

- This Python file contains a simple grid-based game. It comprises functions to update the grid with player and enemy positions, handle user inputs for movement within the grid, and display the updated grid.
- To run the app, execute the Python script. The game creates a grid where 'P' represents the player's position and 'E' denotes enemy positions. Users can enter commands ('u', 'd', 'l', 'r' followed by a number) to move the player within the grid. 
- 'u' being up, 'd' being down, 'l' being left, and 'r' being right. Typing 'q' quits the game.
- The main() function initializes the grid, player, and enemy positions and initiates the game loop, which continuously updates the grid and accepts user inputs until the user quits or the game ends.
- To play, interact with the game through the command line by inputting the specified commands ('u', 'd', 'l', 'r' followed by a number). Ex. u3 to go left 3 steps.

NOTE: When running this app on a terminal with docker, since its user interactive, command would be:
	docker run -i -t python-assignment4

Otherwise it would give you an error saying "EOF when reading a line"

2. URL to the GitHub repository:

https://github.com/oblivxin/assignment4

3. URL to the Docker Hub Image:

https://hub.docker.com/r/oblivxin/python-assignment4