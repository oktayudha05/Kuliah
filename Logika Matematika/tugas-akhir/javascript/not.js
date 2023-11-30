//! logic not
const trueNot = document.querySelector('#trueNot');
const falseNot = document.querySelector('#falseNot');
const kirimNot = document.querySelector('#kirimNot');
const outputNot = document.querySelector('#outputNot');

trueNot.addEventListener('click', () => {
    falseNot.classList.remove('active');
    trueNot.classList.toggle('active');
    return inputNot = true
});
falseNot.addEventListener('click', () => {
    trueNot.classList.remove('active');
    falseNot.classList.toggle('active');
    return inputNot = false
});

kirimNot.addEventListener('click', () => {
    if (inputNot == true) {
        outputNot.innerHTML = 'Hasil dari <strong>NOT ' + inputNot + '</strong> adalah ' + '<strong>False</strong>'
    } else {
        outputNot.innerHTML = 'Hasil dari <strong>NOT ' + inputNot + '</strong> adalah ' + '<strong>True</strong>'
    }
});
