from datetime import date

from notes.note import Note
from tags import month_tag


class DailyNote(Note):
    def __init__(self, text):

        today = date.today()
        title = str(today)
        path = "Daily Notes"

        super().__init__(title, text, path)

        self.add_tag(month_tag)
