
# Car Game

This project is a simple lane-based car game developed using Python and Pygame. Players control a car to avoid oncoming vehicles and score points. The game demonstrates essential game development concepts such as sprite handling, collision detection, and dynamic difficulty.

## Project Overview

The Car Game project is designed for both fun and learning. It allows users to experience arcade-style gameplay while providing developers a hands-on understanding of Pygame. The core objective is to navigate lanes, avoid vehicles, and achieve a high score as the game progressively becomes more challenging.

## Features

- **Lane-Based Navigation**: Players can move between three lanes.
- **Dynamic Difficulty**: The speed of the game increases as the player’s score grows.
- **Collision Detection**: Game ends upon collision with other vehicles.
- **Score System**: Points are awarded for each vehicle successfully avoided.
- **Restart Functionality**: Players can restart the game after a crash.

## Gameplay Instructions

- **Objective**: Avoid colliding with other vehicles while scoring as many points as possible.
- **Controls**:
  - **Left Arrow**: Move the car left.
  - **Right Arrow**: Move the car right.
- **Scoring**: You earn 1 point for every vehicle you successfully avoid.
- **Game Over**: The game ends when you collide with another vehicle. Press:
  - **Y** to restart.
  - **N** to quit.

## Screenshots

### Gameplay
![Gameplay Screenshot](images/gameplay.png)

### Game Over Screen
![Game Over Screenshot](images/gameover.png)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd car_game
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed. Install Pygame using pip:
   ```bash
   pip install pygame
   ```

3. **Run the Game**:
   ```bash
   python car_game.py
   ```

## Project Structure

```
├── images/               # Folder containing vehicle and crash images
│   ├── car.png
│   ├── crash.png
│   ├── pickup_truck.png
│   ├── semi_trailer.png
│   ├── taxi.png
│   └── van.png
├── car_game.py           # Main game script
├── README.md             # Project documentation
└── LICENSE               # License file
```

## Dependencies

- **Python 3.8+**
- **Pygame 2.0+**

To install the dependencies:
```bash
pip install pygame
```

## Known Issues

- Occasionally, vehicles may spawn close to the player, making collisions unavoidable.
- Currently, no sound effects are implemented.

## Future Improvements

- **Sound Effects**: Add collision sounds and background music.
- **Enhanced Graphics**: Improve animations and visuals for better user experience.
- **Leaderboards**: Implement a system to track and display high scores.
- **Additional Game Modes**: Introduce new modes with varied challenges.

## Contributing

Contributions are welcome! If you'd like to improve the game, please:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request.

## Changelog

### Version 1.0.0
- Initial release with:
  - Basic lane-switching gameplay.
  - Collision detection.
  - Score tracking and dynamic speed increase.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## References

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python Official Website](https://www.python.org/)
