import json
import os
import sys
from .utils import NoIndent, NoIndentEncoder
from json import JSONDecodeError
from types import SimpleNamespace
from typing import List

from loguru import logger
from rich.console import Console
from rich.prompt import Prompt

console = Console()


class Logger:
    """Логер"""

    def logger_setup(self, custom_debug=False, threads=True):
        logger.remove()
        if threads:
            logger.add(sys.stdout, colorize=True, format="[<fg #929292><b>{time:DD-MM-YYYY HH:mm:ss}</b></fg #929292>] "
                                                         "[<fg #00ff00><b>{thread.name}</b></fg #00ff00>] [<level>{level}"
                                                         "</level>] - {message}")
        else:
            logger.add(sys.stdout, colorize=True, format="[<fg #929292><b>{time:DD-MM-YYYY HH:mm:ss}</b></fg #929292>] "
                                                         "[<level>{level}"
                                                         "</level>] - {message}")

        if custom_debug: self.debug_setup()
        return logger

    @staticmethod
    def debug_setup():
        logger.add("debug.log", format="{time:DD-MM-YYYY HH:mm:ss} | {thread.name} | {level} | {message}",
                   level="DEBUG",
                   rotation="1 MB",
                   compression="zip",
                   serialize=False)

    @staticmethod
    def custom_tag(name: str):
        console.print(f"[bold blue]{name} запущен![/]")
        console.print("[bold white]По всем вопросам обращаться в Telegram: @svja7ik[/]")


class ConfigLoader:
    """Конфигуратор конфигурации"""

    class ConfigParam:
        def __init__(self, name, description=None, value=None, value_type=None):
            self.name = name
            self.value = value
            if value_type is None and type(value) not in [list, dict]:
                self.value_type = type(value)
            else:
                self.value_type = value_type
            self.description = description

        def convert(self, value):
            if self.value_type in [list, dict]:
                self.value = json.loads(value)
                if type(self.value) not in [list, dict]:
                    return False
            else:
                self.value = self.value_type(value)
            return self.value

        def __dict__(self):
            if self.description:
                return {f'{self.name}_description': self.description, self.name: self.value}
            else:
                return {self.name: self.value}

    @staticmethod
    def __check_keys_in_config(structure, config):
        missing_keys = []
        if structure:
            for key in structure:
                key = key.name
                if key not in config.__dict__.keys():
                    missing_keys.append(key)
            if len(missing_keys) > 0:
                keys = ', '.join(missing_keys)
                if len(missing_keys) > 1: console.print(f"[bold white][CONFIG] - Отсутствуют параметры: {keys}[/]")
                else: console.print(f"[bold white][CONFIG] - Отсутствует параметр: {keys}[/]")

    @staticmethod
    def load_config_outer(*d_args, **d_kwargs):
        def outer(func):
            def inner(*args, **kwargs):  # Параметры функции
                while True:
                    try:
                        return func(*args, **kwargs)
                    except ValueError:
                        continue

            return inner

        return outer

    @load_config_outer()
    def load_config(self, filename='config.json', structure: List[ConfigParam] | None = None, auto_clear=False):
        if auto_clear: os.remove(filename)
        if not os.path.exists(filename):
            with open(filename, mode='x', encoding='utf-8', errors='ignore') as file:
                if structure:
                    file_structure = {}
                    for config_param in structure:
                        while True:
                            if config_param.value:
                                config_param.value = NoIndent(config_param.value)
                                break

                            if config_param.description:
                                if config_param.value_type in [list]:
                                    status = config_param.value = NoIndent(config_param.convert(
                                        Prompt.ask(f"[bold white][CONFIG] - Параметр "
                                                   f"({config_param.name}, "
                                                   f"{config_param.description}) не задан.\n"
                                                   f"[CONFIG] - Используйте формат [1, 2, 3] для заполнения.\n"
                                                   f"Впишите значение[/]")))
                                else:
                                    status = config_param.value = config_param.convert(
                                        Prompt.ask(f"[bold white][CONFIG] - Параметр "
                                                   f"({config_param.name}, "
                                                   f"{config_param.description}) не задан.\n"
                                                   f"Впишите значение[/]"))

                            else:
                                if config_param.value_type in [list]:
                                    status = config_param.value = NoIndent(config_param.convert(
                                        Prompt.ask(f"[bold white][CONFIG] - Параметр "
                                                   f"({config_param.name}"
                                                   f") не задан.\n"
                                                   f"[CONFIG] - Используйте формат [1, 2, 3] для заполнения.\n"
                                                   f"Впишите значение[/]")))
                                else:
                                    status = config_param.value = config_param.convert(
                                        Prompt.ask(f"[bold white][CONFIG] - Параметр "
                                                   f"({config_param.name}"
                                                   f") не задан.\n"
                                                   f"Впишите значение[/]"))
                            if status: break

                        file_structure.update(config_param.__dict__())
                    file.write(json.dumps(file_structure, indent=4, cls=NoIndentEncoder,
                                          sort_keys=False, ensure_ascii=False))
        try:
            with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
                config = json.load(file, object_hook=lambda d: SimpleNamespace(**d))
        except JSONDecodeError:
            console.print(f"[bold white][CONFIG] - Отсутствуют данные в конфигурации[/]")
            os.remove(filename)
            raise ValueError

        self.__check_keys_in_config(structure, config)
        return config
