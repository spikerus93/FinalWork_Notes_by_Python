import model.note


def read_file():
    try:
        array = []
        file = open("notes.csv", mode='r', encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            str_n = n.split(";")
            note = model.note.Note(
                id=str_n[0], title=str_n[1], body=str_n[2], date=str_n[3])
            array.append(note)
    except Exception:
        print("Заметки отсутствуют")
    finally:
        return array
