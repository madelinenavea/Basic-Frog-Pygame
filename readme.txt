HOW TO RUN THE GAME:
    OBJECTIVE:
        - Eat all 5 flies under 10 seconds to win! Keep track of your best (or worst) games if you play multiple times.

    HOW TO EARN POINTS (a better score)
        - Try to beat your best time. The shorter your time is, the better your score is! (It is like golf, the lower the score, the better the score.)

    HOW TO LOSE POINTS (a bad score)
        - If you have a longer time, you will get a worse score. 

    HOW TO LOSE
        - You cannot have a score over 10 seconds or you will lose.

FROG CLASS:
    - DESCRIPTION:
        - the frog can move left and right using the LEFT and RIGHT ARROW KEY buttons.
        - the frog can jump using the UP ARROW KEY button
        - press the SPACEBAR to eat the flies.
    - methods:
        - draw: draw an instance of a frog
        - get_rect: bounding box for frog
        - left: shows if frog is looking left (to flip the frog's image and make it appear to move left)
        - move: moves the frog left and right and updates the frog's position (idle, jumping up, landing, idle) accordingly
        - follow_mouse: hw instructions instance to move the frog all around the screen


FLY CLASS:
    - DESCRIPTION:
        - the flies move around randomly and all around the screen, (like the homework instructions).
        - random images of flies are generated and they are generated at random places on the screen.
    - methods:
        - draw: draws an instance of a fly
        - get_rect: shows bounding box
        - move: moves it at a certain speed and location
        - move_randomly: makes the fly shake

TEXT CLASS:
    - messages are generated using the default text class settings
    - methods:
        - draw: draws the message
        - get_rect: shows bounding box
        - setMessage: sets all message info

DRAWABLE CLASS:
    - abstract base class
    - methods:
        - getters: gets location
        - setters: set both x and y using setLoc or set x and y individually
        - visibility: see if drawings are visible and set its visibility
        - intersects: see if drawings intersect
        - abstractmethods: pass these methods onto their child classes


MAIN SCRIPT:
    - I set the main script up like how we created the pathway games in 171 for specific people (i.e., in a function), so that i could repeat the game if the user decides they want to play again.

SCORING TRACKING VALUES:
    - The main script keeps track of their time and the number of flies eaten. The number of flies eaten is a requirement to win the game. The time is how to see your best times, however, one of the requirements of the game is to have your time be under 10 seconds.
    - The scoreboard shows previous games played and their top scores.

REQUIRED ELEMENTS:
• "Keep track of how many times the predator eats"
    Found in the top left corner of my game.

• "Have a starting condition"
    The starting condition is when the timer starts.

• "Show changes in condition during the running of the program"
    The time is kept track of in the left corner and the number of flies eaten is shown in the right corner. The flies disappear when the frog eats them. The frog also jumps and moves around. The flies move around.

• "Show the final condition. In a game this is a win/lose threshold and in a simulation it may be a predetermined number of predators or prey or time cycles"
    This is found when the "Congrats" or "You lose" section appear and also when the scoreboard loads.