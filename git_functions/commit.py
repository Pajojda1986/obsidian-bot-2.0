import os
import subprocess

from tags import day_tag
from config import PATH_TO_OBSIDIAN


def commit():
    try:
        os.chdir(os.path.expanduser(PATH_TO_OBSIDIAN))
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", day_tag], check=True)
        print("Коммит выполнен успешно!")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении git команды: {e}")
