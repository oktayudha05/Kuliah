//! logic or
const true1or = document.querySelector('#true1or');
const false1or = document.querySelector('#false1or');
const true2or = document.querySelector('#true2or');
const false2or = document.querySelector('#false2or');
const kirimOr = document.querySelector('#kirimOr');
const outputOr = document.querySelector('#outputOr');
const baris1 = document.querySelector('#baris1');
const baris2 = document.querySelector('#baris2');
const baris3 = document.querySelector('#baris3');
const baris4 = document.querySelector('#baris4');


true1or.addEventListener('click', () => {
    false1or.classList.remove('active');
    true1or.classList.toggle('active');
    return input1or = true
});
false1or.addEventListener('click', () => {
    true1or.classList.remove('active');
    false1or.classList.toggle('active');
    return input1or = false
});

true2or.addEventListener('click', () => {
    false2or.classList.remove('active');
    true2or.classList.toggle('active');
    return input2or = true
});
false2or.addEventListener('click', () => {
    true2or.classList.remove('active');
    false2or.classList.toggle('active');
    return input2or = false
});

kirimOr.addEventListener('click', () => {
    if (input1or || input2or == true) {
        outputOr.innerHTML = 'Hasil dari <strong>' + input1or + '</strong> OR <strong>' + input2or + '</strong> adalah ' + '<strong>True</strong>'
    } else {
        outputOr.innerHTML = 'Hasil dari <strong>' + input1or + '</strong> OR <strong>' + input2or + '</strong> adalah ' + '<strong>False</strong>'
    }

    if (input1or == true && input2or == true) {
        baris1.classList.add('table-success');

        baris2.classList.remove('table-success');
        baris3.classList.remove('table-success');
        baris4.classList.remove('table-success');
    } else if (input1or == false && input2or == false) {
        baris4.classList.add('table-success');

        baris1.classList.remove('table-success');
        baris2.classList.remove('table-success');
        baris3.classList.remove('table-success');
    } else if (input1or == true && input2or == false) {
        baris2.classList.add('table-success');

        baris1.classList.remove('table-success');
        baris3.classList.remove('table-success');
        baris4.classList.remove('table-success');
    } else if (input1or == false && input2or == true) {
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