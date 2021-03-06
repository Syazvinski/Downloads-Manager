import os
import shutil
from win10toast_persist import ToastNotifier
import time
import pickle

class Main():

    def __init__(self):

        #notification settings
        self.toast = ToastNotifier()

        #notification title
        self.notificationTitle = "File Moved"

        #notificatin duration set to none for notification to linger
        self.notificationDuration = None

        #icon path
        self.iconPath = "icon.ico"

        #time to wait before moving file
        self.timeToWait = 0.1

        #endings and where to move
        self.data = ["csv","txt"]
        self.documents = ["pdf","doc","xlsx","xls","xlsm"]
        self.photos = ["jpg","jpeg","bmp","png","wepb","heic","jfif","ico"]
        self.zipped = ["zip"]
        self.video = ["mp4","mov","avi"]
        self.installers = ["exe","msi","dll"]
        self.audio = ["mp3","wav"]

    def move_and_notify(self,folderName):
        time.sleep(self.timeToWait)

        fullPath = os.path.normpath(self.path+r"\\"+self.fullFileName)

        if not os.path.exists(os.path.normpath(self.path+r"\\"+folderName)):
            os.makedirs(os.path.normpath(self.path+r"\\"+folderName))
            
        try:
            shutil.move(fullPath,os.path.normpath(self.path+r"\\"+folderName))
        except:
            self.send_notification("Error","This file already exists")

        self.toast.show_toast(self.notificationTitle,f"{self.fullFileName} has been moved to the {folderName} folder.",duration=self.notificationDuration,icon_path=self.iconPath,threaded=True)
    
    def send_notification(self,title,body):
        self.toast.show_toast(title,body,duration=self.notificationDuration,icon_path=self.iconPath,threaded=True)


    def id_file(self,fullFileName,fileEnding,path):
        self.fullFileName = fullFileName
        self.fileEnding = fileEnding
        self.path = path

        for i in self.data:
            if self.fileEnding == i:
                self.move_and_notify("data")

        for i in self.documents:
            if self.fileEnding == i:
                self.move_and_notify("documents")

        for i in self.photos:
            if self.fileEnding == i:
                self.move_and_notify("photos")

        for i in self.zipped:
            if self.fileEnding == i:
                self.move_and_notify("zipped")

        for i in self.video:
            if self.fileEnding == i:
                self.move_and_notify("video")

        for i in self.installers:
            if self.fileEnding == i:
                self.move_and_notify("installers")

        for i in self.audio:
            if self.fileEnding == i:
                self.move_and_notify("audio")



        

    
        
