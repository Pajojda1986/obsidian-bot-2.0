from notes import DailyNote, NoteWriter, PeopleNote
from git_functions import GitFunctions
if __name__ == "__main__":

    note = PeopleNote("Дмитрий Z", "Иматор говно")

    writer = NoteWriter()
    writer.write_note(note)
    GitFunctions.commit_and_push()
