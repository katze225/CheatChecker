import platform

# Virtual keywords list
virtual_keywords = ['virtual', 'vmware', 'hypervisor', 'qemu', 'xen']

# Module check virtual machine
def check():
    print("Проверка на виртуальную машину...")
    system_info = platform.system().lower()
    
    for keyword in virtual_keywords:
        if keyword in system_info:
            print("Это виртуальная машина!")
            return True
    
    if 'cdrom' in platform.uname().machine.lower():
        print("Это виртуальная машина!")
        return True
    
    print("Это не виртуальная машина")