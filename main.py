import utils.title as title
import modules.virtual as virtual
import modules.processes as processes
import modules.files as files
import time
import os

build = "v0.1"
logo = '''
█▀▀ █░█ █▀▀ ▄▀█ ▀█▀ █▀▀ █░█ █▀▀ █▄▀ █▀▀ █▀█
█▄▄ █▀█ ██▄ █▀█ ░█░ █▄▄ █▀█ ██▄ █░█ ██▄ █▀▄

       Build v0.1 | github.com/katze225
'''
    
def main():
    title.set("CheatCheker | " + build)
    print(logo)

    # Check virtual machine
    virtual.check()
    print()

    # Check processes
    processes.check()
    print()

    # Check files
    print("Проверка файлов...")
    files.check()
    print()
    
    input("Нажмите Enter, чтобы закрыть программу...")

if __name__ == "__main__":
    main()
