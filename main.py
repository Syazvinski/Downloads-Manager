import os, time
import logic
from infi.systray import SysTrayIcon
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path

#path that we are watching
path_to_watch = str(os.path.join(Path.home(), "Downloads"))


#making before list
before = dict ([(f, None) for f in os.listdir (path_to_watch)])

def detectFileChange():
    global before
    time.sleep (1)
    after = dict ([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]
    before = after
    if added: 
        return added
    else:
        return False


def main():

    global path_to_watch

    fileChange = detectFileChange()
    if fileChange != False:

        fullFileName = fileChange[0]
        fileEnding = fileChange[0].split(".")[-1]
        fileName = fullFileName.replace(fileEnding,"").replace(".","")
        m = logic.Main()
        m.id_file(fullFileName,fileEnding,path_to_watch)


def organizeFolder(systray):
    global path_to_watch
    onlyfiles = [f for f in listdir(path_to_watch) if isfile(join(path_to_watch, f))]
    for fileName in onlyfiles:
        fileEnding = fileName.split(".")[-1]
        m = logic.Main()
        m.id_file(fileName,fileEnding,path_to_watch)

#leaving and diabling program
def  on_quit_callback(systray):
    print("quitting")
    #os exit to quit all threads
    os._exit(1)
        
menu_options = (('Toggle Auto Organize', "automation.ico", on_quit_callback),
                ('Organize Folder', "folder.ico", organizeFolder),
                ('Settings', "settings.ico", (('Change Folder Path', "path.ico", on_quit_callback),
                                               ('File/Folder Settings', "settings.ico", on_quit_callback),
                                              ))
               )

#defining tray stuff
systray = SysTrayIcon("icon.ico", "Downloads Manager v1.0",menu_options,on_quit=on_quit_callback)

#start tray icon
systray.start()



if __name__ == "__main__":
    while True:
        main()

