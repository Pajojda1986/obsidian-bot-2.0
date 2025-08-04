from notes.note import Note
from tags import day_tag


class UniversityNote(Note):
    def __init__(self, title, text):
        path = "University"
        super().__init__(title, text, path)
        self.add_tag(day_tag)
