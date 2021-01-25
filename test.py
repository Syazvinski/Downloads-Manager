from infi.systray import SysTrayIcon


def say_hello():
    print("Hello, World!")


menu_options = (("Say Hello", None, say_hello),)

systray = SysTrayIcon("icon.ico", "Download Manager", menu_options)

#sart systray
systray.start()