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

    //! determinan
    const determinan = document.querySelector('#determinan');
    determinan.addEventListener('click', function(e) {
        e.preventDefault();
        if (baris !== kolom) {
            alert('Ordo baris dan kolom harus sama!');
            return;
        }
        if (baris == 2) {
            const a = parseInt(document.querySelector('#datA00').value);
            let b = parseInt(document.querySelector('#datA01').value);
            let c = parseInt(document.querySelector('#datA10').value);
            const d = parseInt(document.querySelector('#datA11').value);

            if (Math.sign(b) == 1) {
                b = b * -1;
            }  else if (Math.sign(b) == -1) {
                b = b * -1;
            }

            if (Math.sign(c) == 1) {
                c = c * -1;
            } else if (Math.sign(c) == -1) {
                c= c * -1;
            }

            const baris1 = [d, b]
            const baris2 = [c, a]
            const hasil = [baris1, baris2];
            hasilOutput(hasil);
        } else if (baris == 3) {
            const a = parseInt(document.querySelector('#datA00').value);
            const b = parseInt(document.querySelector('#datA01').value);
            const c = parseInt(document.querySelector('#datA02').value);
            const d = parseInt(document.querySelector('#datA10').value);
            const e = parseInt(document.querySelector('#datA11').value);
            const f = parseInt(document.querySelector('#datA12').value);
            const g = parseInt(document.querySelector('#datA20').value);
            const h = parseInt(document.querySelector('#datA21').value);
            const i = parseInt(document.querySelector('#datA22').value);
            
            const langkah1 = a * e * i;
            const langkah2 = b * f * g;
            const langkah3 = c * d * h;
            const langkah4 = c * e * g;
            const langkah5 = b * d * i;
            const langkah6 = a * f * h;

            const hasil = langkah1 + langkah2 + langkah3 - langkah4 - langkah5 - langkah6;
            const isi = document.createElement('div');
            const p = document.createElement('p');
            p.innerHTML = hasil;
            isi.appendChild(p);
            output.appendChild(isi);
        } else {
            alert('Ordo baris dan kolom harus 2 atau 3!');
        }
    });

    //! Output
    const hasilOutput = (hasil) => {
        output.innerHTML = '';
        for (let i = 0; i < baris; i++) {
            const tr = document.createElement('tr');
            for (let j = 0; j < kolom; j++) {
                const td = document.createElement('td');
                const isi = document.createElement('div');
                isi.setAttribute('class', 'text-center alert alert-success mb-0 border-0');
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

