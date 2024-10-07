from bson import ObjectId

from db import get_db_connection
from models.note import Note

def create_note(title, content, urgency,date):
    db_connection = get_db_connection()
    note = Note(title=title, content=content, urgency=urgency, date=date)
    result = db_connection.insert_one(note.to_dict())
    return result.inserted_id

def get_all_notes():
    db_connection = get_db_connection()
    return list(db_connection.find())

def get_note_by_id(id):
    db_connection = get_db_connection()
    return db_connection.find_one({'_id': ObjectId(id)})

def update_note_by_id(id, title=None, content=None, urgency=None, date=None):
    db_connection = get_db_connection()
    update_data = {}
    if title is not None:
        update_data['title'] = title
    if content is not None:
        update_data['content'] = content
    if urgency is not None:
        update_data['urgency'] = urgency
    if date is not None:
        update_data['date'] = date

    result = db_connection.update_one(
        {'_id': ObjectId(id)},
        {'$set': update_data}
    )
    return result.modified_count > 0


def delete_note_by_id(id):
    db_connection = get_db_connection()
    db_connection.delete_one({'_id': ObjectId(id)})
    return True

def delete_all_notes():
    db_connection = get_db_connection()
    db_connection.delete_many({})
    return True
