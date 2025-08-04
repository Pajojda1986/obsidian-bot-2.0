from datetime import date

from notes.note import Note


class DailyNote(Note):
    def __init__(self, text):

        today = date.today()
        title = str(today)
        path = "Daily Notes"

        super().__init__(title, text, path)

        month_tag = f"{today.year}-{today.month}"
        self.add_tag(month_tag)
