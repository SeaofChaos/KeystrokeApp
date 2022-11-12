import os
from tkinter.filedialog import askopenfilename
import json
import keyboard


def getMessage(prevFile):
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
    startDir = os.getenv('LOCALAPPDATA') + '\\Discord\\'
    print(startDir)
    if not os.path.exists(startDir):
        exit("Discord not found on system.")
    
    for root, dirs, files in os.walk(startDir):
        for name in files:
            if name == "Discord.exe":
                targetDir = os.path.abspath(os.path.join(root, name))
                print(name)
    
    if not targetDir:
        exit("Discord application not found.")
    print(targetDir)
    os.startfile(targetDir)


def main():
    info = {}

    if (os.path.exists(os.getcwd() + '\\discordData.json')):
        print("discordData.json exists. Loading data...")
        file = open('discordData.json')
        info = json.load(file)

    prevFile = info['prevFile'] if 'prevFile' in info.keys() else None

    msgFile, message = getMessage(prevFile)

    if not prevFile or prevFile != msgFile:
        info['prevFile'] = msgFile

    openDiscord()

    if os.path.exists(os.getcwd() + 'discordData.json'):
        json.dump(info, file)
    else:
        with open('discordData.json', 'w') as f:
            json.dump(info, f)


if __name__ == "__main__":
    main()