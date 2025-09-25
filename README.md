# Basic-Frog-Pygame
A simple Pygame project where you play as a hungry frog trying to eat flies as fast as possible.  
---

## 🎮 How to Run the Game

**Prerequisites**
- Python 3.x  
- Pygame

**Install Pygame**
```bash
pip install pygame

Run
python main.py

🏆 Objective

Eat all 5 flies in under 10 seconds to win.

The game keeps track of your times so you can try to beat your personal best.

📊 Scoring

Better score: Lower time (like golf — lower is better).

Worse score: Longer time gives a worse score.

Lose condition: If your time is over 10 seconds, you lose.

🕹️ Controls

← Left Arrow — Move left

→ Right Arrow — Move right

↑ Up Arrow — Jump

Spacebar — Eat flies

🧩 Classes
🐸 Frog Class

Description: Controls the frog character and its behaviors.
Methods

draw() — Draw the frog to the screen

get_rect() — Return the bounding box for collision detection

left — Tracks whether the frog is facing left (used to flip sprite)

move() — Move frog left/right and update state (idle, jumping, landing)

follow_mouse() — (Optional) Move the frog to follow the mouse

🪰 Fly Class

Description: Flies move randomly and spawn at random screen positions.
Methods

draw() — Draw a fly

get_rect() — Return the bounding box

move() — Update fly position given speed and direction

move_randomly() — Add jitter/shake to fly movement

📝 Text Class

Description: Handles on-screen messages and scoreboard text.
Methods

draw() — Render the message on screen

get_rect() — Return bounding box for the text

setMessage() — Set message content and properties

🎨 Drawable Class (Abstract Base)

Description: Base class for drawable game objects.
Methods / Features

Getters and setters for position (getX, getY, setLoc, etc.)

Visibility controls (isVisible, setVisible)

intersects() — Check collision with another drawable

Abstract methods that child classes must implement (e.g., draw, get_rect, move)

🏗️ Main Script

The main game loop is wrapped in a function (inspired by CS171 pathway games), which makes it straightforward to restart/replay the game if the player chooses to play again.

The main script initializes game objects, starts the timer, handles input, updates objects, checks collisions, and shows win/lose screens.

⏱️ Score Tracking

Time taken — Tracked from the starting condition; used to determine win/lose and ranking.

Number of flies eaten — Must reach 5 to win.

Scoreboard — Shows previous games and top (fastest) times.

✅ Required Elements

Predator tracking: Number of flies eaten shown in the top-left corner.

Starting condition: Timer starts when the game begins.

Changing condition: Time and flies-eaten counters update during play; flies disappear when eaten; frog moves and jumps; flies move randomly.

Final condition: When the game ends, a Win/Lose message appears (e.g., “Congrats” or “You lose”) and the scoreboard loads with the results.

🐸 Final Notes

Eat quickly and keep your time under 10 seconds.

Lower times are better — try to beat your personal best!
