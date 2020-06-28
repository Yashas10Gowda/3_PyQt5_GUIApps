# Developed 3 PyQt5 GUI/Desktop Applications

## ImageShrinker
As I'm Full-Stack Web Developer, I always wanted a tool to optimise the size of the images so it loads faster on the client's devices without bankrupting their internet packets ;)

## CPUStats
As I was lazy to press all three button i.e. Ctrl+Shift+Esc in Windows at once, I decided to build my own GUI app which should launch on two clicks ;) . And thus saved myself from hunting down Task Manager shortcut in my whole machine(which has got 600 million directories).

## Logger
Well there's no specific reason why I developed this app but it made me realize how easy it is to write .csv or .json files programmatiacally (or any file for that matter) thereby a non-programmer can also easily understand the data.
It could have also been hooked to a Rest-API using "requests" library, but I did not want an entire server to run just to keep this application alive.

### To run in Development mode
```
# Install the Dependency First 
pip install pyqt5

# Run It
python imageshrinker.py

# OR or AND
python cpustats.py

# OR or AND
python logger.py

# --> these are comments, if you're using windows use git bash or Try avoiding the comments in cmd-prompt/powershell.
```

### To run in Production mode

Double click on .exe files ;) but there is catch, these files are only tested in Win 8.1 Pro and it does not run on Mac or Linux.
But you can always try running in development mode since it just needs a python interpretor with pip.
Either clone this repo or just download the .exe files to test it out.
