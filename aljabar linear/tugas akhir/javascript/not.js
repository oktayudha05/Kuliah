//! logic not
const trueNot = document.querySelector('#trueNot');
const falseNot = document.querySelector('#falseNot');
const kirimNot = document.querySelector('#kirimNot');
const outputNot = document.querySelector('#outputNot');
const baris1 = document.querySelector('#baris1');
const baris2 = document.querySelector('#baris2');

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

    if (inputNot == true) {
        baris1.classList.add('table-success');

        baris2.classList.remove('table-success');
    } else if (inputNot == false) {
        baris2.classList.add('table-success');

        baris1.classList.remove('table-success');
    }
});
