import psutil
import re

# Cheat process list
process_list = ['DeadCode', 'DeadCodeLauncher', 'Nursultan', 'expensive', 'wild', 'nurik', 'excellent', 'arbuz', 'celestial', 'celka']

# Module check processes
def check():
    print("Проверка процессов...")
    
    found_processes = []
    process_list_patterns = [re.compile(re.escape(name).replace(r'\*', '.*'), re.IGNORECASE) for name in process_list]

    for process in psutil.process_iter(['pid', 'name']):
        process_name_lower = process.info['name'].lower()
        if any(pattern.match(process_name_lower) for pattern in process_list_patterns):
            found_processes.append(process.info['name'])

    if found_processes:
        print("Процессы найдены:")
        for process_name in found_processes:
            print(process_name)
    else:
        print("Ничего не найдено")