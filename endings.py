import os
import shutil
from win10toast_persist import ToastNotifier


def whatToDo (fileName,fileEnding,path):

    

    pathWithSlash = os.path.normpath(path+r"\\")

    #notification settings
    toast = ToastNotifier()
    notificationTitle = "File Moved"
    notificationDuration = None
    iconPath = "icon.ico"

    if fileEnding == "csv":

        folderName = "data"

        fullPath = os.path.normpath(path+r"\\"+fileName)

        if not os.path.exists(os.path.normpath(path+r"\\"+"data")):
            os.makedirs(os.path.normpath(path+r"\\"+"data"))
            
        shutil.move(fullPath,os.path.normpath(path+r"\\"+"data"))

        toast.show_toast(notificationTitle,f"{fileName} has been moved to the {folderName} folder.",duration=notificationDuration,icon_path=iconPath,threaded=True)

    
        
