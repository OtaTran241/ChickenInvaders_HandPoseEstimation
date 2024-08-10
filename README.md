# Chicken Invaders Hand Control

This repository contains code to play Chicken Invaders using hand gestures detected by a camera.

## Table of Contents

- [Introduction](#introduction)
  - [Quick Demo Video](#Quick-Demo-Video) 
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
  - [HandMouseController](#handmousecontroller)
  - [GameRunner](#gamerunner)

## Introduction

This project enables you to play Chicken Invaders using your hands. The camera tracks your hand movements and translates them into mouse movements and cup your hands to shoot, allowing you to control the game without using a traditional mouse.  
### Quick Demo Video
✅ [YouTube](https://youtu.be/shlkBMwmfos)  
[![Play Chicken Invaders With Hand Detection](./Images/DemoVideo.png)](https://youtu.be/shlkBMwmfos?si=2QF0DWRr1Iv-i_Qx "Play Chicken Invaders With Hand Detection")  

<img src="./Images/DemoVideo.gif" style="width:1000px;"/>


## Requirements

- Python 3.10+
- OpenCV
- MediaPipe
- NumPy
- PyAutoGUI
- PyGetWindow

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/OtaTran241/ChickenInvaders_HandPoseEstimation.git
   cd ChickenInvaders_HandPoseEstimation
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
## Usage
1. Update the "Main.py" file with the correct path to your Chicken Invaders executable if necessary (should be left as default):
   ```bash
   game_runner = GameRunner(exe_path=r"path_to_your_game_executable", window_title="Chicken Invaders", window_width=1500, window_height=1000)
   ```
2. Run the "Main.py" file:
   ```bash
   python Main.py
   ```
## Code Overview

### 1. `Game_Runner` Class

This class is designed to launch and manage a game window, along with a camera tracking window.

- **Initialization (`__init__` method):**
  - **Attributes:**
    - `exe_path`: Path to the game's executable file (e.g., `exe_path="game/rungame.exe"`).
    - `window_title`: Title of the game window (e.g., `window_title="GameRunner"`).
    - `window_width`: Desired width of the game window (e.g., `window_width=1920`).
    - `window_height`: Desired height of the game window (e.g., `window_height=1080`).

- **Running the Game (`run_game` method):**
  - **Steps:**
    1. Launches the game using the specified executable path.
    2. Waits for the game window to appear (5 seconds delay).
    3. Adjusts the game window size and position according to the specified dimensions.
    4. Moves the game window to the top-left corner of the screen.
    5. Activates the game window and simulates a mouse click.
    6. Searches for a window titled "Hand Tracking," resizes it, and moves it to the top-right corner of the screen.

### 2. `HandMouseController` Class

This class utilizes Mediapipe and OpenCV to control the mouse cursor based on hand gestures detected by the webcam.

- **Initialization (`__init__` method):**
  - **Attributes:**
    - `camera_width` and `camera_height`: Dimensions of the camera feed window (e.g., `camera_width=640`, `camera_height=480`).
    - **Mediapipe Setup:**
      - Initializes Mediapipe's hand tracking model with specified detection and tracking confidence levels.

- **Screen Coordinate Conversion (`convert_to_screen_coordinates` method):**
  - Converts hand coordinates from the camera frame to screen coordinates, mapping them relative to the game window's position and size.

- **Hand Gesture Recognition (`is_hand_closed` method):**
  - Determines if the hand is closed (i.e., a click gesture) by measuring the distance between the wrist and middle finger landmarks.

- **Running the Hand Tracking (`run` method):**
  - **Steps:**
    1. Captures video from the webcam.
    2. Processes each video frame to detect hand landmarks.
    3. Draws hand landmarks on the video frame.
    4. Calculates and moves the mouse cursor on the screen based on the detected hand position.
    5. Detects if the hand is closed to simulate a mouse click.
    6. Displays the processed video feed with hand tracking until the user presses 'q' to quit the application.


### Running the Project
1. Ensure your camera is connected and working.

2. Run the main.py script to start the game and hand tracking:
   
   ```bash
    python Main.py
    ```
4. Use your hand to control the game. The wrist position will control the mouse movement, and closing your hand will simulate a mouse click.







