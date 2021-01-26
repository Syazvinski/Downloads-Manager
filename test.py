from infi.systray import SysTrayIcon


systray = SysTrayIcon("icon.ico", "Downloads Manager")
systray.start()

systray.update(hover_text=item)