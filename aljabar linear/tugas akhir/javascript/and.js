const ordoBaris = document.querySelector('#ordoBaris');
const ordoKolom = document.querySelector('#ordoKolom');
const setOrdo = document.querySelector('#setOrdo');

setOrdo.addEventListener('click', function(e) {
    e.preventDefault();

    if (ordoBaris.value === '' || ordoKolom.value === '') {
        alert('Ordo baris dan kolom tidak boleh kosong!');
        return;
    } else if (ordoBaris.value > 5 || ordoKolom.value > 5) {
        alert('Jangan banyak banyak ya, maksimal 5 baris dan kolom!');
        ordoBaris.value = '';
        ordoKolom.value = '';
        return;
     } 
    buatTable(ordoBaris.value, ordoKolom.value);
});

const buatTable = (baris, kolom) => {
    const tableMatrixA = document.querySelector('#tableMatrixA');
    const tableMatrixB = document.querySelector('#tableMatrixB');
    const output = document.querySelector('#output');

    //! Matrix A
    tableMatrixA.innerHTML = '';
    const judulMatrixA = document.createElement('h2');
    judulMatrixA.setAttribute('class', 'fw-bold text-success text-center');
    judulMatrixA.innerHTML = 'Matrix A';
    tableMatrixA.appendChild(judulMatrixA);
    for (let i = 0; i < baris; i++) {
        const tr = document.createElement('tr');
        for (let j = 0; j < kolom; j++) {
            const td = document.createElement('td');
            const input = document.createElement('input');
            input.setAttribute('type', 'text');
            input.setAttribute('class', 'form-control');
            input.setAttribute('id', `datA${i}${j}`);
            td.appendChild(input);
            tr.appendChild(td);
        }
        tableMatrixA.appendChild(tr);
    }
    //! Matrix B
    tableMatrixB.innerHTML = '';
    const judulMatrixB = document.createElement('h2');
    judulMatrixB.setAttribute('class', 'fw-bold text-success text-center');
    judulMatrixB.innerHTML = 'Matrix B';
    tableMatrixB.appendChild(judulMatrixB);
    for (let i = 0; i < baris; i++) {
        const tr = document.createElement('tr');
        for (let j = 0; j < kolom; j++) {
            const td = document.createElement('td');
            const input = document.createElement('input');
            input.setAttribute('type', 'text');
            input.setAttribute('class', 'form-control');
            input.setAttribute('id', `datB${i}${j}`);
            td.appendChild(input);
            tr.appendChild(td);
        }
        tableMatrixB.appendChild(tr);
    }

    //! Tambah
    const tambah = document.querySelector('#tambah');
    tambah.addEventListener('click', function(e) {
        e.preventDefault();
        temp = [];
        for (let i = 0; i < baris; i++) {
            tempBaris = [];
            for (let j = 0; j < kolom; j++) {
                const datA = parseInt(document.querySelector(`#datA${i}${j}`).value);
                const datB = parseInt(document.querySelector(`#datB${i}${j}`).value);
                const hasil = datA + datB;
                tempBaris.push(hasil);
            }
            temp.push(tempBaris);
        }
        console.log(temp);
        hasilOutput(temp);
    });

    //! Kurang
    const kurang = document.querySelector('#kurang');
    kurang.addEventListener('click', function(e) {
        e.preventDefault();
        temp = [];
        for (let i = 0; i < baris; i++) {
            tempBaris = [];
            for (let j = 0; j < kolom; j++) {
                const datA = parseInt(document.querySelector(`#datA${i}${j}`).value);
                const datB = parseInt(document.querySelector(`#datB${i}${j}`).value);
                const hasil = datA - datB;
                tempBaris.push(hasil);
            }
            temp.push(tempBaris);
        }
        console.log(temp);
        hasilOutput(temp);
    });

    //! Kali
    const kali = document.querySelector('#kali');
    kali.addEventListener('click', function(e) {
        e.preventDefault();
        temp = [];
        for (let i = 0; i < baris; i++) {
            tempBaris = [];
            for (let j = 0; j < kolom; j++) {
                let hasil = 0;
                for (let k = 0; k < kolom; k++) {
                    const datA = parseInt(document.querySelector(`#datA${i}${k}`).value);
                    const datB = parseInt(document.querySelector(`#datB${k}${j}`).value);
                    hasil += datA * datB;
                }
                tempBaris.push(hasil);
            }
            temp.push(tempBaris);
        } 

        hasilOutput(temp);
    });

    //! Output
    const hasilOutput = (hasil) => {
        output.innerHTML = '';
        for (let i = 0; i < baris; i++) {
            const tr = document.createElement('tr');
            for (let j = 0; j < kolom; j++) {
                const td = document.createElement('td');
                const isi = document.createElement('div');
                const p = document.createElement('p');
                p.innerHTML = hasil[i][j];
                isi.appendChild(p);
                td.appendChild(isi);
                tr.appendChild(td);
            }
            output.appendChild(tr);
        }
    }
}

