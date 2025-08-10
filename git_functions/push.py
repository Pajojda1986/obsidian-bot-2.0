import os
import subprocess

from tags import day_tag
from config import PATH_TO_OBSIDIAN


def push():
    try:
        os.chdir(os.path.expanduser(PATH_TO_OBSIDIAN))
        subprocess.run(["git", "push"], check=True)
        print("Пуш выполнен успешно!")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении git команды: {e}")
