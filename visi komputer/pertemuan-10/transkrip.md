# Transkrip Video — Deep Learning & CNN

Total ± 1680 kata → ± 14–16 menit kalau dibaca pelan (100–115 kata/menit).

## Slide 1 — Judul

Assalamualaikum warahmatullahi wabarakatuh. Perkenalkan, nama saya Oktario Mufti Yudha dengan NPM 2320506044. Pada video ini saya akan mempresentasikan tugas Visi Komputer pertemuan kesepuluh. Topiknya ada dua, yaitu deep learning, yang mencakup cara kerja, jenis layer, activation function, dan optimizer, lalu dilanjutkan dengan cara kerja dan prinsip kerja CNN.

## Slide 2 — Materi

Supaya mudah diikuti, materinya saya bagi menjadi dua bagian. Di bagian pertama, kita mulai dari pengertian deep learning dan neuron buatan, lalu melihat bagaimana jaringan belajar, serta peran activation function dan optimizer. Setelah dasarnya paham, di bagian kedua kita masuk ke CNN, mulai dari cara komputer membaca gambar sampai langkah-langkah CNN mengenali gambar.

## Slide 3 — Bagian 1: Deep Learning

Baik, kita mulai dari bagian pertama, yaitu deep learning.

## Slide 4 — AI, Machine Learning, dan Deep Learning

Sebelum masuk ke cara kerjanya, kita lihat dulu posisi deep learning di antara istilah lain. Kotak paling luar adalah AI, yaitu bidang yang membuat mesin bisa bertindak cerdas. Di dalamnya ada machine learning, di mana mesin tidak diberi aturan satu per satu, tetapi belajar sendiri dari data. Lalu di dalam machine learning ada deep learning, yang memakai jaringan saraf tiruan dengan banyak lapisan, sehingga disebut deep.

## Slide 5 — Neuron Buatan

Lalu, jaringan saraf tiruan itu tersusun dari neuron buatan seperti di slide ini. Neuron menerima beberapa input, dan setiap input punya bobot yang menunjukkan seberapa penting input tersebut. Pertama, setiap input dikalikan dengan bobotnya, lalu semuanya dijumlahkan dan ditambah bias, dan hasilnya kita sebut z. Setelah itu, z dimasukkan ke activation function sehingga keluar output y. Pada contoh di bawah, nilai z-nya 0,3. Nah, bobot dan bias inilah yang nantinya dipelajari oleh deep learning.

## Slide 6 — Tipe Layer Berdasarkan Posisi

Karena satu neuron kemampuannya terbatas, neuron-neuron disusun berlapis menjadi jaringan. Berdasarkan posisinya, ada tiga tipe layer. Input layer adalah tempat data masuk, misalnya nilai piksel gambar. Data itu lalu diolah di hidden layer, tempat pola dipelajari, sampai akhirnya output layer memberikan jawaban, misalnya kucing atau anjing. Semakin banyak hidden layer-nya, jaringannya semakin dalam, dan dari situlah nama deep learning berasal.

## Slide 7 — Cara Kerja Deep Learning (Proses Training)

Setelah jaringannya tersusun, bagaimana jaringan ini belajar? Prosesnya disebut training. Pertama, data dihitung lapis demi lapis sampai menghasilkan prediksi, yang disebut forward pass. Prediksi itu dibandingkan dengan jawaban yang benar, dan selisihnya disebut loss. Kesalahan itu lalu dihitung mundur untuk mengetahui pengaruh setiap bobot, yang disebut backpropagation, kemudian optimizer memperbarui bobot supaya loss mengecil. Siklus ini diulang, di mana satu putaran seluruh data disebut epoch, dan data diproses per kelompok kecil yang disebut batch.

## Slide 8 — Jenis Layer Berdasarkan Fungsi

Selain berdasarkan posisi, layer juga dibedakan berdasarkan fungsinya, seperti di tabel ini. Dense layer menghubungkan setiap neuron ke semua neuron sebelumnya, dan biasanya dipakai di akhir untuk menentukan kelas. Convolutional layer mendeteksi pola seperti tepi dan garis, lalu pooling memperkecil ukuran data, dan flatten mengubahnya menjadi satu baris. Ada juga dropout, yang mematikan sebagian neuron secara acak saat training supaya model tidak sekadar hafal data, serta recurrent layer untuk data berurutan seperti teks.

## Slide 9 — Activation Function: Kenapa Perlu?

Sekarang kita kembali ke huruf f di neuron tadi, yaitu activation function. Fungsi ini diperlukan karena tanpa aktivasi, jaringan hanya bisa menghasilkan garis lurus, berapa pun jumlah layernya. Padahal, seperti gambar di kanan, data nyata sering tidak bisa dipisahkan dengan garis lurus. Dengan activation function, jaringan bisa membentuk batas yang melengkung, sehingga mampu mempelajari pola yang rumit.

## Slide 10 — Activation Function: Sigmoid & Tanh

Activation function yang pertama adalah sigmoid, yang mengubah input menjadi nilai antara nol dan satu. Karena hasilnya bisa dibaca sebagai peluang, sigmoid cocok untuk output dua kelas. Tanh bentuknya mirip, tetapi rentangnya minus satu sampai satu. Masalahnya, kalau input terlalu besar atau terlalu kecil, grafik keduanya menjadi datar, sehingga bobot sangat lambat berubah. Masalah ini disebut vanishing gradient.

## Slide 11 — Activation Function: ReLU & Leaky ReLU

Untuk mengatasi masalah itu, sekarang lebih banyak dipakai ReLU. Aturannya sederhana: input negatif menjadi nol, sedangkan input positif tetap. Karena ringan dihitung, ReLU menjadi standar untuk hidden layer, termasuk di CNN. Tetapi neuron yang terus menerima input negatif bisa berhenti belajar, jadi muncullah Leaky ReLU, yang mengalikan input negatif dengan angka kecil seperti 0,01, sehingga neuron tetap bisa belajar.

## Slide 12 — Activation Function: Softmax

Selanjutnya softmax, yang dipakai di output ketika kelasnya lebih dari dua. Softmax mengubah skor mentah menjadi peluang yang totalnya seratus persen. Pada contoh ini, skor kucing, anjing, dan burung berubah menjadi 66, 24, dan 10 persen. Karena peluang terbesarnya kucing, maka prediksinya adalah kucing.

## Slide 13 — Ringkasan: Activation Function

Jadi ringkasnya, hidden layer biasanya memakai ReLU. Untuk output dua kelas kita pakai sigmoid, untuk banyak kelas kita pakai softmax, dan kalau outputnya berupa angka, seperti harga rumah, kita pakai linear atau tanpa aktivasi.

## Slide 14 — Optimizer: Gradient Descent

Tadi sudah disebut bahwa bobot diperbarui oleh optimizer. Grafik di kiri menunjukkan hubungan bobot dengan loss, dan tujuannya adalah mencari bobot di titik loss terendah. Caranya disebut gradient descent: kita hitung gradient, yaitu kemiringan grafik di posisi bobot sekarang, lalu bobot digeser ke arah yang menurun. Rumusnya, bobot baru sama dengan bobot lama dikurangi learning rate dikali gradient, dan karena diulang terus, titik birunya perlahan turun ke loss terendah.

## Slide 15 — Learning Rate

Learning rate di rumus tadi menentukan seberapa besar langkah perubahan bobot. Kalau terlalu kecil, training jadi lambat. Kalau pas, loss cepat turun ke titik terendah. Tetapi kalau terlalu besar, bobot melompat melewati titik terendah dan loss malah naik. Karena itu, nilai awal yang umum dipakai adalah 0,001.

## Slide 16 — Jenis-Jenis Optimizer

Gradient descent punya beberapa variasi, seperti di tabel ini. Batch gradient descent memperbarui bobot setelah melihat seluruh data, jadi akurat tetapi lambat, sedangkan SGD memperbarui setiap satu data, jadi cepat tetapi tidak stabil. Mini-batch berada di tengahnya dan paling umum dipakai. Momentum menambahkan pengaruh langkah sebelumnya, dan RMSprop mengatur learning rate otomatis per bobot. Adam menggabungkan keduanya, sehingga paling sering dipakai sebagai pilihan awal.

## Slide 17 — Bagian 2: Convolutional Neural Network (CNN)

Dengan begitu, dasar deep learning sudah kita bahas. Sekarang kita masuk ke bagian kedua, yaitu CNN, jenis deep learning yang khusus untuk mengolah gambar.

## Slide 18 — Gambar bagi Komputer = Tabel Angka

Sebelum masuk ke CNN, kita lihat dulu bagaimana komputer membaca gambar. Bagi komputer, gambar adalah tabel angka. Setiap kotak disebut piksel, dengan nilai 0 untuk hitam sampai 255 untuk putih, jadi gambar wajah di kiri sebenarnya adalah tabel angka di tengah. Untuk gambar berwarna, tabelnya ada tiga, yaitu merah, hijau, dan biru. Nah, tugas CNN adalah menemukan pola dari angka-angka ini.

## Slide 19 — Kenapa Gambar Butuh CNN?

Lalu kenapa gambar tidak langsung dimasukkan ke dense layer biasa? Masalah pertama, bobotnya terlalu banyak, karena gambar 224 kali 224 berwarna punya sekitar 150 ribu input, sehingga butuh sekitar 150 juta bobot untuk seribu neuron. Masalah kedua, gambar harus diratakan, sehingga informasi piksel mana yang berdekatan ikut hilang. CNN mengatasi keduanya, karena satu filter 3 kali 3 hanya butuh 27 bobot, dan gambarnya tetap dua dimensi.

## Slide 20 — Prinsip Kerja CNN

CNN bisa seefisien itu karena tiga prinsip. Yang pertama local connectivity, artinya setiap neuron hanya melihat area kecil gambar, sehingga menangkap pola lokal seperti tepi. Yang kedua weight sharing, artinya filter yang sama dipakai di seluruh gambar, jadi bobotnya sedikit dan pola bisa dikenali di posisi mana pun. Yang ketiga hierarki fitur, di mana layer awal mendeteksi garis, layer tengah mendeteksi bentuk, dan layer akhir mengenali objek.

## Slide 21 — Cara Kerja CNN: Alur Umum

Dari prinsip tadi, alur CNN secara umum terlihat di slide ini. Gambar masuk ke convolution dan ReLU, lalu diperkecil dengan pooling, dan pasangan ini bisa diulang. Bagian oranye ini disebut ekstraksi fitur. Setelah itu data di-flatten, diolah di fully connected layer, lalu softmax menentukan kelasnya, dan bagian hijau ini disebut klasifikasi. Sekarang kita bahas langkahnya satu per satu.

## Slide 22 — Langkah 1 — Konvolusi

Langkah pertama adalah konvolusi. Di sini ada input 5 kali 5 dan filter 3 kali 3. Filter diletakkan di pojok kiri atas, yaitu kotak oranye, lalu setiap angka dikalikan dengan angka filter di posisi yang sama dan semuanya dijumlahkan, sehingga hasilnya 4. Setelah itu filter digeser satu kotak dan dihitung lagi, sampai seluruh gambar selesai. Hasil akhirnya, tabel 3 kali 3 di kanan, disebut feature map.

## Slide 23 — Stride & Padding

Dari contoh tadi, ukuran gambar menyusut dari 5 kali 5 menjadi 3 kali 3, dan ini dipengaruhi stride dan padding. Stride adalah jumlah kotak setiap kali filter bergeser, jadi stride 2 membuat hasilnya lebih kecil. Padding adalah tambahan nilai nol di sekeliling gambar, seperti kotak abu-abu di kiri, supaya ukurannya tidak menyusut. Dengan rumus di slide, tanpa padding hasilnya 3 kali 3, sedangkan dengan padding satu ukurannya tetap 5 kali 5.

## Slide 24 — Filter & Feature Map

Tadi kita hanya memakai satu filter, padahal setiap filter mendeteksi pola yang berbeda, misalnya garis vertikal, garis horizontal, atau penajaman seperti di slide ini. Karena itu, satu convolutional layer biasanya punya banyak filter, misalnya 32 atau 64, dan setiap filter menghasilkan satu feature map. Yang penting, nilai filter ini tidak ditentukan manual, tetapi dipelajari sendiri oleh CNN saat training.

## Slide 25 — Langkah 2 — ReLU

Setelah feature map didapat, langkah kedua adalah ReLU. Semua nilai negatif diubah menjadi nol, sedangkan nilai positif tetap, jadi minus 2, minus 1, minus 3, dan minus 5 di contoh ini berubah menjadi nol. Dengan begitu, hanya bagian yang cocok dengan pola filter yang diteruskan ke layer berikutnya.

## Slide 26 — Langkah 3 — Pooling

Karena ukuran feature map masih besar, langkah ketiga adalah pooling. Yang paling umum adalah max pooling 2 kali 2. Feature map dibagi menjadi area 2 kali 2 sesuai warnanya, lalu dari setiap area diambil nilai terbesar, yaitu 6, 4, 7, dan 9, sehingga ukurannya turun menjadi 2 kali 2. Ada juga average pooling yang mengambil rata-ratanya. Dengan ukuran lebih kecil, komputasi jadi lebih cepat dan model lebih tahan terhadap pergeseran objek.

## Slide 27 — Langkah 4 — Flatten, Fully Connected, Output

Setelah fiturnya didapat, langkah terakhir adalah klasifikasi. Hasil pooling diratakan dengan flatten menjadi satu baris, karena fully connected layer hanya menerima input satu dimensi. Fully connected layer lalu mengolah fitur-fitur itu, dan softmax di output menghasilkan peluang setiap kelas. Di sini hasilnya 85 persen kucing, sehingga CNN memprediksi gambar tersebut adalah kucing.

## Slide 28 — Contoh Arsitektur CNN: Kucing vs Anjing

Kalau semua langkah tadi digabung, contohnya seperti tabel ini. Gambar 64 kali 64 kali 3 melewati dua kali konvolusi dan pooling, sehingga ukurannya mengecil menjadi 16 kali 16, tetapi jumlah feature map-nya bertambah menjadi 64. Hasilnya lalu di-flatten menjadi 16.384 nilai, diolah di dense 128 neuron, dan berakhir di dense 2 neuron dengan softmax. Jadi polanya, semakin dalam, ukuran gambar semakin kecil tetapi fiturnya semakin banyak.

## Slide 29 — Kesimpulan

Sebagai kesimpulan, deep learning adalah jaringan saraf berlapis yang belajar lewat forward pass, loss, backpropagation, dan pembaruan bobot. Layer-nya dibagi menurut posisi dan fungsi, activation function membuat jaringan bisa mempelajari pola rumit, dan optimizer seperti Adam memperbarui bobot supaya loss turun. Sementara itu, CNN bekerja dengan local connectivity, weight sharing, dan hierarki fitur, melalui alur konvolusi, ReLU, pooling, flatten, fully connected, hingga softmax.

## Slide 30 — Terima Kasih

Demikian presentasi dari saya mengenai deep learning dan CNN. Semoga bermanfaat, dan terima kasih sudah menonton. Wassalamualaikum warahmatullahi wabarakatuh.

