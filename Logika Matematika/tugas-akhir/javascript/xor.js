//! logic xor
const true1xor = document.querySelector('#true1xor');
const false1xor = document.querySelector('#false1xor');
const true2xor = document.querySelector('#true2xor');
const false2xor = document.querySelector('#false2xor');
const kirimXor = document.querySelector('#kirimXor');
const outputXor = document.querySelector('#outputXor');

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
});