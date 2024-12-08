// Please see documentation at https://learn.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your JavaScript code.

function changePhase(newPhase, currentPage) {
    selectedPhase = newPhase + 1;
    console.log(currentPage + '/?selectedPhase=' + selectedPhase);
    window.location.href = currentPage + '/?selectedPhase=' + selectedPhase;
}

function rowClicked(rowNumber, selectedPhase) {
    window.location.href = '/OpenTournament?row=' + rowNumber + '&selectedPhase=' + selectedPhase;
}