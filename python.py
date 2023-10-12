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

# Функция для редактирования заметки по идентификатору
def edit_note(notes, note_id, new_title, new_body):
    for note in notes:
        if note["id"] == note_id:
            note["title"] = new_title
            note["body"] = new_body
            note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print(f"Заметка '{new_title}' успешно отредактирована.")
            return
    print(f"Заметка с идентификатором '{note_id}' не найдена.")

# Функция для удаления заметки по идентификатору
def delete_note(notes, note_id):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print(f"Заметка '{note['title']}' успешно удалена.")
            return
    print(f"Заметка с идентификатором '{note_id}' не найдена.")

# Функция для сохранения заметок в JSON файл
def save_notes(notes):
    with open("notes.json", "w") as json_file:
        json.dump(notes, json_file)

# Функция для загрузки заметок из JSON файла
def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as json_file:
            notes = json.load(json_file)
        return notes
    return []

# Основной цикл программы
def main():
    notes = load_notes()

    while True:
        print("\nВыберите действие:")
        print("1. Создать заметку")
        print("2. Список заметок")
        print("3. Прочитать заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выйти из программы")
        choice = input("Введите номер действия: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            create_note(notes, title, body)
        elif choice == "2":
            list_notes(notes)
        elif choice == "3":
            note_id = int(input("Введите идентификатор заметки для чтения: "))
            read_note(notes, note_id)
        elif choice == "4":
            note_id = int(input("Введите идентификатор заметки для редактирования: "))
            new_title = input("Введите новый заголовок: ")
            new_body = input("Введите новый текст: ")
            edit_note(notes, note_id, new_title, new_body)
        elif choice == "5":
            note_id = int(input("Введите идентификатор заметки для удаления: "))
            delete_note(notes, note_id)
        elif choice == "6":
            break
        else:
            print("Неправильный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
