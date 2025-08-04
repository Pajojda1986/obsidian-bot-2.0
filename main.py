from notes import DailyNote, NoteWriter
if __name__ == "__main__":
    note = DailyNote("Принял решение переписать бота")

    writer = NoteWriter()
    writer.write_note(note)
