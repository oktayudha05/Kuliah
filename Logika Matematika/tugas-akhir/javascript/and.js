//! logic and
const true1and = document.querySelector('#true1and');
const false1and = document.querySelector('#false1and');
const true2and = document.querySelector('#true2and');
const false2and = document.querySelector('#false2and');
const kirimAnd = document.querySelector('#kirimAnd');
const outputAnd = document.querySelector('#outputAnd');

true1and.addEventListener('click', () => {
    false1and.classList.remove('active');
    true1and.classList.toggle('active');
    return input1and = true
});
false1and.addEventListener('click', () => {
    true1and.classList.remove('active');
    false1and.classList.toggle('active');
    return input1and = false
});

true2and.addEventListener('click', () => {
    false2and.classList.remove('active');
    true2and.classList.toggle('active');
    return input2and = true
});
false2and.addEventListener('click', () => {
    true2and.classList.remove('active');
    false2and.classList.toggle('active');
    return input2and = false
});

kirimAnd.addEventListener('click', () => {
    if (input1and && input2and == true) {
        outputAnd.innerHTML = 'Hasil dari <strong>' + input1and + '</strong> AND <strong>' + input2and + '</strong> adalah ' + '<strong>True</strong>'
    } else {
        outputAnd.innerHTML = 'Hasil dari <strong>' + input1and + '</strong> AND <strong>' + input2and + '</strong> adalah ' + '<strong>False</strong>'
    }
});





// and.addEventListener('DOMContentLoaded', () => programAnd());
// or.addEventListener('DOMContentLoaded', () => programOr());
