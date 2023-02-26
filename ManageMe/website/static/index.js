function deleteNote(noteId) {
  fetch("/delete-task", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/home";
  });
}

function calendar() {
    window.location.href = "/calendar";
};
