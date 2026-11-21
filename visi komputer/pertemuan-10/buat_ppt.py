# Generator PPT + transkrip tugas pertemuan 10 (Deep Learning & CNN).
# Jalankan: ../.venv/bin/python buat_ppt.py  -> presentasi.pptx + transkrip.md
import io

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

NAMA, NPM = "Oktario Mufti Yudha", "2320506044"

C = lambda h: RGBColor.from_string(h)
NAVY, ORANGE, BLUE, GREEN, RED, LIGHT, GRAY, WHITE = map(
    C, "1F2A44 F28C28 3A7BD5 2E9E6A D64545 EEF2F8 5A6275 FFFFFF".split())
SOFT_BLUE, SOFT_ORANGE, SOFT_GREEN, SOFT_RED, SOFT_GRAY = map(C, "CFE2FF FFE0C2 CFF0DC F9D0D9 D9DDE3".split())
FONT = "Calibri"

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
transkrip = []


# ---------- helper gambar ----------
def runs(p, s, size, color=NAVY, bold=False, font=FONT):
    # **teks** = tebal
    for i, part in enumerate(s.split("**")):
        if part:
            r = p.add_run()
            r.text = part
            f = r.font
            f.size, f.name, f.bold = Pt(size), font, bold or i % 2 == 1
            f.color.rgb = color


def text(s, x, y, w, h, lines, size=22, color=NAVY, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
         shape=None, fill=None, line=None, bold=False, font=FONT, spacing=6):
    if shape is None:
        sh = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    else:
        sh = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
        sh.shadow.inherit = False
        if fill:
            sh.fill.solid()
            sh.fill.fore_color.rgb = fill
        else:
            sh.fill.background()
        if line:
            sh.line.color.rgb = line
            sh.line.width = Pt(1.25)
        else:
            sh.line.fill.background()
    tf = sh.text_frame
    tf.word_wrap, tf.vertical_anchor = True, anchor
    tf.margin_left = tf.margin_right = Inches(0.08)
    tf.margin_top = tf.margin_bottom = Inches(0.04)
    for i, ln in enumerate([lines] if isinstance(lines, str) else lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(spacing)
        runs(p, ln, size, color, bold, font)
    return sh


def box(s, x, y, w, h, t, fill=BLUE, color=WHITE, size=18, bold=True,
        shape=MSO_SHAPE.ROUNDED_RECTANGLE, line=None):
    return text(s, x, y, w, h, t, size, color, PP_ALIGN.CENTER, MSO_ANCHOR.MIDDLE, shape, fill, line, bold, spacing=2)


def card(s, x, y, w, h, lines, fill=LIGHT, line=BLUE, size=18):
    return text(s, x, y, w, h, lines, size, NAVY, shape=MSO_SHAPE.ROUNDED_RECTANGLE, fill=fill, line=line)


def bullets(s, items, x=0.7, y=1.45, w=12, h=5.6, size=24):
    # item diawali ">" = sub-poin
    lines = ["      –  " + it[1:] if it.startswith(">") else "•  " + it for it in items]
    return text(s, x, y, w, h, lines, size, spacing=10)


def panah(s, x, y, w=0.55, h=0.45, color=GRAY, shape=MSO_SHAPE.RIGHT_ARROW):
    a = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    a.fill.solid()
    a.fill.fore_color.rgb = color
    a.line.fill.background()
    a.shadow.inherit = False


def garis(s, x1, y1, x2, y2, color=GRAY, width=1.25):
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = color
    c.line.width = Pt(width)


def matrix(s, M, x, y, c=0.55, hl=None, size=16, fill=WHITE):
    hl = hl or {}
    for r, row in enumerate(M):
        for k, v in enumerate(row):
            box(s, x + k * c, y + r * c, c, c, str(v), hl.get((r, k), fill), NAVY, size, False,
                MSO_SHAPE.RECTANGLE, GRAY)


def window(r0, k0, n=3, color=SOFT_ORANGE):
    return {(r, k): color for r in range(r0, r0 + n) for k in range(k0, k0 + n)}


def gambar(s, fig, x, y, w):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=160, bbox_inches="tight", transparent=True)
    plt.close(fig)
    buf.seek(0)
    s.shapes.add_picture(buf, Inches(x), Inches(y), width=Inches(w))


def nn(s, sizes, x0, y0, w, h, colors, labels=(), texts=None, d=0.55):
    xs = [x0 + i * w / (len(sizes) - 1) for i in range(len(sizes))]
    pos = []
    for n in sizes:
        gap = min(1.0, h / n)
        pos.append([y0 + h / 2 + (j - (n - 1) / 2) * gap for j in range(n)])
    for i in range(len(sizes) - 1):
        for ya in pos[i]:
            for yb in pos[i + 1]:
                garis(s, xs[i], ya, xs[i + 1], yb, SOFT_GRAY, 1)
    for i, ys in enumerate(pos):
        for j, yy in enumerate(ys):
            t = texts[i][j] if texts and texts[i] else ""
            box(s, xs[i] - d / 2, yy - d / 2, d, d, t, colors[i], WHITE, 14, True, MSO_SHAPE.OVAL)
    for i, lb in enumerate(labels):
        text(s, xs[i] - 1, y0 + h + 0.15, 2, 0.8, lb, 16, NAVY, PP_ALIGN.CENTER, bold=True)


def table(s, rows, x, y, col_w, size=16, row_h=0.55):
    t = s.shapes.add_table(len(rows), len(rows[0]), Inches(x), Inches(y),
                           Inches(sum(col_w)), Inches(row_h * len(rows))).table
    for j, cw in enumerate(col_w):
        t.columns[j].width = Inches(cw)
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            cell = t.cell(i, j)
            cell.text = ""
            runs(cell.text_frame.paragraphs[0], val, size, WHITE if i == 0 else NAVY, i == 0)
            cell.fill.solid()
            cell.fill.fore_color.rgb = NAVY if i == 0 else (LIGHT if i % 2 else WHITE)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE


def new(title, notes):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.1))
    bar.fill.solid()
    bar.fill.fore_color.rgb = NAVY
    bar.line.fill.background()
    accent = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.1), prs.slide_width, Inches(0.07))
    accent.fill.solid()
    accent.fill.fore_color.rgb = ORANGE
    accent.line.fill.background()
    text(s, 0.5, 0.15, 12.3, 0.85, title, 32, WHITE, anchor=MSO_ANCHOR.MIDDLE, bold=True)
    text(s, 0.2, 7.05, 1, 0.4, str(len(prs.slides)), 12, GRAY)
    s.notes_slide.notes_text_frame.text = notes
    transkrip.append((len(prs.slides), title, notes))
    return s


def section(title, sub, notes):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = NAVY
    text(s, 0.8, 2.3, 11.7, 1.5, title, 54, WHITE, PP_ALIGN.CENTER, MSO_ANCHOR.MIDDLE, bold=True)
    text(s, 0.8, 3.9, 11.7, 1.4, sub, 26, ORANGE, PP_ALIGN.CENTER)
    s.notes_slide.notes_text_frame.text = notes
    transkrip.append((len(prs.slides), title, notes))
    return s


# ---------- helper grafik (matplotlib) ----------
def plot_fn(fn, judul, color, ylim=None):
    x = np.linspace(-5, 5, 400)
    fig, ax = plt.subplots(figsize=(4.6, 3))
    ax.plot(x, fn(x), lw=3.5, color=color)
    ax.axhline(0, color="gray", lw=0.8)
    ax.axvline(0, color="gray", lw=0.8)
    ax.set_title(judul, fontsize=17, fontweight="bold")
    ax.grid(alpha=0.3)
    if ylim:
        ax.set_ylim(*ylim)
    return fig


def gd_path(lr, x0=-4.0, n=10):
    xs = [x0]
    for _ in range(n):
        xs.append(xs[-1] - lr * 2 * xs[-1])  # turunan x^2 = 2x
    return np.array(xs)


def plot_gd(ax, lr, judul, n=10, color="#3A7BD5"):
    x = np.linspace(-7, 7, 300)
    ax.plot(x, x ** 2, color="#5A6275", lw=2)
    p = gd_path(lr, n=n)
    ax.plot(p, p ** 2, "o-", color=color, ms=7, lw=1.5)
    ax.plot(0, 0, "*", color="#2E9E6A", ms=18)
    ax.set_title(judul, fontsize=14, fontweight="bold")
    ax.set_xlabel("bobot (w)")
    ax.set_ylabel("loss")
    ax.set_ylim(-2, 50)
    ax.set_xticks([])
    ax.set_yticks([])


def konvolusi(img, k):
    n = img.shape[0] - k.shape[0] + 1
    return np.array([[int((img[i:i + 3, j:j + 3] * k).sum()) for j in range(n)] for i in range(n)])


# =====================================================================
# SLIDE
# =====================================================================

s = prs.slides.add_slide(prs.slide_layouts[6])
s.background.fill.solid()
s.background.fill.fore_color.rgb = NAVY
text(s, 0.8, 1.6, 11.7, 1.8, "Deep Learning & Convolutional Neural Network (CNN)", 46, WHITE,
     PP_ALIGN.CENTER, MSO_ANCHOR.MIDDLE, bold=True)
text(s, 0.8, 3.4, 11.7, 1, "Cara kerja, jenis layer, activation function, optimizer, dan prinsip kerja CNN",
     24, ORANGE, PP_ALIGN.CENTER)
text(s, 0.8, 4.8, 11.7, 1.5, [f"{NAMA}  •  NPM {NPM}", "Mata Kuliah Visi Komputer — Pertemuan 10"], 22, WHITE,
     PP_ALIGN.CENTER)
notes = (f"Assalamualaikum warahmatullahi wabarakatuh. Perkenalkan, nama saya {NAMA} dengan NPM {NPM}. Pada "
         "video ini saya akan mempresentasikan tugas Visi Komputer pertemuan kesepuluh. Topiknya ada dua, "
         "yaitu deep learning, yang mencakup cara kerja, jenis layer, activation function, dan optimizer, "
         "lalu dilanjutkan dengan cara kerja dan prinsip kerja CNN.")
s.notes_slide.notes_text_frame.text = notes
transkrip.append((1, "Judul", notes))

s = new("Materi",
        "Supaya mudah diikuti, materinya saya bagi menjadi dua bagian. Di bagian pertama, kita mulai dari "
        "pengertian deep learning dan neuron buatan, lalu melihat bagaimana jaringan belajar, serta peran "
        "activation function dan optimizer. Setelah dasarnya paham, di bagian kedua kita masuk ke CNN, mulai "
        "dari cara komputer membaca gambar sampai langkah-langkah CNN mengenali gambar.")
card(s, 0.7, 1.6, 5.8, 5.2, ["**BAGIAN 1 — Deep Learning**", "1. Pengertian Deep Learning", "2. Neuron buatan",
                             "3. Cara kerja (proses training)", "4. Tipe & jenis layer", "5. Activation function",
                             "6. Optimizer"], LIGHT, BLUE, 22)
card(s, 6.9, 1.6, 5.8, 5.2, ["**BAGIAN 2 — CNN**", "7. Gambar sebagai data angka", "8. Kenapa butuh CNN",
                             "9. Prinsip kerja CNN", "10. Cara kerja: Konvolusi → ReLU → Pooling → Flatten → "
                             "Fully Connected", "11. Kesimpulan"], LIGHT, ORANGE, 22)

section("Bagian 1: Deep Learning", "cara kerja • layer • activation function • optimizer",
        "Baik, kita mulai dari bagian pertama, yaitu deep learning.")

s = new("AI, Machine Learning, dan Deep Learning",
        "Sebelum masuk ke cara kerjanya, kita lihat dulu posisi deep learning di antara istilah lain. Kotak "
        "paling luar adalah AI, yaitu bidang yang membuat mesin bisa bertindak cerdas. Di dalamnya ada "
        "machine learning, di mana mesin tidak diberi aturan satu per satu, tetapi belajar sendiri dari data."
        " Lalu di dalam machine learning ada deep learning, yang memakai jaringan saraf tiruan dengan banyak "
        "lapisan, sehingga disebut deep.")
text(s, 0.6, 1.5, 6.6, 5.6, "**Artificial Intelligence (AI)**", 22, NAVY, PP_ALIGN.CENTER,
     shape=MSO_SHAPE.ROUNDED_RECTANGLE, fill=SOFT_BLUE)
text(s, 1.2, 2.3, 5.4, 4.5, "**Machine Learning (ML)**", 22, NAVY, PP_ALIGN.CENTER,
     shape=MSO_SHAPE.ROUNDED_RECTANGLE, fill=SOFT_ORANGE)
box(s, 1.9, 3.3, 4.0, 3.0, ["**Deep Learning (DL)**", "jaringan saraf berlapis-lapis"], ORANGE, WHITE, 20, False)
bullets(s, ["**AI** = membuat mesin bisa bertindak cerdas",
            "**ML** = mesin belajar dari **data**, bukan dari aturan yang ditulis manual",
            "**DL** = ML yang memakai **jaringan saraf tiruan** dengan **banyak layer**",
            "\"Deep\" = jumlah layernya **banyak**"], 7.6, 1.7, 5.4, 5.2, 21)

s = new("Neuron Buatan",
        "Lalu, jaringan saraf tiruan itu tersusun dari neuron buatan seperti di slide ini. Neuron menerima "
        "beberapa input, dan setiap input punya bobot yang menunjukkan seberapa penting input tersebut. "
        "Pertama, setiap input dikalikan dengan bobotnya, lalu semuanya dijumlahkan dan ditambah bias, dan "
        "hasilnya kita sebut z. Setelah itu, z dimasukkan ke activation function sehingga keluar output y. "
        "Pada contoh di bawah, nilai z-nya 0,3. Nah, bobot dan bias inilah yang nantinya dipelajari oleh deep"
        " learning.")
ins = [(1.4, 1.9), (1.4, 3.1), (1.4, 4.3)]
sx, sy = 5.6, 3.1
for i, (x, y) in enumerate(ins):
    garis(s, x, y, sx, sy, GRAY, 2)
    text(s, (x + sx) / 2 - 0.4, (y + sy) / 2 - 0.5, 0.9, 0.4, f"w{i + 1}", 18, RED, PP_ALIGN.CENTER, bold=True)
    box(s, x - 0.4, y - 0.4, 0.8, 0.8, f"x{i + 1}", BLUE, WHITE, 20, True, MSO_SHAPE.OVAL)
garis(s, sx, 1.75, sx, sy, GRAY, 2)
box(s, sx - 0.8, 1.35, 1.6, 0.5, "b (bias)", SOFT_ORANGE, NAVY, 16)
box(s, sx - 0.65, sy - 0.65, 1.3, 1.3, "Σ", ORANGE, WHITE, 36, True, MSO_SHAPE.OVAL)
panah(s, 6.45, 2.9)
box(s, 7.15, 2.5, 1.8, 1.2, ["f( )", "aktivasi"], GREEN, WHITE, 20)
panah(s, 9.15, 2.9)
box(s, 9.85, 2.65, 0.9, 0.9, "y", NAVY, WHITE, 22, True, MSO_SHAPE.OVAL)
text(s, 10.85, 2.8, 2.2, 0.6, "output", 18, NAVY)
card(s, 0.8, 5.0, 11.7, 2.0, ["**Langkah 1 — jumlahkan:**   z = x1·w1 + x2·w2 + x3·w3 + b",
                              "**Langkah 2 — aktivasi:**     y = f(z)",
                              "**Contoh:**  x = (1, 1, 1),  w = (0,6; 0,4; −0,8),  b = 0,1  →  "
                              "z = 0,6 + 0,4 − 0,8 + 0,1 = **0,3**"], LIGHT, ORANGE, 20)

s = new("Tipe Layer Berdasarkan Posisi",
        "Karena satu neuron kemampuannya terbatas, neuron-neuron disusun berlapis menjadi jaringan. "
        "Berdasarkan posisinya, ada tiga tipe layer. Input layer adalah tempat data masuk, misalnya nilai "
        "piksel gambar. Data itu lalu diolah di hidden layer, tempat pola dipelajari, sampai akhirnya output "
        "layer memberikan jawaban, misalnya kucing atau anjing. Semakin banyak hidden layer-nya, jaringannya "
        "semakin dalam, dan dari situlah nama deep learning berasal.")
nn(s, [3, 4, 4, 2], 1.3, 1.6, 6.3, 4.2, [BLUE, ORANGE, ORANGE, GREEN],
   ["Input layer", "Hidden layer 1", "Hidden layer 2", "Output layer"])
bullets(s, ["**Input layer** — tempat data masuk (mis. nilai piksel)",
            "**Hidden layer** — mengolah data & mempelajari pola",
            "**Output layer** — jawaban akhir (mis. kucing / anjing)",
            "Hidden layer **banyak** = jaringan **\"deep\"**"], 8.6, 1.6, 4.5, 5.3, 20)

s = new("Cara Kerja Deep Learning (Proses Training)",
        "Setelah jaringannya tersusun, bagaimana jaringan ini belajar? Prosesnya disebut training. Pertama, "
        "data dihitung lapis demi lapis sampai menghasilkan prediksi, yang disebut forward pass. Prediksi itu"
        " dibandingkan dengan jawaban yang benar, dan selisihnya disebut loss. Kesalahan itu lalu dihitung "
        "mundur untuk mengetahui pengaruh setiap bobot, yang disebut backpropagation, kemudian optimizer "
        "memperbarui bobot supaya loss mengecil. Siklus ini diulang, di mana satu putaran seluruh data "
        "disebut epoch, dan data diproses per kelompok kecil yang disebut batch.")
steps = [("1. Forward Pass", "data dihitung dari input → output, hasilnya prediksi", BLUE),
         ("2. Hitung Loss", "selisih prediksi dengan jawaban benar", ORANGE),
         ("3. Backpropagation", "hitung mundur pengaruh tiap bobot terhadap loss", RED),
         ("4. Update Bobot", "optimizer mengubah bobot supaya loss turun", GREEN),
         ("5. Ulangi", "sampai loss kecil", NAVY)]
for i, (t, d, col) in enumerate(steps):
    x = 0.45 + i * 2.55
    box(s, x, 1.9, 2.1, 1.3, t, col, WHITE, 16)
    text(s, x, 3.35, 2.1, 1.4, d, 17, NAVY, PP_ALIGN.CENTER)
    if i < 4:
        panah(s, x + 2.12, 2.35, 0.4, 0.4)
panah(s, 6.2, 4.65, 0.9, 0.7, ORANGE, MSO_SHAPE.LEFT_ARROW)
card(s, 0.8, 5.5, 11.7, 1.3, ["**Epoch** = 1 putaran, seluruh data latih sudah diproses 1 kali",
                              "**Batch** = kelompok kecil data yang diproses sekaligus (mis. 32 data)"], LIGHT, ORANGE, 20)

s = new("Jenis Layer Berdasarkan Fungsi",
        "Selain berdasarkan posisi, layer juga dibedakan berdasarkan fungsinya, seperti di tabel ini. Dense "
        "layer menghubungkan setiap neuron ke semua neuron sebelumnya, dan biasanya dipakai di akhir untuk "
        "menentukan kelas. Convolutional layer mendeteksi pola seperti tepi dan garis, lalu pooling "
        "memperkecil ukuran data, dan flatten mengubahnya menjadi satu baris. Ada juga dropout, yang "
        "mematikan sebagian neuron secara acak saat training supaya model tidak sekadar hafal data, serta "
        "recurrent layer untuk data berurutan seperti teks.")
table(s, [["Layer", "Fungsinya", "Dipakai untuk"],
          ["**Dense / Fully Connected**", "Setiap neuron terhubung ke SEMUA neuron layer sebelumnya",
           "Klasifikasi di bagian akhir"],
          ["**Convolutional (Conv)**", "Mendeteksi pola lokal: tepi, garis, tekstur", "Inti dari CNN"],
          ["**Pooling**", "Memperkecil ukuran data, info penting tetap ada", "CNN, setelah Conv"],
          ["**Flatten**", "Mengubah data 2D/3D menjadi 1 baris", "Sebelum masuk Dense"],
          ["**Dropout**", "Menonaktifkan sebagian neuron secara acak saat training", "Mencegah overfitting"],
          ["**Recurrent (RNN / LSTM)**", "Mengolah data berurutan", "Teks, suara, data waktu"]],
      0.5, 1.5, [3.5, 5.3, 3.5], 18, 0.75)

s = new("Activation Function: Kenapa Perlu?",
        "Sekarang kita kembali ke huruf f di neuron tadi, yaitu activation function. Fungsi ini diperlukan "
        "karena tanpa aktivasi, jaringan hanya bisa menghasilkan garis lurus, berapa pun jumlah layernya. "
        "Padahal, seperti gambar di kanan, data nyata sering tidak bisa dipisahkan dengan garis lurus. Dengan"
        " activation function, jaringan bisa membentuk batas yang melengkung, sehingga mampu mempelajari pola"
        " yang rumit.")
bullets(s, ["Activation function = fungsi **f** di neuron, mengubah z menjadi output",
            "**Tanpa aktivasi** → sebanyak apa pun layer, hasilnya tetap **garis lurus** (linear)",
            "**Dengan aktivasi** → jaringan jadi **non-linear** → bisa mempelajari pola rumit"],
        0.6, 1.5, 6.0, 5.5, 21)
rng = np.random.default_rng(0)
ang = rng.uniform(0, 2 * np.pi, 120)
rad = np.r_[rng.uniform(0, 1, 60), rng.uniform(1.6, 2.4, 60)]
px, py = rad * np.cos(ang), rad * np.sin(ang)
fig, axs = plt.subplots(1, 2, figsize=(8, 4))
for ax, judul in zip(axs, ["Tanpa aktivasi: garis lurus ✗", "Dengan aktivasi: melengkung ✓"]):
    ax.scatter(px[:60], py[:60], color="#3A7BD5", s=22)
    ax.scatter(px[60:], py[60:], color="#F28C28", s=22)
    ax.set_title(judul, fontsize=13, fontweight="bold")
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
axs[0].plot([-2.5, 2.5], [-1.2, 1.8], color="#D64545", lw=3)
axs[1].add_patch(Circle((0, 0), 1.3, fill=False, color="#2E9E6A", lw=3))
gambar(s, fig, 6.8, 2.0, 6.2)

sig = lambda x: 1 / (1 + np.exp(-x))
s = new("Activation Function: Sigmoid & Tanh",
        "Activation function yang pertama adalah sigmoid, yang mengubah input menjadi nilai antara nol dan "
        "satu. Karena hasilnya bisa dibaca sebagai peluang, sigmoid cocok untuk output dua kelas. Tanh "
        "bentuknya mirip, tetapi rentangnya minus satu sampai satu. Masalahnya, kalau input terlalu besar "
        "atau terlalu kecil, grafik keduanya menjadi datar, sehingga bobot sangat lambat berubah. Masalah ini"
        " disebut vanishing gradient.")
gambar(s, plot_fn(sig, "Sigmoid", "#3A7BD5"), 1.0, 1.35, 4.6)
gambar(s, plot_fn(np.tanh, "Tanh", "#F28C28"), 7.4, 1.35, 4.6)
bullets(s, ["Output **0 sampai 1**", "Cocok untuk output **2 kelas**"], 0.8, 4.6, 5.8, 2.4, 19)
bullets(s, ["Output **−1 sampai 1**", "Kekurangan keduanya: ujung grafik **datar**",
            "→ training lambat (**vanishing gradient**)"], 7.2, 4.6, 5.8, 2.4, 19)

s = new("Activation Function: ReLU & Leaky ReLU",
        "Untuk mengatasi masalah itu, sekarang lebih banyak dipakai ReLU. Aturannya sederhana: input negatif "
        "menjadi nol, sedangkan input positif tetap. Karena ringan dihitung, ReLU menjadi standar untuk "
        "hidden layer, termasuk di CNN. Tetapi neuron yang terus menerima input negatif bisa berhenti "
        "belajar, jadi muncullah Leaky ReLU, yang mengalikan input negatif dengan angka kecil seperti 0,01, "
        "sehingga neuron tetap bisa belajar.")
gambar(s, plot_fn(lambda x: np.maximum(0, x), "ReLU", "#2E9E6A"), 1.0, 1.35, 4.6)
gambar(s, plot_fn(lambda x: np.where(x > 0, x, 0.1 * x), "Leaky ReLU", "#D64545"), 7.4, 1.35, 4.6)
bullets(s, ["Negatif → **0**, positif → **tetap**", "**Standar untuk hidden layer** & CNN"],
        0.8, 4.6, 5.8, 2.4, 19)
bullets(s, ["Negatif → dikali angka kecil (mis. **0,01**)", "Mencegah neuron berhenti belajar",
            "(kemiringan dibesarkan supaya terlihat)"], 7.2, 4.6, 5.8, 2.4, 19)

skor = np.array([2.0, 1.0, 0.1])
p = np.exp(skor) / np.exp(skor).sum()
assert [round(v * 100) for v in p] == [66, 24, 10]
s = new("Activation Function: Softmax",
        "Selanjutnya softmax, yang dipakai di output ketika kelasnya lebih dari dua. Softmax mengubah skor "
        "mentah menjadi peluang yang totalnya seratus persen. Pada contoh ini, skor kucing, anjing, dan "
        "burung berubah menjadi 66, 24, dan 10 persen. Karena peluang terbesarnya kucing, maka prediksinya "
        "adalah kucing.")
text(s, 0.8, 1.45, 3, 0.5, "**Skor mentah**", 20, NAVY, PP_ALIGN.CENTER)
text(s, 6.0, 1.45, 6, 0.5, "**Setelah softmax (peluang)**", 20, NAVY)
for i, (nm, sk, pv, col) in enumerate(zip(["Kucing", "Anjing", "Burung"], skor, p, [ORANGE, BLUE, GREEN])):
    y = 2.1 + i * 1.25
    box(s, 0.8, y, 1.6, 0.9, nm, col, WHITE, 18)
    box(s, 2.5, y, 1.3, 0.9, f"{sk:.1f}".replace(".", ","), WHITE, NAVY, 20, True, line=GRAY)
    box(s, 6.0, y, max(0.3, 6.0 * pv), 0.9, "", col, shape=MSO_SHAPE.RECTANGLE)
    text(s, 6.1 + 6.0 * pv, y + 0.15, 1.5, 0.6, f"**{round(pv * 100)}%**", 22)
panah(s, 4.2, 3.0, 1.4, 0.9, ORANGE)
text(s, 4.0, 3.9, 1.8, 0.5, "softmax", 18, ORANGE, PP_ALIGN.CENTER, bold=True)
card(s, 0.8, 6.0, 11.7, 1.0, ["Total = 100%  →  prediksi = peluang terbesar = **KUCING**.   "
                              "Dipakai di output untuk **lebih dari 2 kelas**."], LIGHT, ORANGE, 20)

s = new("Ringkasan: Activation Function",
        "Jadi ringkasnya, hidden layer biasanya memakai ReLU. Untuk output dua kelas kita pakai sigmoid, "
        "untuk banyak kelas kita pakai softmax, dan kalau outputnya berupa angka, seperti harga rumah, kita "
        "pakai linear atau tanpa aktivasi.")
table(s, [["Dipakai di mana?", "Pakai apa?", "Contoh"],
          ["Hidden layer", "**ReLU** (atau Leaky ReLU)", "Semua layer di tengah, termasuk CNN"],
          ["Output: 2 kelas", "**Sigmoid**", "Spam / bukan spam"],
          ["Output: banyak kelas", "**Softmax**", "Kucing / anjing / burung"],
          ["Output: angka", "**Linear** (tanpa aktivasi)", "Prediksi harga rumah"]],
      1.0, 1.8, [3.4, 3.9, 4.0], 21, 1.0)

s = new("Optimizer: Gradient Descent",
        "Tadi sudah disebut bahwa bobot diperbarui oleh optimizer. Grafik di kiri menunjukkan hubungan bobot "
        "dengan loss, dan tujuannya adalah mencari bobot di titik loss terendah. Caranya disebut gradient "
        "descent: kita hitung gradient, yaitu kemiringan grafik di posisi bobot sekarang, lalu bobot digeser "
        "ke arah yang menurun. Rumusnya, bobot baru sama dengan bobot lama dikurangi learning rate dikali "
        "gradient, dan karena diulang terus, titik birunya perlahan turun ke loss terendah.")
fig, ax = plt.subplots(figsize=(5.5, 4.2))
plot_gd(ax, 0.2, "Gradient Descent", 8)
ax.set_ylim(-2, 20)
ax.set_xlim(-4.8, 4.8)
ax.annotate("bobot awal", (-4, 16), (-2.4, 18.5), fontsize=12, arrowprops=dict(arrowstyle="->"))
ax.annotate("loss terendah", (0, 0), (0.4, 12), fontsize=12, arrowprops=dict(arrowstyle="->"))
gambar(s, fig, 0.5, 1.4, 6.0)
bullets(s, ["**Optimizer** = algoritma yang memperbarui bobot supaya **loss turun**",
            "**Gradient** = kemiringan grafik loss di posisi bobot sekarang",
            "Bobot digeser ke arah yang **menurun**, diulang sampai loss terendah"], 6.9, 1.5, 6.1, 3.6, 20)
card(s, 6.9, 5.1, 6.0, 1.3, ["**w baru = w lama − learning rate × gradient**"], LIGHT, ORANGE, 21)

s = new("Learning Rate",
        "Learning rate di rumus tadi menentukan seberapa besar langkah perubahan bobot. Kalau terlalu kecil, "
        "training jadi lambat. Kalau pas, loss cepat turun ke titik terendah. Tetapi kalau terlalu besar, "
        "bobot melompat melewati titik terendah dan loss malah naik. Karena itu, nilai awal yang umum dipakai"
        " adalah 0,001.")
fig, axs = plt.subplots(1, 3, figsize=(13, 4))
plot_gd(axs[0], 0.03, "Terlalu kecil → lambat", 12, "#F28C28")
plot_gd(axs[1], 0.3, "Pas → cepat sampai", 8, "#2E9E6A")
plot_gd(axs[2], 1.05, "Terlalu besar → loss naik", 5, "#D64545")
gambar(s, fig, 0.4, 1.5, 12.5)
box(s, 0.8, 5.9, 11.7, 1.0, "Learning rate = besar langkah perubahan bobot.  Nilai awal yang umum: 0,001",
    SOFT_ORANGE, NAVY, 21)

s = new("Jenis-Jenis Optimizer",
        "Gradient descent punya beberapa variasi, seperti di tabel ini. Batch gradient descent memperbarui "
        "bobot setelah melihat seluruh data, jadi akurat tetapi lambat, sedangkan SGD memperbarui setiap satu"
        " data, jadi cepat tetapi tidak stabil. Mini-batch berada di tengahnya dan paling umum dipakai. "
        "Momentum menambahkan pengaruh langkah sebelumnya, dan RMSprop mengatur learning rate otomatis per "
        "bobot. Adam menggabungkan keduanya, sehingga paling sering dipakai sebagai pilihan awal.")
table(s, [["Optimizer", "Cara kerjanya", "Kelebihan / kekurangan"],
          ["**Batch Gradient Descent**", "Update bobot setelah melihat SEMUA data", "Akurat, tapi lambat"],
          ["**SGD (Stochastic)**", "Update bobot setiap 1 data", "Cepat, tapi tidak stabil"],
          ["**Mini-batch GD**", "Update bobot setiap 1 batch (mis. 32 data)", "Seimbang, paling umum"],
          ["**Momentum**", "Menambahkan pengaruh langkah sebelumnya", "Lebih cepat & stabil"],
          ["**RMSprop**", "Learning rate diatur otomatis per bobot", "Stabil untuk data beragam"],
          ["**Adam** ⭐", "Gabungan Momentum + RMSprop", "Paling populer, pilihan awal"]],
      0.5, 1.5, [3.4, 4.9, 4.0], 18, 0.78)

section("Bagian 2: Convolutional Neural Network (CNN)", "cara kerja & prinsip kerja CNN",
        "Dengan begitu, dasar deep learning sudah kita bahas. Sekarang kita masuk ke bagian kedua, yaitu CNN,"
        " jenis deep learning yang khusus untuk mengolah gambar.")

smile = [[255] * 7, [255, 255, 0, 255, 0, 255, 255], [255, 255, 0, 255, 0, 255, 255], [255] * 7,
         [255, 0, 255, 255, 255, 0, 255], [255, 255, 0, 0, 0, 255, 255], [255] * 7]
s = new("Gambar bagi Komputer = Tabel Angka",
        "Sebelum masuk ke CNN, kita lihat dulu bagaimana komputer membaca gambar. Bagi komputer, gambar "
        "adalah tabel angka. Setiap kotak disebut piksel, dengan nilai 0 untuk hitam sampai 255 untuk putih, "
        "jadi gambar wajah di kiri sebenarnya adalah tabel angka di tengah. Untuk gambar berwarna, tabelnya "
        "ada tiga, yaitu merah, hijau, dan biru. Nah, tugas CNN adalah menemukan pola dari angka-angka ini.")
fig, ax = plt.subplots(figsize=(3.5, 3.5))
ax.imshow(smile, cmap="gray", vmin=0, vmax=255)
ax.set_xticks(np.arange(-0.5, 7), minor=True)
ax.set_yticks(np.arange(-0.5, 7), minor=True)
ax.grid(which="minor", color="#5A6275", lw=1)
ax.tick_params(which="both", length=0, labelbottom=False, labelleft=False)
ax.set_title("Gambar", fontsize=14, fontweight="bold")
gambar(s, fig, 0.5, 1.5, 3.6)
panah(s, 4.25, 3.3, 0.6, 0.5)
text(s, 5.0, 1.4, 3.6, 0.5, "**Data yang dibaca komputer**", 17, NAVY, PP_ALIGN.CENTER)
matrix(s, smile, 5.0, 1.95, 0.5, {(r, k): SOFT_GRAY for r in range(7) for k in range(7) if smile[r][k] == 0}, 11)
for i, (nm, col) in enumerate([("R (merah)", RED), ("G (hijau)", GREEN), ("B (biru)", BLUE)]):
    box(s, 9.3 + i * 0.35, 2.0 + i * 0.35, 2.4, 1.9, nm if i == 2 else "", col, WHITE, 18,
        shape=MSO_SHAPE.RECTANGLE, line=WHITE)
text(s, 9.1, 4.75, 3.9, 1.2, "Gambar berwarna = **3 channel** (R, G, B)", 17, NAVY, PP_ALIGN.CENTER)
card(s, 0.6, 5.85, 12.1, 1.15, ["1 kotak = 1 **piksel**, nilainya **0 (hitam) sampai 255 (putih)**.  "
                                "Tugas CNN: menemukan pola dari angka-angka ini."], LIGHT, ORANGE, 19)

s = new("Kenapa Gambar Butuh CNN?",
        "Lalu kenapa gambar tidak langsung dimasukkan ke dense layer biasa? Masalah pertama, bobotnya terlalu"
        " banyak, karena gambar 224 kali 224 berwarna punya sekitar 150 ribu input, sehingga butuh sekitar "
        "150 juta bobot untuk seribu neuron. Masalah kedua, gambar harus diratakan, sehingga informasi piksel"
        " mana yang berdekatan ikut hilang. CNN mengatasi keduanya, karena satu filter 3 kali 3 hanya butuh "
        "27 bobot, dan gambarnya tetap dua dimensi.")
card(s, 0.6, 1.5, 5.9, 5.4, ["**✗ Pakai Dense biasa**", "",
                             "**1. Bobot terlalu banyak**", "Gambar 224×224×3 = 150.528 input",
                             "× 1.000 neuron ≈ **150 juta bobot** (1 layer saja)", "",
                             "**2. Posisi hilang**", "Gambar diratakan jadi 1 baris → hubungan antar piksel "
                                                     "yang berdekatan hilang"], SOFT_RED, RED, 19)
card(s, 6.8, 1.5, 5.9, 5.4, ["**✓ Pakai CNN**", "",
                             "**1. Bobot sedikit**", "1 filter 3×3×3 = hanya **27 bobot**",
                             "dipakai berulang di seluruh gambar", "",
                             "**2. Posisi terjaga**", "Gambar tetap berbentuk 2D → hubungan antar piksel "
                                                      "tetap ada"], SOFT_GREEN, GREEN, 19)

s = new("Prinsip Kerja CNN",
        "CNN bisa seefisien itu karena tiga prinsip. Yang pertama local connectivity, artinya setiap neuron "
        "hanya melihat area kecil gambar, sehingga menangkap pola lokal seperti tepi. Yang kedua weight "
        "sharing, artinya filter yang sama dipakai di seluruh gambar, jadi bobotnya sedikit dan pola bisa "
        "dikenali di posisi mana pun. Yang ketiga hierarki fitur, di mana layer awal mendeteksi garis, layer "
        "tengah mendeteksi bentuk, dan layer akhir mengenali objek.")
for i, (judul, isi, col) in enumerate([
        ("1. Local Connectivity", ["Setiap neuron hanya melihat **area kecil** gambar (mis. 3×3 piksel)",
                                   "Menangkap pola lokal: tepi, sudut, garis"], BLUE),
        ("2. Weight Sharing", ["**Filter yang sama** dipakai di seluruh bagian gambar",
                               "Bobot sedikit, pola dikenali di **posisi mana pun**"], ORANGE),
        ("3. Hierarki Fitur", ["Layer awal → **tepi & garis**", "Layer tengah → **bentuk**",
                               "Layer akhir → **objek**"], GREEN)]):
    x = 0.55 + i * 4.15
    box(s, x, 1.55, 3.9, 0.9, judul, col, WHITE, 21)
    card(s, x, 2.6, 3.9, 4.3, isi, LIGHT, col, 20)

s = new("Cara Kerja CNN: Alur Umum",
        "Dari prinsip tadi, alur CNN secara umum terlihat di slide ini. Gambar masuk ke convolution dan ReLU,"
        " lalu diperkecil dengan pooling, dan pasangan ini bisa diulang. Bagian oranye ini disebut ekstraksi "
        "fitur. Setelah itu data di-flatten, diolah di fully connected layer, lalu softmax menentukan "
        "kelasnya, dan bagian hijau ini disebut klasifikasi. Sekarang kita bahas langkahnya satu per satu.")
chain = [("Input\ngambar", NAVY), ("Conv\n+ ReLU", ORANGE), ("Pooling", ORANGE), ("Conv\n+ ReLU", ORANGE),
         ("Pooling", ORANGE), ("Flatten", GREEN), ("Fully\nConnected", GREEN), ("Output\nSoftmax", GREEN)]
for i, (t, col) in enumerate(chain):
    x = 0.45 + i * 1.57
    box(s, x, 2.2, 1.3, 1.5, t.split("\n"), col, WHITE, 16)
    if i < 7:
        panah(s, x + 1.31, 2.75, 0.25, 0.35)
box(s, 2.02, 4.0, 6.0, 0.8, "EKSTRAKSI FITUR — mencari pola di gambar", SOFT_ORANGE, NAVY, 18)
box(s, 8.3, 4.0, 4.5, 0.8, "KLASIFIKASI — menentukan kelas", SOFT_GREEN, NAVY, 18)
card(s, 0.6, 5.3, 12.1, 1.5, ["Pasangan **Conv + ReLU → Pooling** bisa diulang beberapa kali.",
                              "Semakin dalam, pola yang dideteksi semakin kompleks."], LIGHT, BLUE, 19)

img = np.array([[1, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0]])
ker = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
out = konvolusi(img, ker)
assert out.tolist() == [[4, 3, 4], [2, 4, 3], [2, 3, 4]]
s = new("Langkah 1 — Konvolusi",
        "Langkah pertama adalah konvolusi. Di sini ada input 5 kali 5 dan filter 3 kali 3. Filter diletakkan "
        "di pojok kiri atas, yaitu kotak oranye, lalu setiap angka dikalikan dengan angka filter di posisi "
        "yang sama dan semuanya dijumlahkan, sehingga hasilnya 4. Setelah itu filter digeser satu kotak dan "
        "dihitung lagi, sampai seluruh gambar selesai. Hasil akhirnya, tabel 3 kali 3 di kanan, disebut "
        "feature map.")
text(s, 0.6, 1.3, 3.0, 0.5, "**Input 5×5**", 18, NAVY, PP_ALIGN.CENTER)
matrix(s, img, 0.6, 1.8, 0.6, window(0, 0))
text(s, 3.75, 2.9, 0.7, 0.8, "×", 40, NAVY, PP_ALIGN.CENTER, bold=True)
text(s, 4.5, 1.3, 2.1, 0.5, "**Filter 3×3**", 18, NAVY, PP_ALIGN.CENTER)
matrix(s, ker, 4.5, 2.4, 0.7, {(r, k): SOFT_BLUE for r in range(3) for k in range(3)}, 18)
text(s, 6.9, 2.9, 0.7, 0.8, "=", 40, NAVY, PP_ALIGN.CENTER, bold=True)
text(s, 7.7, 1.3, 2.1, 0.5, "**Feature map**", 18, NAVY, PP_ALIGN.CENTER)
matrix(s, out, 7.7, 2.4, 0.7, {(0, 0): ORANGE}, 18)
card(s, 10.3, 1.8, 2.7, 3.0, ["**Filter / kernel**", "matriks kecil yang digeser di atas gambar"], LIGHT, BLUE, 18)
pairs = [f"{img[r, k]}×{ker[r, k]}" for r in range(3) for k in range(3)]
card(s, 0.6, 5.0, 12.4, 2.0, ["**1.** Kalikan angka yang sejajar (kotak oranye), lalu jumlahkan:",
                              "     " + " + ".join(pairs) + " = **4**",
                              "**2.** Geser filter 1 kotak → hitung lagi → sampai seluruh gambar selesai"],
     LIGHT, ORANGE, 19)

pad = np.pad(img, 1)
s = new("Stride & Padding",
        "Dari contoh tadi, ukuran gambar menyusut dari 5 kali 5 menjadi 3 kali 3, dan ini dipengaruhi stride "
        "dan padding. Stride adalah jumlah kotak setiap kali filter bergeser, jadi stride 2 membuat hasilnya "
        "lebih kecil. Padding adalah tambahan nilai nol di sekeliling gambar, seperti kotak abu-abu di kiri, "
        "supaya ukurannya tidak menyusut. Dengan rumus di slide, tanpa padding hasilnya 3 kali 3, sedangkan "
        "dengan padding satu ukurannya tetap 5 kali 5.")
matrix(s, pad, 0.6, 1.5, 0.5, {(r, k): SOFT_GRAY for r in range(7) for k in range(7) if r in (0, 6) or k in (0, 6)},
       14)
text(s, 0.6, 5.1, 3.5, 0.9, "abu-abu = **padding** (nilai 0)", 16, NAVY, PP_ALIGN.CENTER)
bullets(s, ["**Stride** = jumlah kotak pergeseran filter",
            ">stride 1 = geser 1 kotak,  stride 2 = geser 2 kotak (hasil lebih kecil)",
            "**Padding** = menambahkan nilai 0 di sekeliling gambar",
            ">supaya ukuran hasil **tidak menyusut**"], 4.6, 1.5, 8.4, 3.2, 20)
card(s, 4.6, 4.5, 8.3, 2.5, ["**Rumus ukuran hasil:**   (N − F + 2P) / S + 1",
                             "N = ukuran gambar, F = ukuran filter, P = padding, S = stride",
                             "Tanpa padding: (5 − 3 + 0) / 1 + 1 = **3**   → menyusut",
                             "Padding 1:      (5 − 3 + 2) / 1 + 1 = **5**   → tetap"], LIGHT, ORANGE, 18)

s = new("Filter & Feature Map",
        "Tadi kita hanya memakai satu filter, padahal setiap filter mendeteksi pola yang berbeda, misalnya "
        "garis vertikal, garis horizontal, atau penajaman seperti di slide ini. Karena itu, satu "
        "convolutional layer biasanya punya banyak filter, misalnya 32 atau 64, dan setiap filter "
        "menghasilkan satu feature map. Yang penting, nilai filter ini tidak ditentukan manual, tetapi "
        "dipelajari sendiri oleh CNN saat training.")
for i, (nm, K) in enumerate([("Garis vertikal", [[1, 0, -1]] * 3),
                             ("Garis horizontal", [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]),
                             ("Penajaman", [[0, -1, 0], [-1, 5, -1], [0, -1, 0]])]):
    x = 1.2 + i * 4.0
    text(s, x - 0.4, 1.4, 2.6, 0.5, f"**{nm}**", 19, NAVY, PP_ALIGN.CENTER)
    matrix(s, K, x, 1.95, 0.6,
           {(r, k): SOFT_GREEN if K[r][k] > 0 else SOFT_RED for r in range(3) for k in range(3) if K[r][k]}, 18)
bullets(s, ["Hijau = positif, merah = negatif",
            "1 layer Conv punya **banyak filter** (mis. 32 / 64) → tiap filter menghasilkan **1 feature map**",
            "**Nilai filter tidak ditentukan manual** — dipelajari saat training (backpropagation + optimizer)"],
        0.8, 4.0, 12, 3.0, 20)

relu_in = [[3, -2, 1], [-1, 4, -3], [2, -5, 0]]
s = new("Langkah 2 — ReLU",
        "Setelah feature map didapat, langkah kedua adalah ReLU. Semua nilai negatif diubah menjadi nol, "
        "sedangkan nilai positif tetap, jadi minus 2, minus 1, minus 3, dan minus 5 di contoh ini berubah "
        "menjadi nol. Dengan begitu, hanya bagian yang cocok dengan pola filter yang diteruskan ke layer "
        "berikutnya.")
neg = {(r, k): SOFT_RED for r in range(3) for k in range(3) if relu_in[r][k] < 0}
text(s, 1.5, 1.5, 2.4, 0.5, "**Sebelum ReLU**", 19, NAVY, PP_ALIGN.CENTER)
matrix(s, relu_in, 1.5, 2.1, 0.8, neg, 22)
panah(s, 4.6, 2.95, 1.6, 0.7, GREEN)
text(s, 4.4, 3.7, 2.0, 0.5, "ReLU", 20, GREEN, PP_ALIGN.CENTER, bold=True)
text(s, 6.9, 1.5, 2.4, 0.5, "**Sesudah ReLU**", 19, NAVY, PP_ALIGN.CENTER)
matrix(s, np.maximum(relu_in, 0), 6.9, 2.1, 0.8, {k: SOFT_GREEN for k in neg}, 22)
card(s, 10.0, 2.1, 2.9, 2.4, ["Negatif → **0**", "Positif → **tetap**"], LIGHT, GREEN, 21)
card(s, 1.0, 5.3, 11.9, 1.2, ["Tujuan: membuat CNN **non-linear** sehingga bisa mempelajari pola yang rumit."],
     LIGHT, ORANGE, 20)

P = [[1, 3, 2, 4], [5, 6, 1, 2], [7, 2, 9, 1], [3, 4, 6, 8]]
quad = [SOFT_BLUE, SOFT_ORANGE, SOFT_GREEN, SOFT_RED]
qcol = {(r, k): quad[(r // 2) * 2 + k // 2] for r in range(4) for k in range(4)}
mx = [[max(P[r][k] for r in (i, i + 1) for k in (j, j + 1)) for j in (0, 2)] for i in (0, 2)]
av = [[sum(P[r][k] for r in (i, i + 1) for k in (j, j + 1)) / 4 for j in (0, 2)] for i in (0, 2)]
assert mx == [[6, 4], [7, 9]] and av == [[3.75, 2.25], [4.0, 6.0]]
s = new("Langkah 3 — Pooling",
        "Karena ukuran feature map masih besar, langkah ketiga adalah pooling. Yang paling umum adalah max "
        "pooling 2 kali 2. Feature map dibagi menjadi area 2 kali 2 sesuai warnanya, lalu dari setiap area "
        "diambil nilai terbesar, yaitu 6, 4, 7, dan 9, sehingga ukurannya turun menjadi 2 kali 2. Ada juga "
        "average pooling yang mengambil rata-ratanya. Dengan ukuran lebih kecil, komputasi jadi lebih cepat "
        "dan model lebih tahan terhadap pergeseran objek.")
text(s, 0.6, 1.4, 3.2, 0.5, "**Feature map 4×4**", 19, NAVY, PP_ALIGN.CENTER)
matrix(s, P, 0.6, 1.95, 0.8, qcol, 22)
panah(s, 4.0, 3.0, 1.1, 0.6, ORANGE)
text(s, 5.3, 1.4, 2.4, 0.5, "**Max pooling**", 19, NAVY, PP_ALIGN.CENTER)
matrix(s, mx, 5.5, 2.35, 0.95, {(r, k): quad[r * 2 + k] for r in range(2) for k in range(2)}, 24)
text(s, 5.1, 4.35, 2.8, 0.5, "ambil **nilai terbesar**", 16, NAVY, PP_ALIGN.CENTER)
text(s, 8.2, 1.4, 2.4, 0.5, "**Average pooling**", 19, NAVY, PP_ALIGN.CENTER)
matrix(s, [[f"{v:g}".replace(".", ",") for v in row] for row in av], 8.4, 2.35, 0.95,
       {(r, k): quad[r * 2 + k] for r in range(2) for k in range(2)}, 20)
text(s, 8.0, 4.35, 2.8, 0.5, "ambil **rata-rata**", 16, NAVY, PP_ALIGN.CENTER)
card(s, 0.6, 5.2, 12.1, 1.8, ["**Manfaat:**  ukuran lebih kecil → komputasi lebih cepat  •  "
                              "lebih tahan terhadap pergeseran kecil",
                              "Paling umum: **max pooling 2×2, stride 2** → ukuran jadi setengah"], LIGHT, ORANGE, 18)

s = new("Langkah 4 — Flatten, Fully Connected, Output",
        "Setelah fiturnya didapat, langkah terakhir adalah klasifikasi. Hasil pooling diratakan dengan "
        "flatten menjadi satu baris, karena fully connected layer hanya menerima input satu dimensi. Fully "
        "connected layer lalu mengolah fitur-fitur itu, dan softmax di output menghasilkan peluang setiap "
        "kelas. Di sini hasilnya 85 persen kucing, sehingga CNN memprediksi gambar tersebut adalah kucing.")
matrix(s, mx, 0.7, 2.8, 0.85, {(r, k): quad[r * 2 + k] for r in range(2) for k in range(2)}, 22)
panah(s, 2.6, 3.3, 0.9, 0.6, ORANGE)
text(s, 2.4, 3.9, 1.3, 0.5, "Flatten", 16, ORANGE, PP_ALIGN.CENTER, bold=True)
nn(s, [4, 3, 2], 4.3, 1.6, 4.6, 4.0, [BLUE, ORANGE, GREEN], ["1 baris", "Fully Connected", "Output (softmax)"],
   [["6", "4", "7", "9"], None, None], 0.7)
box(s, 9.6, 2.65, 2.9, 0.75, "Kucing 85% ✓", GREEN, WHITE, 20)
box(s, 9.6, 3.8, 2.9, 0.75, "Anjing 15%", SOFT_GRAY, NAVY, 20)
card(s, 0.6, 6.2, 12.1, 0.85, ["Prediksi CNN: **KUCING** (peluang terbesar)"], LIGHT, ORANGE, 20)

assert 16 * 16 * 64 == 16384
s = new("Contoh Arsitektur CNN: Kucing vs Anjing",
        "Kalau semua langkah tadi digabung, contohnya seperti tabel ini. Gambar 64 kali 64 kali 3 melewati "
        "dua kali konvolusi dan pooling, sehingga ukurannya mengecil menjadi 16 kali 16, tetapi jumlah "
        "feature map-nya bertambah menjadi 64. Hasilnya lalu di-flatten menjadi 16.384 nilai, diolah di dense"
        " 128 neuron, dan berakhir di dense 2 neuron dengan softmax. Jadi polanya, semakin dalam, ukuran "
        "gambar semakin kecil tetapi fiturnya semakin banyak.")
table(s, [["Layer", "Ukuran output", "Keterangan"],
          ["Input gambar", "64 × 64 × 3", "gambar RGB"],
          ["Conv2D 32 filter 3×3 + ReLU", "64 × 64 × 32", "32 feature map (padding = same)"],
          ["MaxPooling 2×2", "32 × 32 × 32", "ukuran jadi setengah"],
          ["Conv2D 64 filter 3×3 + ReLU", "32 × 32 × 64", "64 feature map"],
          ["MaxPooling 2×2", "16 × 16 × 64", "setengah lagi"],
          ["Flatten", "16.384", "16 × 16 × 64 jadi 1 baris"],
          ["Dense 128 + ReLU", "128", "fully connected"],
          ["Dense 2 + Softmax", "2", "peluang kucing & anjing"]],
      0.6, 1.45, [4.4, 3.0, 4.7], 17, 0.58)
text(s, 0.6, 6.85, 12.1, 0.5, "Pola: ukuran gambar **makin kecil**, jumlah fitur **makin banyak**", 18, ORANGE)

s = new("Kesimpulan",
        "Sebagai kesimpulan, deep learning adalah jaringan saraf berlapis yang belajar lewat forward pass, "
        "loss, backpropagation, dan pembaruan bobot. Layer-nya dibagi menurut posisi dan fungsi, activation "
        "function membuat jaringan bisa mempelajari pola rumit, dan optimizer seperti Adam memperbarui bobot "
        "supaya loss turun. Sementara itu, CNN bekerja dengan local connectivity, weight sharing, dan "
        "hierarki fitur, melalui alur konvolusi, ReLU, pooling, flatten, fully connected, hingga softmax.")
bullets(s, ["**Deep learning** = jaringan saraf berlapis, belajar lewat forward pass → loss → backprop → update bobot",
            "**Layer:** tipe (input, hidden, output) & jenis (Dense, Conv, Pooling, Flatten, Dropout, ...)",
            "**Activation function:** membuat jaringan non-linear — ReLU, Sigmoid, Softmax",
            "**Optimizer:** memperbarui bobot supaya loss turun — paling populer **Adam**",
            "**CNN:** local connectivity, weight sharing, hierarki fitur",
            ">alur: Konvolusi → ReLU → Pooling → Flatten → Fully Connected → Softmax"], 0.7, 1.5, 12.2, 5.6, 22)

section("Terima Kasih", f"{NAMA}  •  NPM {NPM}",
        "Demikian presentasi dari saya mengenai deep learning dan CNN. Semoga bermanfaat, dan terima kasih "
        "sudah menonton. Wassalamualaikum warahmatullahi wabarakatuh.")

# ---------- simpan ----------
prs.save("presentasi.pptx")
kata = sum(len(n.split()) for _, _, n in transkrip)
with open("transkrip.md", "w") as f:
    f.write("# Transkrip Video — Deep Learning & CNN\n\n"
            f"Total ± {kata} kata → ± {kata // 115}–{kata // 100} menit kalau dibaca pelan (100–115 kata/menit).\n\n")
    for no, judul, isi in transkrip:
        f.write(f"## Slide {no} — {judul}\n\n{isi}\n\n")
print(f"{len(prs.slides)} slide, {kata} kata")
