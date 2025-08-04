from abc import ABC


class Note(ABC):
    def __init__(self, title: str | None, text: str, path: str):
        self.__title = title
        self.__text = text
        self.__path = path
        self.__tags: list[str] = []

    def add_tag(self, *tags: str):
        for tag in tags:
            self.__tags.append(tag)

    @property
    def path(self) -> str:
        return self.__path

    @property
    def title(self) -> str | None:
        return self.__title

    @property
    def text(self) -> str:
        return self.__text

    @property
    def tags(self) -> list[str]:
        return self.__tags

    @property
    def formatted_tags(self) -> str:
        tags_string = ""
        for i in self.__tags:
            tags_string += f"[[{i}]]\n"
        return tags_string
