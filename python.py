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
# Функция для чтения списка заметок
def list_notes(notes):
    if notes:
        print("Список заметок:")
        for note in notes:
            print(f"{note['id']}. {note['title']} (Дата: {note['timestamp']})")
    else:
        print("У вас нет заметок.")

# Функция для чтения заметки по идентификатору
def read_note(notes, note_id):
    for note in notes:
        if note["id"] == note_id:
            print(f"Заметка '{note['title']}' (Дата: {note['timestamp']}):\n{note['body']}")
            return
    print(f"Заметка с идентификатором '{note_id}' не найдена.")