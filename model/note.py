from datetime import datetime
from view import counter
import uuid


class Note:
    def __init__(self, id=str(counter.counter()), title="text", body="text",
                 date=str(datetime.now().strftime("%dd.%mm.%yyyy %HH:%MM:%SS"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def set_id(note):
        note.id = str(counter.counter())

    def set_title(note):
        note.title = note

    def set_body(note):
        note.body = note

    def set_date(note):
        note.date = str(datetime.now().strftime("%dd.%mm.%yyyy %HH:%MM:%SS"))

    def get_id(note):
        return note.id

    def get_title(note):
        return note.title

    def get_body(note):
        return note.body

    def get_date(note):
        return note.date

    def get_Info(note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date

    def map_Info(note):
        return ("\nId: " + note.id + '\n' + "Название: " + note.title +
                '\n' + "Описание: " + note.body + "\n" + "Дата создания - " + note.date)