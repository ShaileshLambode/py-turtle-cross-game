# Turtle Cross Game 🐢🚗

A fun arcade-style game built with **Python Turtle Graphics** where the player guides a turtle across a busy road while avoiding moving cars.

---

## Demo / Preview

![Game video](game-video.gif)

---

## Table of Contents

- [Features](#features)  
- [Project Structure](#project-structure)  
- [Game Rules](#game-rules)  
- [Installation](#installation)  
- [Running the Game](#running-the-game)  
- [Usage](#usage)  
- [Future Improvements](#future-improvements)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features

- Player controls a turtle character trying to cross the screen.  
- Cars continuously move across the road with increasing speed.  
- Difficulty increases as you progress through levels.  
- Scoreboard shows the current level.  
- Classic retro-style visuals using Python’s Turtle module.  

---

## Project Structure

```
py-turtle-cross-game/
├── main.py            # Game entry point
├── player.py          # Player (turtle) class
├── car_manager.py     # Car behavior and spawning
├── scoreboard.py      # Scoreboard handling
├── Demo.png           # Screenshot/demo image
├── README.md
└── LICENSE
```

- **main.py**: Launches the game  
- **player.py**: Handles turtle movement and boundary checks  
- **car_manager.py**: Generates cars and moves them across the screen  
- **scoreboard.py**: Tracks and displays player’s level/score  

---

## Game Rules

- Use the **Up Arrow Key** ⬆️ to move the turtle upwards.  
- Avoid getting hit by the cars.  
- Each successful crossing increases your level.  
- Cars get faster as levels increase.  
- If you collide with a car, the game ends.  

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ShaileshLambode/py-turtle-cross-game.git
   cd py-turtle-cross-game
   ```

2. Ensure you have Python 3.x installed. Turtle comes pre-installed with Python, no extra dependencies are required.

---

## Running the Game

```bash
python main.py
```

---

## Usage

- Run the game from the terminal.  
- Use the **Up Arrow Key** to move.  
- Keep crossing until you reach the highest level you can!  

---

## Future Improvements

- Add support for saving high scores.  
- Introduce multiple lanes and obstacles.  
- Add sound effects for collisions and level-ups.  
- Support more controls (left/right movements).  
- Improve UI with custom turtle sprites.  

---

## Contributing

Contributions are welcome!  

1. Fork the repo  
2. Create a new branch (`feature/my-feature`)  
3. Commit your changes  
4. Push the branch  
5. Open a Pull Request  
