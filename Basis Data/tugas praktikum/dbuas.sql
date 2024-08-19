-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 05 Jun 2024 pada 17.25
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_test`
--

DELIMITER $$
--
-- Prosedur
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetTransaksiByCustomer` (IN `id_customer` VARCHAR(255))   BEGIN
    SELECT 
        transaksi.Id_transaksi,
        transaksi.Tgl_pesan,
        customer.nm_customer,
        makanan.nm_makanan,
        transaksi.Jmlh_makanan,
        makanan.Harga_makanan,
        minuman.nm_minuman,
        minuman.Harga_minuman,
        transaksi.Jmlh_minuman,
        transaksi.Ttl_harga,
        transaksi.Alamat_tujuan
    FROM 
        Transaksi 
    LEFT JOIN customer ON transaksi.id_customer = customer.id_customer 
    LEFT JOIN Makanan ON transaksi.id_makanan = makanan.id_makanan
    LEFT JOIN Minuman ON transaksi.id_minuman = minuman.id_minuman
    WHERE 
        transaksi.id_customer = id_customer;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Struktur dari tabel `customer`
--

CREATE TABLE `customer` (
  `id_customer` int(11) NOT NULL,
  `nm_customer` varchar(100) DEFAULT NULL,
  `alamat_customer` text DEFAULT NULL,
  `kota` varchar(100) DEFAULT NULL,
  `no_tlp` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `customer`
--

INSERT INTO `customer` (`id_customer`, `nm_customer`, `alamat_customer`, `kota`, `no_tlp`, `email`) VALUES
(1, 'John Doe', 'Jl. Sudirman No. 10', 'Jakarta', '081234567890', 'john.doe@example.com'),
(2, 'Jane Smith', 'Jl. Thamrin No. 20', 'Bandung', '081234567891', 'jane.smith@example.com'),
(3, 'Alice Johnson', 'Jl. Merdeka No. 30', 'Surabaya', '081234567892', 'alice.johnson@example.com');

-- --------------------------------------------------------

--
-- Struktur dari tabel `makanan`
--

CREATE TABLE `makanan` (
  `id_makanan` int(11) NOT NULL,
  `id_supplier` int(11) DEFAULT NULL,
  `nm_makanan` varchar(100) DEFAULT NULL,
  `harga_makanan` decimal(10,2) DEFAULT NULL,
  `stok_makanan` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `makanan`
--

INSERT INTO `makanan` (`id_makanan`, `id_supplier`, `nm_makanan`, `harga_makanan`, `stok_makanan`) VALUES
(1, 1, 'Nasi Goreng', 25000.00, 100),
(2, 2, 'Mie Goreng', 20000.00, 199),
(3, 3, 'Ayam Bakar', 30000.00, 150);

-- --------------------------------------------------------

--
-- Struktur dari tabel `minuman`
--

CREATE TABLE `minuman` (
  `id_minuman` int(11) NOT NULL,
  `id_supplier` int(11) DEFAULT NULL,
  `nm_minuman` varchar(100) DEFAULT NULL,
  `harga_minuman` decimal(10,2) DEFAULT NULL,
  `stok_minuman` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `minuman`
--

INSERT INTO `minuman` (`id_minuman`, `id_supplier`, `nm_minuman`, `harga_minuman`, `stok_minuman`) VALUES
(1, 1, 'Teh Manis', 5000.00, 299),
(2, 2, 'Kopi', 10000.00, 200),
(3, 3, 'Jus Jeruk', 15000.00, 100);

--
-- Trigger `minuman`
--
DELIMITER $$
CREATE TRIGGER `reduce_stock_minuman` AFTER INSERT ON `minuman` FOR EACH ROW BEGIN
    UPDATE Minuman
    SET stok_minuman = stok_minuman - NEW.stok_minuman
    WHERE id_minuman = NEW.id_minuman;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Struktur dari tabel `supplier`
--

CREATE TABLE `supplier` (
  `id_supplier` int(11) NOT NULL,
  `nm_supplier` varchar(100) DEFAULT NULL,
  `alamat_supplier` text DEFAULT NULL,
  `kota_supplier` varchar(100) DEFAULT NULL,
  `no_tlp_supplier` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `supplier`
--

INSERT INTO `supplier` (`id_supplier`, `nm_supplier`, `alamat_supplier`, `kota_supplier`, `no_tlp_supplier`) VALUES
(1, 'Supplier A', 'Jl. Industri No. 1', 'Jakarta', '081234567893'),
(2, 'Supplier B', 'Jl. Industri No. 2', 'Bandung', '081234567894'),
(3, 'Supplier C', 'Jl. Industri No. 3', 'Surabaya', '081234567895');

-- --------------------------------------------------------

--
-- Struktur dari tabel `transaksi`
--

CREATE TABLE `transaksi` (
  `id_transaksi` int(11) NOT NULL,
  `id_customer` int(11) DEFAULT NULL,
  `ttl_harga` decimal(10,2) DEFAULT NULL,
  `tgl_pesan` date DEFAULT NULL,
  `tgl_kirim` date DEFAULT NULL,
  `alamat_tujuan` text DEFAULT NULL,
  `kota_tujuan` varchar(100) DEFAULT NULL,
  `id_makanan` int(11) DEFAULT NULL,
  `jmlh_makanan` int(11) DEFAULT NULL,
  `id_minuman` int(11) DEFAULT NULL,
  `jmlh_minuman` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `transaksi`
--

INSERT INTO `transaksi` (`id_transaksi`, `id_customer`, `ttl_harga`, `tgl_pesan`, `tgl_kirim`, `alamat_tujuan`, `kota_tujuan`, `id_makanan`, `jmlh_makanan`, `id_minuman`, `jmlh_minuman`) VALUES
(1, 1, NULL, '2024-06-05', '2024-06-05', 'jakarta', 'magelang', 3, 1, 3, 1),
(2, 2, 20000.00, '2024-06-05', '2024-06-05', 'magelang', 'tmg', 2, 1, 1, 1);

--
-- Trigger `transaksi`
--
DELIMITER $$
CREATE TRIGGER `reduce_stock_transaksi` AFTER INSERT ON `transaksi` FOR EACH ROW BEGIN
    -- Mengurangi stok makanan
    UPDATE Makanan
    SET stok_makanan = stok_makanan - NEW.jmlh_makanan
    WHERE id_makanan = NEW.id_makanan;

    -- Mengurangi stok minuman
    UPDATE Minuman
    SET stok_minuman = stok_minuman - NEW.jmlh_minuman
    WHERE id_minuman = NEW.id_minuman;
END
$$
DELIMITER ;

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id_customer`);

--
-- Indeks untuk tabel `makanan`
--
ALTER TABLE `makanan`
  ADD PRIMARY KEY (`id_makanan`),
  ADD KEY `id_supplier` (`id_supplier`);

--
-- Indeks untuk tabel `minuman`
--
ALTER TABLE `minuman`
  ADD PRIMARY KEY (`id_minuman`),
  ADD KEY `id_supplier` (`id_supplier`);

--
-- Indeks untuk tabel `supplier`
--
ALTER TABLE `supplier`
  ADD PRIMARY KEY (`id_supplier`);

--
-- Indeks untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id_transaksi`),
  ADD KEY `id_customer` (`id_customer`),
  ADD KEY `id_makanan` (`id_makanan`),
  ADD KEY `id_minuman` (`id_minuman`);

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `makanan`
--
ALTER TABLE `makanan`
  ADD CONSTRAINT `makanan_ibfk_1` FOREIGN KEY (`id_supplier`) REFERENCES `supplier` (`id_supplier`);

--
-- Ketidakleluasaan untuk tabel `minuman`
--
ALTER TABLE `minuman`
  ADD CONSTRAINT `minuman_ibfk_1` FOREIGN KEY (`id_supplier`) REFERENCES `supplier` (`id_supplier`);

--
-- Ketidakleluasaan untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  ADD CONSTRAINT `transaksi_ibfk_1` FOREIGN KEY (`id_customer`) REFERENCES `customer` (`id_customer`),
  ADD CONSTRAINT `transaksi_ibfk_2` FOREIGN KEY (`id_makanan`) REFERENCES `makanan` (`id_makanan`),
  ADD CONSTRAINT `transaksi_ibfk_3` FOREIGN KEY (`id_minuman`) REFERENCES `minuman` (`id_minuman`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
