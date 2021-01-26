import os, time
import logic
from infi.systray import SysTrayIcon
import sys

#path to watch
path_to_watch = r"C:\Users\syazv\Downloads"

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

    m = logic.Main()

    if fileChange != False:

        fileName = fileChange[0]

        fileEnding = fileChange[0].split(".")[-1]
        m.id_file(fileName,fileEnding,path_to_watch)

#leaving and diabling program
def  on_quit_callback(systray):
    print("quitting")
    systray.shutdown()
    sys.exit()
        
#defining tray stuff
systray = SysTrayIcon("icon.ico", "Downloads Manager",on_quit=on_quit_callback)

#start tray icon
systray.start()

while 1:
    main()


