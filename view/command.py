import model.note
import model.writer.read as rF
import model.writer.save as sF


def add_note():
    title = input("Введите Заголовок заметки: \n")
    body = input("Введите Описание заметки: \n")
    note = model.note.Note(title=title, body=body)
    array_notes = rF.read_file()
    for i in array_notes:
        if model.note.Note.get_id(note) == model.note.Note.get_id(i):
            model.note.Note.set_id(note)
    array_notes.append(note)
    sF.save_file(array_notes, 'a')
    print("Заметка добавлена в Журнал.")


def show(txt):
    array_notes = rF.read_file()

    if array_notes:
        if txt == "all":
            print("Журнал заметок: ")
            for i in array_notes:
                print(model.note.Note.map_Info(i))
    elif txt == "ID":
        for i in array_notes:
            print("ID: ", model.note.Note.get_id(i))
        id = input("\n Введите id Заметки: ")
        flag = True
        for i in array_notes:
            if id == model.note.Note.get_id(i):
                print(model.note.Note.map_Info(i))
                flag = False
            if flag:
                print("Нет такого id!")
    elif txt == "date":
        date = input("Введите дату в формате: dd.mm.yyyy: ")
        flag = True
        for i in array_notes:
            date_note = str(model.note.Note.get_date(i))
            if date == date_note[:10]:
                print(model.note.Note.map_Info(i))
                flag = False
        if flag:
            print("На данную дату заметок не найдено.")
    else:
        print("Журнал заметок пуст!")


def del_notes():
    id = input("Введите ID заметку, которую необходимо УДАЛИТЬ: ")
    array_notes = rF.read_file()
    flag = False

    for i in array_notes:
        if id == model.note.Note.get_id(i):
            array_notes.remove(i)


def change_note():
    id = input("Введите ID заметки для внесения изменений: ")
    array_notes = rF.read_file()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == model.note.Note.get_id(i):
            i.title = input("Измените Заголовок: \n")
            i.body = input("Измените Описание: \n")
            model.note.Note.set_date(i)
            flag = False
        array_notes_new.append(i)

    if flag:
        sF.save_file(array_notes_new, 'a')
        print("Заметка с id: ", id, " изменена.")
    else:
        print("id не найден!")
