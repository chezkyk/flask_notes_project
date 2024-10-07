from flask import Blueprint, jsonify, request
from services.note import create_note, get_all_notes, get_note_by_id, update_note_by_id, delete_note_by_id,delete_all_notes

note_bp = Blueprint('notes', __name__, url_prefix='/api/notes')


@note_bp.route('', methods=['POST'])
def post_note():
    data = request.json
    title = data.get('title')
    content = data.get('content')
    urgency = data.get('urgency')
    date = data.get('date')

    if not title or not content:
        return jsonify({'error': 'Title and content are required'}), 400

    note_id = create_note(title, content, urgency, date)
    return jsonify({'message': 'Note created', 'id': str(note_id)}), 201


@note_bp.route('', methods=['GET'])
def get_notes():
    notes = get_all_notes()
    notes = [{**note, '_id': str(note['_id'])} for note in notes]  # Convert ObjectId to string
    return jsonify(notes), 200


@note_bp.route('/<string:id>', methods=['GET'])
def get_single_note(id):
    note = get_note_by_id(id)
    if not note:
        return jsonify({'error': 'Note not found'}), 404
    note['_id'] = str(note['_id'])  # Convert ObjectId to string
    return jsonify(note), 200


@note_bp.route('/<string:id>', methods=['PUT'])
def update_note(id):
    data = request.json
    title = data.get('title')
    content = data.get('content')
    urgency = data.get('urgency')
    date = data.get('date')

    updated = update_note_by_id(id, title=title, content=content, urgency=urgency, date=date)
    if updated:
        return jsonify({'message': 'Note updated'}), 200
    else:
        return jsonify({'error': 'Note not found or not updated'}), 404


@note_bp.route('/<string:id>', methods=['DELETE'])
def delete_note(id):
    deleted = delete_note_by_id(id)
    if deleted:
        return jsonify({'message': 'Note deleted'}), 200
    else:
        return jsonify({'error': 'Note not found'}), 404


@note_bp.route('/', methods=['DELETE'])
def delete_notes():
    delete_all_notes()
    return jsonify({'message': 'All notes deleted'}), 200



