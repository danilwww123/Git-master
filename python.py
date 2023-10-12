import json
import os
import datetime

# Функция для создания новой заметки
def create_note(notes, title, body):
    note_id = len(notes) + 1
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_note = {
        "id": note_id,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(new_note)
    save_notes(notes)
    print(f"Заметка '{title}' успешно создана.")
