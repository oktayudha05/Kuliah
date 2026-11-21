# Penjelasan Tugas Object Detection dengan YOLOv8

File notebook: `tugas_12.ipynb`

## 1. Tugasnya apa

Dari slide materi Object Detection ada tiga perintah:

1. Cari dataset object detection di Kaggle.
2. Lakukan object detection pakai metode apa saja.
3. Evaluasi hasilnya dengan menghitung mAP.

Yang gw kerjakan: ambil dataset rambu lalu lintas dari Kaggle, latih model YOLOv8 untuk mendeteksi rambu, lalu hitung mAP di data test.

## 2. Konsep dasar yang perlu dipahami dulu

### Klasifikasi vs deteksi objek

- **Klasifikasi gambar** cuma menjawab "ini gambar apa". Satu gambar dapat satu label, misalnya "kucing".
- **Deteksi objek** menjawab dua hal sekaligus: "ada objek apa saja" dan "di mana letaknya". Setiap objek dikasih kotak (disebut **bounding box**) plus label kelasnya. Satu gambar bisa berisi banyak objek, misalnya "kucing, anjing, anjing" [1].

### One-stage vs two-stage detector

Di slide dijelaskan ada dua jenis detektor [1]:

- **Two-stage**, contohnya Faster R-CNN. Tahap pertama mencari dulu area yang kemungkinan berisi objek (disebut *region proposal*). Tahap kedua mengklasifikasi dan merapikan kotak di area itu. Biasanya akurat, tapi lebih lambat.
- **One-stage**, contohnya YOLO dan SSD. Langsung memprediksi kotak dan kelas dalam satu kali proses, tanpa tahap region proposal. Hasilnya jauh lebih cepat.

### YOLO

YOLO singkatan dari *You Only Look Once*. Idenya: gambar cukup "dilihat" sekali oleh jaringan, lalu jaringan langsung mengeluarkan semua kotak dan kelasnya [2]. Di tugas ini gw pakai **YOLOv8n** dari library Ultralytics. Huruf "n" artinya *nano*, versi paling kecil dengan sekitar 3 juta parameter, jadi cepat dilatih [3].

### Transfer learning

YOLOv8n yang gw pakai sudah pernah dilatih sebelumnya di dataset **COCO**, yaitu dataset besar berisi 80 kelas benda sehari-hari [3][4]. Jadi model sudah "paham" bentuk, tepi, dan warna secara umum. Kita tinggal melatih ulang (*fine-tuning*) supaya model mengenali 15 kelas rambu. Di log training terlihat 349 dari 355 bagian bobot berhasil dipindahkan dari model COCO. Sisanya bagian kepala (*head*) yang harus disesuaikan, karena jumlah kelasnya beda (80 jadi 15).

## 3. Dataset

**Traffic Signs Detection** dari Kaggle [5]:

| Info | Nilai |
|---|---|
| Total gambar | 4969 |
| Train | 3530 gambar |
| Valid | 801 gambar |
| Test | 638 gambar |
| Jumlah kelas | 15 |

Kelasnya: Green Light, Red Light, Speed Limit 10 sampai 120, dan Stop.

Dataset ini sudah dalam **format YOLO**. Setiap gambar punya file `.txt` berisi label, satu baris untuk satu objek:

```
id_kelas  x_tengah  y_tengah  lebar  tinggi
```

Semua angka posisi dinormalisasi ke rentang 0 sampai 1, jadi tidak tergantung ukuran gambar. Contoh: `14 0.5 0.5 0.3 0.4` artinya objek kelas ke-14 (Stop), titik tengahnya di tengah gambar, lebarnya 30% dan tingginya 40% dari ukuran gambar.

## 4. Langkah-langkah di notebook

### Langkah 1: Install library
Install `ultralytics` (untuk YOLOv8) dan `kagglehub` (untuk download dataset dari Kaggle langsung di Colab).

### Langkah 2: Download dataset
`kagglehub.dataset_download("pkdarabi/cardetection")` mengunduh dataset. Setelah itu dicari file `data.yaml`, yaitu file konfigurasi yang berisi jumlah kelas dan nama-nama kelas.

### Langkah 3: Atur ulang path dataset
Path di `data.yaml` bawaan dataset belum sesuai dengan lokasi folder di Colab. Jadi gw tulis ulang supaya menunjuk ke folder `train/images`, `valid/images`, dan `test/images`. Kalau path-nya salah, YOLO tidak bisa menemukan gambarnya.

### Langkah 4: Training
```python
model = YOLO("yolov8n.pt")
model.train(data="data.yaml", epochs=20, imgsz=640, batch=16, seed=42)
```
- `yolov8n.pt` = bobot pretrained COCO.
- `epochs=20` = seluruh data train dilihat model sebanyak 20 putaran.
- `imgsz=640` = gambar diubah ukurannya jadi 640 piksel.
- `batch=16` = model belajar dari 16 gambar sekaligus per langkah.
- `seed=42` = supaya hasilnya bisa diulang.

Training jalan di GPU T4 Colab sekitar 17 menit. Selama training, YOLO menghitung tiga jenis loss (ukuran kesalahan model):
- **box_loss**: seberapa meleset posisi kotak.
- **cls_loss**: seberapa salah tebakan kelas.
- **dfl_loss**: kesalahan detail batas tepi kotak.

Ketiganya turun selama training, artinya model makin pintar. Grafiknya ada di notebook (`results.png`).

### Langkah 5: Evaluasi mAP di data test
Model terbaik (`best.pt`, yang skornya paling tinggi di data valid) diuji pakai **data test**. Data test belum pernah dilihat model sama sekali, jadi hasilnya jujur.

### Langkah 6: Contoh hasil deteksi
Enam gambar test diprediksi, lalu digambar kotak, label, dan tingkat keyakinannya (*confidence*). Contoh: `Speed Limit 30 0.93` artinya model yakin 93% itu rambu batas kecepatan 30.

## 5. Cara mengukur: IoU, Precision, Recall, AP, mAP

Bagian ini yang paling penting buat dipahami, karena tugasnya minta mAP.

### IoU (Intersection over Union)
IoU mengukur seberapa pas kotak prediksi menempel dengan kotak asli (*ground truth*) [6].

```
IoU = luas irisan kedua kotak / luas gabungan kedua kotak
```

- IoU = 1 → kotak prediksi persis sama dengan kotak asli.
- IoU = 0 → kotak sama sekali tidak bersentuhan.

Prediksi dianggap **benar (True Positive)** kalau kelasnya benar **dan** IoU-nya di atas batas tertentu, misalnya 0,5.

### Precision dan Recall
- **TP (True Positive)**: objek ada dan berhasil dideteksi dengan benar.
- **FP (False Positive)**: model bilang ada objek, padahal tidak ada atau salah kelas.
- **FN (False Negative)**: objek ada, tapi model tidak mendeteksinya.

```
Precision = TP / (TP + FP)   → dari semua tebakan model, berapa yang benar
Recall    = TP / (TP + FN)   → dari semua objek asli, berapa yang ketemu
```

Contoh: di gambar ada 10 rambu. Model menebak 8 kotak, 6 di antaranya benar.
Precision = 6/8 = 0,75. Recall = 6/10 = 0,6.

### AP (Average Precision)
Precision dan recall berubah tergantung batas confidence yang dipakai. Kalau semua nilai itu digambar, jadinya **kurva precision-recall**. **AP adalah luas area di bawah kurva itu**, dihitung untuk satu kelas [6]. Makin besar luasnya (maksimal 1), makin bagus. Artinya model bisa menemukan banyak objek (recall tinggi) sambil tetap jarang salah (precision tinggi).

### mAP (mean Average Precision)
mAP = **rata-rata AP dari semua kelas**. Karena ada 15 kelas, AP ke-15 kelas itu dijumlah lalu dibagi 15.

- **mAP50**: AP dihitung dengan batas IoU 0,5. Kotak dianggap benar kalau menempel minimal 50%. Ini versi yang "longgar".
- **mAP50-95**: AP dihitung di 10 batas IoU (0,50; 0,55; 0,60; … ; 0,95), lalu dirata-rata. Ini versi yang "ketat", karena kotak harus benar-benar pas supaya skornya tinggi. Metrik ini dipakai sebagai standar di COCO [4][6].

## 6. Hasil

### Hasil keseluruhan di data test (638 gambar, 770 objek)

| Metrik | Nilai |
|---|---|
| Precision | 0,8875 |
| Recall | 0,8902 |
| **mAP50** | **0,9389** |
| **mAP50-95** | **0,7934** |

### AP per kelas

| Kelas | AP50 | AP50-95 |
|---|---|---|
| Green Light | 0,9027 | 0,5320 |
| Red Light | 0,8011 | 0,4748 |
| Speed Limit 10 | 0,8630 | 0,6706 |
| Speed Limit 100 | 0,9869 | 0,8599 |
| Speed Limit 110 | 0,8889 | 0,7938 |
| Speed Limit 120 | 0,9692 | 0,8714 |
| Speed Limit 20 | 0,9730 | 0,8819 |
| Speed Limit 30 | 0,9453 | 0,8402 |
| Speed Limit 40 | 0,9895 | 0,8892 |
| Speed Limit 50 | 0,9112 | 0,8246 |
| Speed Limit 60 | 0,9396 | 0,8452 |
| Speed Limit 70 | 0,9634 | 0,8302 |
| Speed Limit 80 | 0,9863 | 0,8613 |
| Speed Limit 90 | 0,9682 | 0,8229 |
| Stop | 0,9950 | 0,9025 |

## 7. Analisis

1. **Model sudah bagus.** mAP50 sebesar 0,94 artinya pada batas IoU 50%, model hampir selalu menemukan rambu dengan kelas yang benar.
2. **mAP50-95 lebih rendah (0,79) itu wajar.** Syaratnya lebih ketat, kotak harus sangat pas. Selisih dengan mAP50 menunjukkan model sudah tahu letak objeknya, tapi batas kotaknya kadang belum presisi.
3. **Stop paling mudah dideteksi** (AP50 0,995). Bentuknya segi delapan dan warnanya merah polos, jadi beda jauh dari kelas lain.
4. **Red Light dan Green Light paling susah** (AP50-95 cuma 0,47 dan 0,53). Lampu lalu lintas ukurannya kecil di gambar, jadi meleset sedikit saja sudah menurunkan IoU banyak. Bentuk lampu merah dan hijau juga mirip, yang membedakan cuma warna.
5. **Speed Limit 10 nilainya kurang bisa dipercaya.** Di data test kelas ini cuma ada 3 objek, terlalu sedikit untuk diambil kesimpulan.
6. **Kecepatan:** inferensi sekitar 4 ms per gambar di GPU T4. Ini menunjukkan kelebihan detektor one-stage: cukup cepat untuk video real-time.

## 8. Kemungkinan pertanyaan kalau presentasi

**Kenapa pakai YOLO, bukan Faster R-CNN?**
YOLO itu one-stage, jadi lebih cepat dilatih dan dipakai. Library Ultralytics juga sudah langsung menghitung mAP. Untuk dataset rambu yang objeknya jelas, akurasinya sudah tinggi.

**Bedanya data valid dan data test apa?**
Data valid dipakai selama training untuk memilih model terbaik (`best.pt`). Data test baru dipakai di akhir, jadi hasil evaluasinya tidak bias.

**Kenapa mAP50-95 lebih kecil dari mAP50?**
Karena mAP50-95 juga menghitung batas IoU yang ketat sampai 95%. Makin ketat batasnya, makin sedikit prediksi yang dianggap benar.

**Gimana cara naikin hasilnya?**
Tambah epoch, pakai model yang lebih besar (YOLOv8s atau YOLOv8m), atau tambah data untuk kelas yang sedikit seperti Speed Limit 10 dan lampu lalu lintas.

## Sumber

1. A. R. Prananda, *Computer Vision – Pertemuan 11: Object Detection*, slide kuliah, Universitas Tidar.
2. J. Redmon, S. Divvala, R. Girshick, A. Farhadi, "You Only Look Once: Unified, Real-Time Object Detection," CVPR 2016. https://arxiv.org/abs/1506.02640
3. Ultralytics, "YOLOv8 Documentation." https://docs.ultralytics.com/models/yolov8/
4. T.-Y. Lin dkk., "Microsoft COCO: Common Objects in Context," ECCV 2014. https://arxiv.org/abs/1405.0312
5. pkdarabi, "Traffic Signs Detection," Kaggle Dataset. https://www.kaggle.com/datasets/pkdarabi/cardetection
6. Ultralytics, "Performance Metrics Deep Dive." https://docs.ultralytics.com/guides/yolo-performance-metrics/
