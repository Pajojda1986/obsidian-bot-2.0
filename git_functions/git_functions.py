import os
import subprocess

from utils.tags import day_tag
from config import PATH_OBSIDIAN


class GitFunctions:

    repo_path = os.path.expanduser(PATH_OBSIDIAN)

    @staticmethod
    def _run_git(*args):
        subprocess.run(["git", *args], check=True,
                       cwd=GitFunctions.repo_path)

    @staticmethod
    def commit():
        try:
            GitFunctions._run_git("add", ".")
            GitFunctions._run_git("commit", "-m", day_tag)
            print("Коммит выполнен успешно!")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении git команды: {e}")

    @staticmethod
    def push():
        try:
            GitFunctions._run_git("push")
            print("Пуш выполнен успешно!")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении git команды: {e}")

    @staticmethod
    def commit_and_push():
        GitFunctions.commit()
        GitFunctions.push()
