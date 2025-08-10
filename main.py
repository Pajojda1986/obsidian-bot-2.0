from notes import DailyNote, NoteWriter, PeopleNote
if __name__ == "__main__":
    note = PeopleNote("Сеня", "Мой кент")

    writer = NoteWriter()
    writer.write_note(note)
