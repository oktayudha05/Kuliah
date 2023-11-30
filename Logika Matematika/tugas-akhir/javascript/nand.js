//! logic nand
true1nand = document.querySelector('#true1nand')
true2nand = document.querySelector('#true2nand')
false1nand = document.querySelector('#false1nand')
false2nand = document.querySelector('#false2nand')
outputNand = document.querySelector('#outputNand')
kirimNand = document.querySelector('#kirimNand')

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
})
