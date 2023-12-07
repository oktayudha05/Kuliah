//! logic nor
const true1nor = document.querySelector('#true1nor');
const false1nor = document.querySelector('#false1nor');
const true2nor = document.querySelector('#true2nor');
const false2nor = document.querySelector('#false2nor');
const kirimNor = document.querySelector('#kirimNor');
const outputNor = document.querySelector('#outputNor');
const baris1 = document.querySelector('#baris1');
const baris2 = document.querySelector('#baris2');
const baris3 = document.querySelector('#baris3');
const baris4 = document.querySelector('#baris4');

true1nor.addEventListener('click', () => {
    false1nor.classList.remove('active');
    true1nor.classList.toggle('active');
    return input1nor = true
});
false1nor.addEventListener('click', () => {
    true1nor.classList.remove('active');
    false1nor.classList.toggle('active');
    return input1nor = false
});

true2nor.addEventListener('click', () => {
    false2nor.classList.remove('active');
    true2nor.classList.toggle('active');
    return input2nor = true
});
false2nor.addEventListener('click', () => {
    true2nor.classList.remove('active');
    false2nor.classList.toggle('active');
    return input2nor = false
});

kirimNor.addEventListener('click', () => {
    if (input1nor || input2nor == true) {
        outputNor.innerHTML = 'Hasil dari <strong>' + input1nor + '</strong> NOR <strong>' + input2nor + '</strong> adalah ' + '<strong>False</strong>'
    } else {
        outputNor.innerHTML = 'Hasil dari <strong>' + input1nor + '</strong> NOR <strong>' + input2nor + '</strong> adalah ' + '<strong>True</strong>'
    }

    if (input1nor == true && input2nor == true) {
        baris1.classList.add('table-success');

        baris2.classList.remove('table-success');
        baris3.classList.remove('table-success');
        baris4.classList.remove('table-success');
    } else if (input1nor == false && input2nor == false) {
        baris4.classList.add('table-success');

        baris1.classList.remove('table-success');
        baris2.classList.remove('table-success');
        baris3.classList.remove('table-success');
    } else if (input1nor == true && input2nor == false) {
        baris2.classList.add('table-success');

        baris1.classList.remove('table-success');
        baris3.classList.remove('table-success');
        baris4.classList.remove('table-success');
    } else if (input1nor == false && input2nor == true) {
        baris3.classList.add('table-success');

        baris1.classList.remove('table-success');
        baris2.classList.remove('table-success');
        baris4.classList.remove('table-success');
    }
});

