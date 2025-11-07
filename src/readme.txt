Reach The Flag - README
========================

Hey there! Thanks for checking out my platformer game.

WHAT'S THIS ABOUT?
------------------
It's a simple game where you try to get from the bottom-left corner to a flag
at the top-right. Sounds easy, right? Well, there are a couple of enemies 
bouncing around trying to stop you!

THE GOAL
--------
Just use your arrow keys to move around and touch the flag. But watch out - 
bumping into enemies will drain your health by 10% each time. You've got 
enough health for 10 hits, so don't get too reckless!

WHAT YOU'LL NEED
----------------
This game uses a few Python libraries:
- pgzrun: Makes game development way easier (it's built on Pygame Zero)
- pygame: Handles all the graphics, sounds, and controls
- pygame.mixer.music: Takes care of the background music

GETTING STARTED
---------------
First, make sure you've got Python 3.6 or newer installed.

Then open your terminal and install the libraries:
   
   pip install pgzero pygame

If that doesn't work, try:
   
   pip3 install pgzero pygame

SETTING UP YOUR FILES
---------------------
Your game folder should look something like this:

platformer_game/
├── platformer_demo.py          (the main game code)
├── images/
│   ├── player_1.png           (that's you!)
│   ├── enemy_2.png            (bad guy #1)
│   ├── enemy_idle.png         (bad guy #2)
│   └── fwin_flag.png          (your destination)
└── sounds/
    ├── bg_music.mp3           (some background tunes)
    └── hit.wav                (ouch sound when you get hit)

Just make sure your images go in the 'images' folder and sounds in 'sounds'.
Pygame Zero knows to look there automatically.

RUNNING THE GAME
----------------
Open your terminal, go to where you saved the game:
   cd path/to/platformer_game

Then just run it:
   python platformer_demo.py
   
Or maybe:
   python3 platformer_demo.py

HOW TO PLAY
-----------
- Arrow Keys: Move the ring around (works in all directions)
- Mouse: Click the menu buttons

TIPS
----
- You start with 100 health
- Enemies take 10 health per hit
- There are two enemies that bounce around randomly
- Get to that flag and you win!
- Run out of health and... well, you know

IF SOMETHING'S NOT WORKING
--------------------------
No music playing?
- Double-check that bg_music.mp3 is in your sounds folder
- Don't worry, the game will still work without it

Images not showing up?
- Make sure all your PNG files are in the images folder
- Check the names match exactly (uppercase/lowercase matters!)

Game won't start at all?
- Check you have Python 3.6 or newer
- Try reinstalling the libraries: pip install --upgrade pgzero pygame
- Make sure you spelled the filename correctly

FINAL NOTES
-----------
Built with Pygame Zero because it makes things so much simpler.
Remember to use your own images and sounds, or grab some free ones online!

Have fun playing!