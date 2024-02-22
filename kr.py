import argparse
import json
from datetime import datetime

def create_note():
    note = {
        "id": generate_id(),
        "title": "Название заметки",
        "body": "Текст заметки",
        "created_at": str(datetime.now()),
        "updated_at": str(datetime.now())
    }
    return note

def save_note(note):
    with open("notes.json", "a") as file:
        file.write(json.dumps(note) + "\n")

def read_notes():
    with open("notes.json", "r") as file:
        for line in file:
            note = json.loads(line)
            print(f"ID: {note['id']}")
            print(f"Название: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата создания: {note['created_at']}")
            print(f"Дата последнего изменения: {note['updated_at']}")
            print()

def edit_note():
    note = {
        "id": "идентификатор заметки",
        "title": "Новое название заметки",
        "body": "Новый текст заметки",
        "created_at": "дата создания",
        "updated_at": str(datetime.now())
    }
    return note

def delete_note():
    note_id = "идентификатор заметки"
    return note_id

def generate_id():
    return str(datetime.now().timestamp())

def main():
    parser = argparse.ArgumentParser(description="Программа для работы с заметками.")
    parser.add_argument("--create", action="store_true", help="Создать новую заметку")
    parser.add_argument("--read", action="store_true", help="Читать список всех заметок")
    parser.add_argument("--edit", action="store_true", help="Редактировать существующую заметку")
    parser.add_argument("--delete", action="store_true", help="Удалить заметку")
    args = parser.parse_args()

    if args.create:
        note = create_note()
        save_note(note)
        print("Заметка успешно создана и сохранена.")
    elif args.read:
        read_notes()
    elif args.edit:
        note = edit_note()
        print("Заметка успешно отредактирована.")
    elif args.delete:
        note_id = delete_note()
        print("Заметка успешно удалена.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()