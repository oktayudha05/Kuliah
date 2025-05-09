<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet"/>

    <style>
    .hero-section {
        position: relative;
        background-image: url('img/bg-lp.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
    }

    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.5);
    }

    .hero-content {
        position: relative;
        z-index: 1;
    }
    </style>
</head>
<body>
    

  <!-- navbar -->
  <div class="bg-white shadow-md p-4 flex justify-between items-center">
    <div class="flex gap-2">
      <div class="text-2xl font-bold">Oktayur</div>
    </div>
    <div class="flex w-1/3 items-center gap-2">
      <input type="text" placeholder="Cari Produk" class="w-full p-2 shadow-md border rounded-full">
      <i class="fas fa-search left-3 top-3 text-gray-500"></i>
    </div>
    <div class="flex items-center space-x-4">
        <a href="/penjual/login.html"><button class="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded font-bold">
            Mitra Oktayur
        </button></a>
    </div>
  </div>

    <!-- Hero Section -->
    <section class="hero-section">
        <div class="container mx-auto h-full flex items-center justify-center">
            <div class="hero-content text-center text-white">
                <h1 class="text-5xl text-green-100 font-bold mb-2">OKTAYUR</h1>
                <p class="text-xl text-green-100 mb-2">Dapurmu butuh sayurku!</p>
                <a href="daftarProduk.html" ><button class="bg-green-500 text-white px-4 py-2 rounded-xl hover:bg-green-600">Mulai Berbelanja</button></a>
                
            </div>
        </div>
    </section>
</body>
</html>