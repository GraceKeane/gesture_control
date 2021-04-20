<h2 align="center">
    Gesture Recognition Project
</h3>

<h3 align="center">
    A program written in Python to control computer functionality using hand gestures
</h4>

<p align="center">
  <img src="./Images/GMIT.jpeg" width=600 height=250/>
</p>

## Project Details
Heading  | Details
-------- | -------------------------------------
Project  | [Project Spec](https://learnonline.gmit.ie/pluginfile.php/316035/mod_resource/content/0/Gesture%20Based%20UI%20Project.pdf)
Course   | BSc (Hons) in Software Development
Module   | Gesture UI Development
Author   | Grace Keane 
ID       | G00359990
Lecturer | Damien Costello

## Contents
- [Repository Description](#repository-description)
- [Running the Program](#running-the-program)
- [Setting up Movie environment](#setting-up-movie-environment)
- [software used](#software-used)
- [Software imports used](#software-imports-used)
- [Purpose of the application](#sha512-overview)
- [Appropriate gestures](#appropriate-gestures)
- [Hardware used in creating this application](#hardware-used-in-creating-this-application)
- [Architecture for the solution](#architecture-for-the-solution)
- [Testing](#testing)
- [Conclusion and Recommendations](#conclusion-and-recommendations)
- [Referances](#referances)

## Repository Description
```bash
├── Images # Folders contains images discussed in README.md
│   ├──  # GMIT.jpeg
│   └──  # Image 2
│   └──  # Image 3
│   └──  # Image 4
├── Screencasts # Folder containing screencasts of how to set-up, deploy and run project
│   ├── # Screencast 1 (Running)
|   └── # Screencast 2 (Demo)
├── .gitignore # Text file listing files to ignore
├── README.md # Full overview and description of project
├── FingerTracker.py       ----------+
├── HandTracker.py                   |
├── TrackingModule.py                |
├── VolumeControl.py       --------- +
├── SnakeAppearance.py     ----------+
├── SnakeApplication.py              |
├── SnakeControl.py                  |
├── SnakeKeys.py           ----------+

```

## Running the Program
1. In your command line terminal: ```git clone https://github.com/GraceKeane/gesture_control```<br>
2. Download [PyCharm Community](https://www.jetbrains.com/pycharm/download/#section=windows) (May take a while to download)
3. Create a new folder and ```git clone https://github.com/GraceKeane/gesture_control.git```
4. Open [PyCharm Community](https://www.jetbrains.com/pycharm/download/#section=windows)
5. Click ```File```
6. Click ```Open```
7. Navigate to the cloned project and click ```gesture_control```
8. Navigate to ```VolumeControl.py```, right click, ```Run VolumeControl```

<b>NOTE: You may need to add Python to the interpreter - Steps are defined below</b>
1. Click ```File```
2. Click ```Settings```
3. Click ```Project: gesture_control```
4. Click ```Interpreter```
5. Click ```Python Interpreter``` down arrow
6. Click ```Show all```
7. Click ```+```
8. Program should auto pick up the ```venv``` file
9. Click ```ok```
10. Wait for imports to be installed (Should only take a few seconds)
11. Program should run successfully now

- Add screencast to explain how to run goes here


## Software used
- [Python 3.8.5](https://www.anaconda.com/products/individual)
- [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)
- [Open CV](https://opencv.org/) 

## Software imports used
- MediaPipe Hands
- [PyCaw](https://github.com/AndreMiras/pycaw)
- PyAutoGUI
- PyGame

## Purpose of the application
The purpose of my application is to allow OpenCv to detect and analyse hand gestures and then use these gestures to control computer functionality.

## Appropriate gestures
- Images of gestures used here

## Hardware used in creating this application
- Computer 
- Computer Camera

## Architecture for the solution

## Testing

## Conclusion and Recommendations
- What I learned?
- Final impression of the project?
- What I would improve?

## Referances
- OpenCv, General Information, <br>
https://docs.opencv.org/3.4/d0/da7/videoio_overview.html <br>
- MediaPipe, Mediapipe Hands, <br>
    https://google.github.io/mediapipe/solutions/hands.html <br>
- GitHub, PyCaw Import to get access to computers audio system, <br>
   https://github.com/AndreMiras/pycaw
- StackOverflow, Apply .gitignore on an existing repository already, <br>
  tracking large number of files <br>
https://stackoverflow.com/a/52539775 <br>
- Zapsplat, Game Music, <br>
https://www.zapsplat.com/page/3/?s=game+music+&post_type=music&sound-effect-category-id <br>
- YouTube, How to build SNAKE in python, <br>
https://www.youtube.com/watch?v=9bBgyOkoBQ0 <br>