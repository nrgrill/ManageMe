function deleteNote(noteId) {
  fetch("/delete-task", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function calendar() {
    window.location.href = "/calendar";
};
