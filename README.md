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
├── TrackingModule.py      ----------+               
├── VolumeControl.py       ----------+
├── SnakeAppearance.py     ----------+
├── SnakeApplication.py              |
├── SnakeControl.py                  |
├── SnakeKeys.py           ----------+

```

<b>TrackingModule.py - </b> Code to detect hand and finger landmarks<br>
<b>VolumeControl.py - </b> Specifies volume control gestures and connects to computers audio system <i>(Run this file to control audio using gestures)</i> <br>
<b>SnakeAppearance.py - </b> Defines reusable snake game styling <br>
<b>SnakeApplication.py - </b> Code that creates the actual snake game itself (Run this class by itself to play game with keyboard or with SnakeControl.py to play using gestures)<br>
 <b>SnakeControl.py - </b> Specifies gestures for the snake game application (run along with SnakeApplication.py) <br>
 <b>SnakeKeys.py</b> - Defines key functionality <br>

## Running the Program
1. In your command line terminal: ```git clone https://github.com/GraceKeane/gesture_control```<br>
2. Download [PyCharm Community](https://www.jetbrains.com/pycharm/download/#section=windows) (May take a while to download)
3. ```git clone https://github.com/GraceKeane/gesture_control.git```
4. Open [PyCharm Community](https://www.jetbrains.com/pycharm/download/#section=windows)
5. Click ```File```
6. Click ```Open```
7. Navigate to the cloned project and click ```gesture_control```
8. Navigate to ```VolumeControl.py```, right click, ```Run VolumeControl```
9. Navigate to ```SnakeApplication.py```, right click, ```Run SnakeApplication```
10. Navigate to ```SnakeControl.py```, right click, ```Run SnakeControl```

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
11. Program should run successfully now if not hover over red lines and import all

<i><b>Screencast of how to clone and run as well as a program demo is included in submission<b></i>
