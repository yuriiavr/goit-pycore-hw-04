import sys
import os
from pathlib import Path
from colorama import Fore, Style, init

init()

def visualize_directory(path, indent=0):
    try:
        items = Path(path).iterdir()
        
        for item in items:
            if item.is_dir():
                print(f"{' ' * indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}") 
                visualize_directory(item, indent + 2)  
            else:
                print(f"{' ' * indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}") 
    except PermissionError:
        print(f"{' ' * indent}{Fore.RED}Доступ заборонено до: {path}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{' ' * indent}{Fore.RED}Помилка: {str(e)}{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 2:
        print("Використання: python task3.py <шлях_до_директорії>")
        return

    directory_path = sys.argv[1]

    if not os.path.exists(directory_path):
        print(f"{Fore.RED}Шлях не існує: {directory_path}{Style.RESET_ALL}")
        return

    if not os.path.isdir(directory_path):
        print(f"{Fore.RED}Це не директорія: {directory_path}{Style.RESET_ALL}")
        return

    print(f"{Fore.YELLOW}Структура директорії: {directory_path}{Style.RESET_ALL}")
    visualize_directory(directory_path)

if __name__ == "__main__":
    main()
