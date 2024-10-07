// Fetch all notes when the page loads
document.addEventListener('DOMContentLoaded', getNotes);

async function getNotes() {
    const response = await fetch('/api/notes', {
        method: 'GET',
    });
    const notes = await response.json();
    const notesList = document.getElementById('notes-list');
    notesList.innerHTML = ''; // Clear the current list

    notes.forEach(note => {
        const li = document.createElement('li');
        li.innerHTML = `
            <strong>${note.title}</strong>
            <p>${note.content}</p>
            <small>Urgency: ${note.urgency} | Date: ${note.date}</small>
            <button onclick="deleteNote('${note._id}')">Delete</button>
            <button onclick="toggleEdit('${note._id}')">Edit</button>
            <div id="edit-fields-${note._id}" class="edit-fields" style="display: none;">
                <input type="text" id="edit-title-${note._id}" value="${note.title}">
                <textarea id="edit-content-${note._id}">${note.content}</textarea>
                <input type="text" id="edit-urgency-${note._id}" value="${note.urgency}">
                <input type="date" id="edit-date-${note._id}" value="${note.date}">
                <button onclick="updateNote('${note._id}')">Update</button>
            </div>
        `;
        notesList.appendChild(li);
    });
}

// Function to toggle the visibility of the edit fields
function toggleEdit(id) {
    const editFields = document.getElementById(`edit-fields-${id}`);
    editFields.style.display = editFields.style.display === 'none' ? 'block' : 'none';
}

// Function to update note
async function updateNote(id) {
    const title = document.getElementById(`edit-title-${id}`).value;
    const content = document.getElementById(`edit-content-${id}`).value;
    const urgency = document.getElementById(`edit-urgency-${id}`).value;
    const date = document.getElementById(`edit-date-${id}`).value;

    const updatedNote = {
        title,
        content,
        urgency,
        date
    };

    const response = await fetch(`/api/notes/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedNote),
    });

    if (response.status === 200) {
        alert('Note updated successfully');
        getNotes();  // Refresh the notes list
    } else {
        alert('Error updating note');
    }
}

// Function to create a new note
async function createNote() {
    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;
    const urgency = document.getElementById('urgency').value;
    const date = document.getElementById('date').value;

    const note = {
        title,
        content,
        urgency,
        date
    };

    const response = await fetch('/api/notes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(note),
    });

    if (response.status === 201) {
        alert('Note created successfully');
        getNotes();  // Refresh the notes list
    } else {
        alert('Error creating note');
    }
}

// Function to delete a note
async function deleteNote(id) {
    const response = await fetch(`/api/notes/${id}`, {
        method: 'DELETE',
    });

    if (response.status === 200) {
        alert('Note deleted');
        getNotes();  // Refresh the notes list
    } else {
        alert('Error deleting note');
    }
}
// Event listener for the "Delete All" button
document.getElementById('delete-all-btn').addEventListener('click', deleteAllNotes);

// Function to delete all notes
async function deleteAllNotes() {
    const confirmDelete = confirm('Are you sure you want to delete all notes?');
    if (confirmDelete) {
        const response = await fetch('/api/notes/', {
            method: 'DELETE',
        });

        if (response.status === 200) {
            alert('All notes deleted successfully');
            getNotes();  // Refresh the notes list
        } else {
            alert('Error deleting all notes');
        }
    }
}
