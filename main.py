from notes import DailyNote, NoteWriter

if __name__ == "__main__":
    note = DailyNote("Привет, лошара")
    writer = NoteWriter()
    writer.write_note(note)
