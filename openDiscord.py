import json
import logging
import os
from tkinter.filedialog import askopenfilename

import keyboard



def getMessage(prevFile):
    '''
    Attempts to open a file containing a message.
    If a previous file has been found in the json, attempt to load it first.
    On failure, prompt user to select a new message file of .txt type.
    If successful, return the file containing the message and the message itself.
    '''
    if prevFile and os.path.exists(prevFile):
        print("Previous file exists. Opening....")
        msgFile = prevFile
    else:
        print("Previous file does not exist. Please open a new text file.")
        try:
            msgFile = askopenfilename()
        except:
            exit("Error opening file. Please select a valid text file.")
    
    if not msgFile.endswith('.txt'):
        print("Invalid file type. Please choose a .txt file.")
        return None

    try:
        file = open(msgFile, "r")
    except:
        exit("Error opening file.")

    message = file.read()
    
    return msgFile, message


def openDiscord():
    '''
    Attempts to find the location of discord within the %localappdata% directory.
    One success, it launches discord (or makes it the focused application).
    '''
    startDir = os.getenv('LOCALAPPDATA') + '\\Discord\\'
    print(startDir)
    if not os.path.exists(startDir):
        exit("Discord not found on system.")
    
    for root, dirs, files in os.walk(startDir):
        for name in files:
            if name == "Discord.exe":
                targetDir = os.path.abspath(os.path.join(root, name))

    if not targetDir:
        exit("Discord application not found.")
    print(targetDir)
    os.startfile(targetDir)


def getKeystrokes():
    '''
    Record keystrokes until a specified key is pressed and return them.
    '''
    keyStroke = keyboard.record(until='esc')
    return keyStroke

def main():
    #dict to hold json data
    info = {}

    #load json file if it exists
    if (os.path.exists(os.getcwd() + '\\discordData.json')):
        print("discordData.json exists. Loading data...")
        file = open('discordData.json')
        info = json.load(file)

    #if previous file exists in json, load it into variable, else None
    prevFile = info['prevFile'] if 'prevFile' in info.keys() else None

    #get the file containing the message and the message itself
    msgFile, message = getMessage(prevFile)

    #save current file over previous one (in json) if it doesn't exist or if user opened a new file
    if not prevFile or prevFile != msgFile:
        info['prevFile'] = msgFile

    #open the discord appliction
    #openDiscord()

    #get keystrokes
    keystrokes = getKeystrokes()
    stringKey = list(keystrokes)
    print(stringKey)
    stringKey = [str(key)[13:] for key in keystrokes]
    #print recorded keystrokes
    print(stringKey)

    #if json already exists, overwrite with updated information, else create new json with the information
    if os.path.exists(os.getcwd() + 'discordData.json'):
        json.dump(info, file)
    else:
        with open('discordData.json', 'w') as f:
            json.dump(info, f)


if __name__ == "__main__":
    main()