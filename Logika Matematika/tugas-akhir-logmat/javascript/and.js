//! logic and
const true1and = document.querySelector('#true1and');
const false1and = document.querySelector('#false1and');
const true2and = document.querySelector('#true2and');
const false2and = document.querySelector('#false2and');
const kirimAnd = document.querySelector('#kirimAnd');
const outputAnd = document.querySelector('#outputAnd');
const baris1 = document.querySelector('#baris1');
const baris2 = document.querySelector('#baris2');
const baris3 = document.querySelector('#baris3');
const baris4 = document.querySelector('#baris4');


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
    
    if (input1and == true && input2and == true) {
        baris1.classList.add('table-success');

        baris2.classList.remove('table-success');
        baris3.classList.remove('table-success');
        baris4.classList.remove('table-success');
    } else if (input1and == false && input2and == false) {
        baris4.classList.add('table-success');

        baris1.classList.remove('table-success');
        baris2.classList.remove('table-success');
        baris3.classList.remove('table-success');
    } else if (input1and == true && input2and == false) {
        baris2.classList.add('table-success');

        baris1.classList.remove('table-success');
        baris3.classList.remove('table-success');
        baris4.classList.remove('table-success');
    } else if (input1and == false && input2and == true) {
        baris3.classList.add('table-success');

        baris1.classList.remove('table-success');
        baris2.classList.remove('table-success');
        baris4.classList.remove('table-success');
    } else {
        baris1.classList.remove('table-success');
        baris2.classList.remove('table-success');
        baris3.classList.remove('table-success');
        baris4.classList.remove('table-success');
    }
});





// and.addEventListener('DOMContentLoaded', () => programAnd());
// or.addEventListener('DOMContentLoaded', () => programOr());
