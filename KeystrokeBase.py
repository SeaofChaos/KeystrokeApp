import json
import os
from tkinter import *
from tkinter.filedialog import askopenfilename
import keyboard
import time

contentFileName = 'sessionInfo.json'
contentJSONPath = os.getcwd() + '\\Content\\' + contentFileName


def loadJSON(fileExists):
    info = {}
    #load json file if it exists
    if fileExists:
        #makes sure JSON file is not empty
        if os.stat(contentJSONPath).st_size == 0:
            print("No previous data found. Continuing without presets...")
            fileExists = False
            os.remove(contentJSONPath)
        else:
            print("Previous session data exists. Loading data...")
            file = open(contentJSONPath)
            try:
                info = json.load(file)
            except ValueError:
                exit((f"Error loading file {os.path.basename(contentJSONPath)}."
                    " Make sure it's in the proper format."))

    return info


def getMessage(prevFile):
    '''
    Attempts to open a file containing a message.
    If a previous file has been found in the json, attempt to load it first.
    On failure, prompt user to select a new message file of .txt type.
    If successful, return the file path and the message.
    '''
    #attempt to load file if stored in JSON
    if prevFile and os.path.exists(prevFile):
        print("Attempting to load data from file...")
        msgFile = prevFile
    #if file does not exist, prompt user to select new file
    else:
        print("Previous file does not exist. Please open a new text file.")
        
        #make sure user selects a valid file
        try:
            msgFile = askopenfilename()
        except ValueError:
            exit("Error opening file. Please select a valid text file.")
    
    #if file is not .txt, exit
    if not msgFile.endswith('.txt'):
        exit("Invalid file type. Please choose a .txt file.")

    #open file
    try:
        with open(msgFile) as file:
            #read in entire file
            message = file.read()
    except ValueError:
        exit("Error opening file.")
    
    return msgFile, message


def openDiscord():
    '''
    Attempts to find location of discord within the %localappdata% directory.
    One success, it launches discord (or makes it the focused application).
    '''
    #try to locate discord
    startDir = os.getenv('LOCALAPPDATA') + '\\Discord\\'
    print(startDir)
    if not os.path.exists(startDir):
        exit("Discord not found on system.")
    
    #loop through files in %localappdata% directory
    for root, dirs, files in os.walk(startDir):
        for name in files:
            if name == "Discord.exe":
                targetDir = os.path.abspath(os.path.join(root, name))

    #if Discord not found, exit program
    if not targetDir:
        exit("Discord application not found.")

    #start/focus discord
    os.startfile(targetDir)


def getKeystrokes(secBeforeRec):
    '''
    Record keystrokes until a specified key is pressed and return them.
    '''
    #countdown must be greater than 0 and 2 digits long
    if secBeforeRec > 99 or secBeforeRec < 0:
        exit("Invalid countdown. Set keystroke countdown between 0 and 100.")

    #countdown
    for i in range(secBeforeRec+1):
        print("\r", end='')
        print("Recording inputs in:", secBeforeRec-i, end='  ')
        time.sleep(1)
    
    print("\nStarting...")
    print("Press the Escape key to stop recording")

    #get keystrokes
    keystrokes = keyboard.record(until='esc')
    print("Finish")

    #print recorded keystrokes
    stringKey = list(keystrokes)
    #print(stringKey)
    stringKey = [str(key)[13:] for key in keystrokes]
    print("Inputted keystrokes: ", stringKey)

    return keystrokes


def main():
    #mainWindow = Tk()
    #Label(mainWindow, text='Hello World').pack()
    #mainWindow.mainloop()

    fileExists = os.path.exists(contentJSONPath)

    #dict to hold json data
    info = loadJSON(fileExists)

    #if previous file exists in json, load it into variable, else None
    prevFile = info['prevFile'] if 'prevFile' in info.keys() else None

    #get the file containing the message and the message itself
    try:
        msgFile, message = getMessage(prevFile)
    except ValueError:
        exit("Failed to load message. Make sure the .txt file contains valid characters.")

    print("Message: \n", message)

    #save current file over previous one (in json) if it doesn't exist or if user opened a new file
    if not prevFile or prevFile != msgFile:
        info['prevFile'] = msgFile

    #open the discord appliction
    #openDiscord()

    #get keystrokes
    keystrokes = getKeystrokes(3)

    #overwrite json with new information
    with open(contentJSONPath, 'w') as f:
        json.dump(info, f, indent=4)


if __name__ == "__main__":
    main()