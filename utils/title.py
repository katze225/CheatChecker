import ctypes

# Edit window title util
@staticmethod
def set(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)