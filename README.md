# Zoom Automation
A python script that automatically joins a zoom meeting based on your timetable.

## What does it do?
It performs the following processes:
1. Checks the "Schedule.csv" file to look for meetings that are going to start.
2. As soon as the current time matches any meeting time it opens the Zoom Desktop application.
3. Navigates the cursor automatically to various steps to join the meeting.
4. The meeting ID and password is extracted from "Schedule.csv" and entered into the Zoom app automatically.

## Prerequisites
1. Zoom app must be installed in your system.
2. You must be logged in to your Zoom account.
3. Meeting time for the day along with Meeting ID and passcode must be entered manually once into "Schedule.csv"

## How to use?
1. The best way to use my script is to firstly clone the git repo where you want to.
2. Be sure to add the location where Zoom.exe is installed in your system (mostly you would only need to change the USER profile)
3. Change directory of buttons images to access them in the code accordingly
4. Open "Schedule.csv" and fill in the Meeting Time, Meeting ID and Passcode of each meeting you want to join automatically.
5. Open "Zoom.py".

NOTE: Meeting Time must be in Hours and Minutes format only!

## What happens behind the scene?
1. An infinite loop keeps checking the current time of the system using "datetime.now" funtion.
2. The zoom app is opened using "subprocess.Popen()" funtion as soon as current time matches the time mentioned in "meetingschedule.csv".
3. "pyautogui.locateOnScreen()" function locates the image of join button on the screen and returns the position.
4. "pyautogui.moveTo()" moves the cursor to that location.
5. "pyautogui.click()" performs a click operation.
6. The meeting Id and Passcode are entered using the "keyboard.write()" command.
