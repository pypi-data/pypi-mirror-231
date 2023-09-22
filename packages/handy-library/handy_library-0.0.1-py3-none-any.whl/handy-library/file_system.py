import inspect
import os
import sys


class FileSystem:
    """Работа с системными путями"""
    def __init__(self):
        self.project_directory = self.get_project_directory()

    def get_project_directory(self, follow_symlinks=True):
        """
        Получить текущую директорию проекта.

        :param bool follow_symlinks: Возвращает канонический путь, убирая все символические ссылки
        """
        if getattr(sys, 'frozen', False):
            path = os.path.abspath(sys.executable)
        else:
            path = inspect.getabsfile(self.get_project_directory)
        if follow_symlinks:
            path = os.path.realpath(path)
        return os.path.dirname(path)
