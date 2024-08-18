import scandir
import psutil
from concurrent.futures import ThreadPoolExecutor

# Cheat files list
search_list = [
    ("user_info.jar", "Библиотека чита"),
    ("viaversion-4.7.1-SNAPSHOT", "Библиотека чита"),
    ("viabackwards-4.7.1-SNAPSHOT", "Библиотека чита"),
    ("baritone", "Запрещенный мод"),
    ("Zamorozka", "Чит"),
    ("antiafk", "Чит"),
    ("elytra", "Чит"),
    ("X-Ray", "Запрещенный мод/РесурсПак"),
    ("freecam", "Запрещенный мод"),
    ("InvMove", "Запрещенный мод"),
    ("double_hotbar", "Запрещенный мод"),
    ("WorldTools", "Запрещенный мод"),
    ("NeoWare", "Чит"),
    ("BebraWare", "Чит"),
    ("Nursultan", "Чит"),
    ("nurik", "Чит"),
    ("Expensive", "Чит"),
    ("Wild", "Чит"),
    ("Arbuz", "Чит"),
    ("Impact", "Чит"),
    ("Impact", "Чит"),
    ("excellent", "Чит"),
    ("celestial", "Чит"),
    ("celka", "Чит"),
    ("thunderhack", "Чит"),
    ("liquidbounce", "Чит"),
    ("liquidlauncher", "Чит"),
    ("calestial", "Чит"),
    ("autobuy", "Запрещенный мод"),
    ("Wurst", "Чит"),
    ("Inertia", "Чит"),
    ("Impact", "Чит"),
    ("rename_me_please", "Чит"),
    ("RusherHack", "Чит"),
    ("Konas", "Чит"),
    ("WintWare", "Чит"),
    ("Norules", "Чит"),
    ("Akrien", "Чит"),
    ("DeadCode", "Чит"),
    ("Eternity", "Чит"),
    ("WEXSIDE", "Чит"),
    ("RichPremium", "Чит"),
    ("EdItMe", "Чит"),
    ("mc100", "Чит"),
    ("delta", "Чит"),
    ("ExLoader", "Чит"),
    ("MouseTweaks", "Чит"),
    ("AutoChest", "Чит"),
    ("ChestStealer", "Чит"),
    ("dauntiblyat", "Чит"),
    ("meteor", "Чит"),
    ("ares", "Чит"),
    ("aristois", "Чит"),
    ("bleachhack", "Чит"),
    ("UsbOblivion", "Чит"),
    ("Wise", "Чит"),
    ("Winner", "Чит"),
    ("Fluger", "Чит"),
    ("Centric", "Чит"),
    ("Minced", "Чит"),
]

# Allowed extensions list
allowed_extensions = [".jar", ".rar", ".zip", ".lnk", ".exe"] 


# Module check files
def check():
    results = []

    def search_files(path):
        try:
            for entry in scandir.scandir(path):
                if entry.is_file() and any(entry.name.lower().endswith(ext) for ext in allowed_extensions):
                    for term, description in search_list:
                        if term.lower() in entry.name.lower():
                            results.append((entry.path, description))
                elif entry.is_dir():
                    search_files(entry.path)
        except (OSError, PermissionError):
            pass

    with ThreadPoolExecutor() as executor:
        all_partitions = psutil.disk_partitions(all=True)
        paths_to_search = [partition.mountpoint for partition in all_partitions]

        futures = [executor.submit(search_files, path) for path in paths_to_search]

        for future in futures:
            future.result()

    if results:
        print("Найдены файлы:")
        for file, description in results:
            print(f"{file} - {description}")
    else:
        print("Ничего не было найдено.")

    return results