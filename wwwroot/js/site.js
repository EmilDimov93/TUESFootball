function changePhase(newPhase, currentPage) {
    selectedPhase = newPhase;
    console.log(currentPage + '/?phase=' + selectedPhase);
    window.location.href = currentPage + '/?phase=' + selectedPhase;
}

function rowClicked(rowNumber, selectedPhase) {
    window.location.href = '/OpenTournament?row=' + rowNumber + '&phase=' + selectedPhase;
}