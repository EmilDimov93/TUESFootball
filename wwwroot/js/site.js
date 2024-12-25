function changePhase(newPhase, currentPage) {
    selectedPhase = newPhase;
    console.log(currentPage + '/?p=' + selectedPhase);
    window.location.href = currentPage + '/?p=' + selectedPhase;
}

function rowClicked(rowNumber, selectedPhase) {
    window.location.href = '/OpenTournament?r=' + rowNumber + '&p=' + selectedPhase;
}