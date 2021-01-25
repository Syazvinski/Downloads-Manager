from infi.systray import SysTrayIcon
import time

def say_hello(systray):
        systray.update(menu_options=menu_optionsbye)
def say_bye(systray):
        systray.update(menu_options=menu_optionshello)
menu_optionshello = (("Say Hello","hello.ico", say_hello),)
menu_optionsbye = (("Say Bye", "bye.ico", say_bye),)
systray = SysTrayIcon("icon.ico", "Hello/Bye", menu_optionshello)   
systray.start()