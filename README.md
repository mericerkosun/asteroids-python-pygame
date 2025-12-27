# 🚀 Asteroids Game Clone

A classic arcade space shooter game recreated using **Python** and **Pygame**. This project demonstrates object-oriented programming, game loop logic, collision detection, and vector mathematics.

## 🎮 Game Features

* **Player Movement:** Physics-based movement including rotation and acceleration (thrust).
* **Shooting Mechanics:** Fire projectiles with a cooldown timer to destroy obstacles.
* **Asteroid Logic:** * Randomized spawning of asteroids.
    * **Splitting Mechanic:** Large asteroids split into two medium ones, and medium ones split into two small ones when destroyed.
* **Collision Detection:** Custom circle-based collision detection system.
* **Game Loop:** Optimized game loop with Delta Time (dt) for frame-rate independent movement.

## 🛠️ Technologies Used

* **Python 3.12+**
* **Pygame Community Edition (CE)**

## 📂 Project Structure

* `main.py`: Entry point of the game. Handles the game loop, initialization, and groups.
* `player.py`: Contains the `Player` class, movement logic, and shooting.
* `asteroid.py`: Contains the `Asteroid` class and the splitting logic.
* `shot.py`: Manages the bullet projectiles.
* `circleshape.py`: Base class for all circular game objects (handles collisions).
* `constants.py`: Stores game configuration (screen size, speed, colors, etc.).

## ⚙️ Installation & How to Run

1.  **Clone the repository:**

2.  **Create a virtual environment (Recommended):**
    ```bash
    # macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    
    # Windows
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install pygame
    ```

4.  **Run the game:**
    ```bash
    uv run main.py
    ```

## 🕹️ Controls

| Key | Action |
| :--- | :--- |
| **W** | Move Forward (Thrust) |
| **S** | Move Backward |
| **A** | Rotate Left |
| **D** | Rotate Right |
| **SPACE** | Shoot |
| **Esc / Close** | Exit Game |

---
*Developed as part of the Boot.dev backend development curriculum.*
