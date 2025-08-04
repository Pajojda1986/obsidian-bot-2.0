from pathlib import Path

from notes.note import Note
from config import PATH_OBSIDIAN


class NoteWriter:
    def write_note(self, note: Note):

        path_to_note = Path(PATH_OBSIDIAN).expanduser() / \
            note.path / f"{note.title}.md"

        path_to_note.parent.mkdir(parents=True, exist_ok=True)

        if path_to_note.exists():
            with path_to_note.open("a", encoding="utf-8") as file:
                file.write(f"\n{note.text}")
        else:
            with path_to_note.open("w", encoding="utf-8") as file:
                file.write(f"{note.formatted_tags}\n{note.text}")
