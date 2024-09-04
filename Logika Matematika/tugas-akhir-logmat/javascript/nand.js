//! logic nand
const true1nand = document.querySelector('#true1nand')
const true2nand = document.querySelector('#true2nand')
const false1nand = document.querySelector('#false1nand')
const false2nand = document.querySelector('#false2nand')
const outputNand = document.querySelector('#outputNand')
const kirimNand = document.querySelector('#kirimNand')
const baris1 = document.querySelector('#baris1');
const baris2 = document.querySelector('#baris2');
const baris3 = document.querySelector('#baris3');
const baris4 = document.querySelector('#baris4');

true1nand.addEventListener('click', () => {
    false1nand.classList.remove('active')
    true1nand.classList.toggle('active')
    return input1nand = true
})
false1nand.addEventListener('click', () => {
    true1nand.classList.remove('active')
    false1nand.classList.toggle('active')
    return input1nand = false
})

true2nand.addEventListener('click', () => {
    false2nand.classList.remove('active')
    true2nand.classList.toggle('active')
    return input2nand = true
})
false2nand.addEventListener('click', () => {
    true2nand.classList.remove('active')
    false2nand.classList.toggle('active')
    return input2nand = false
})

kirimNand.addEventListener('click', () => {
    if (input1nand && input2nand == true) {
        outputNand.innerHTML = 'Hasil dari <strong>' + input1nand + '</strong> NAND <strong>' + input2nand + '</strong> adalah ' + '<strong>False</strong>'
    } else {
        outputNand.innerHTML = 'Hasil dari <strong>' + input1nand + '</strong> NAND <strong>' + input2nand + '</strong> adalah ' + '<strong>True</strong>'
    }

    if (input1nand == true && input2nand == true) {
        baris1.classList.add('table-success');

        baris2.classList.remove('table-success');
        baris3.classList.remove('table-success');
        baris4.classList.remove('table-success');
    } else if (input1nand == false && input2nand == false) {
        baris4.classList.add('table-success');

        baris1.classList.remove('table-success');
        baris2.classList.remove('table-success');
        baris3.classList.remove('table-success');
    } else if (input1nand == true && input2nand == false) {
        baris2.classList.add('table-success');

        baris1.classList.remove('table-success');
        baris3.classList.remove('table-success');
        baris4.classList.remove('table-success');
    } else if (input1nand == false && input2nand == true) {
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
})
