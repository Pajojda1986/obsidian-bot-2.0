from notes.note import Note
from utils.tags import day_tag


class PeopleNote(Note):
    def __init__(self, title, text):
        path = "People"
        super().__init__(title, text, path)
        self.add_tag(day_tag)
