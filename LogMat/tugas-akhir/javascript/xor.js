//! logic xor
const true1xor = document.querySelector('#true1xor');
const false1xor = document.querySelector('#false1xor');
const true2xor = document.querySelector('#true2xor');
const false2xor = document.querySelector('#false2xor');
const kirimXor = document.querySelector('#kirimXor');
const outputXor = document.querySelector('#outputXor');
const baris1 = document.querySelector('#baris1');
const baris2 = document.querySelector('#baris2');
const baris3 = document.querySelector('#baris3');
const baris4 = document.querySelector('#baris4');


true1xor.addEventListener('click', () => {
    false1xor.classList.remove('active');
    true1xor.classList.toggle('active');
    return input1xor = true
});
false1xor.addEventListener('click', () => {
    true1xor.classList.remove('active');
    false1xor.classList.toggle('active');
    return input1xor = false
});

true2xor.addEventListener('click', () => {
    false2xor.classList.remove('active');
    true2xor.classList.toggle('active');
    return input2xor = true
});
false2xor.addEventListener('click', () => {
    true2xor.classList.remove('active');
    false2xor.classList.toggle('active');
    return input2xor = false
});

kirimXor.addEventListener('click', () => {
    if (input1xor == input2xor) {
        outputXor.innerHTML = 'Hasil dari <strong>' + input1xor + '</strong> XOR <strong>' + input2xor + '</strong> adalah ' + '<strong>True</strong>'
    } else {
        outputXor.innerHTML = 'Hasil dari <strong>' + input1xor + '</strong> XOR <strong>' + input2xor + '</strong> adalah ' + '<strong>False</strong>'
    }
    if (input1xor == true && input2xor == true) {
        baris1.classList.add('table-success');

        baris2.classList.remove('table-success');
        baris3.classList.remove('table-success');
        baris4.classList.remove('table-success');
    } else if (input1xor == false && input2xor == false) {
        baris4.classList.add('table-success');

        baris1.classList.remove('table-success');
        baris2.classList.remove('table-success');
        baris3.classList.remove('table-success');
    } else if (input1xor == true && input2xor == false) {
        baris2.classList.add('table-success');

        baris1.classList.remove('table-success');
        baris3.classList.remove('table-success');
        baris4.classList.remove('table-success');
    } else if (input1xor == false && input2xor == true) {
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