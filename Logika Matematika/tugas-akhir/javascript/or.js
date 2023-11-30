//! logic or
const true1or = document.querySelector('#true1or');
const false1or = document.querySelector('#false1or');
const true2or = document.querySelector('#true2or');
const false2or = document.querySelector('#false2or');
const kirimOr = document.querySelector('#kirimOr');
const outputOr = document.querySelector('#outputOr');

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
});