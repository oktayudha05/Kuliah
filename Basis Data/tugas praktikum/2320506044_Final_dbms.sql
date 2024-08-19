-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 06, 2024 at 06:28 PM
-- Server version: 8.0.36-0ubuntu0.22.04.1
-- PHP Version: 8.1.2-1ubuntu2.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `2320506044_Final_dbms`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetTransaksiByCustomer` (IN `id_customer` VARCHAR(255))  BEGIN
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
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id_customer` int NOT NULL,
  `nm_customer` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `alamat_customer` text COLLATE utf8mb4_general_ci,
  `kota` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `no_tlp` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id_customer`, `nm_customer`, `alamat_customer`, `kota`, `no_tlp`, `email`) VALUES
(1, 'Agus Separatis', 'Jl. Sudimara No. 10', 'Ngawi', '081234567890', 'ikan@gmail.com'),
(2, 'Rofik Destroyer', 'Jl. Thamrin No. 20', 'Bandung', '081234567891', 'kapalKaram@gmail.com'),
(3, 'Bambang Slap Slup', 'Jl. Merdeka No. 30', 'Surabaya', '081234567892', 'jaya@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `makanan`
--

CREATE TABLE `makanan` (
  `id_makanan` int NOT NULL,
  `id_supplier` int DEFAULT NULL,
  `nm_makanan` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `harga_makanan` decimal(10,2) DEFAULT NULL,
  `stok_makanan` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `makanan`
--

INSERT INTO `makanan` (`id_makanan`, `id_supplier`, `nm_makanan`, `harga_makanan`, `stok_makanan`) VALUES
(1, 1, 'Nasi Garam', '25000.00', 10),
(2, 2, 'Mie Kecap', '20000.00', 197),
(3, 3, 'Nasi Kering', '30000.00', 150);

-- --------------------------------------------------------

--
-- Table structure for table `minuman`
--

CREATE TABLE `minuman` (
  `id_minuman` int NOT NULL,
  `id_supplier` int DEFAULT NULL,
  `nm_minuman` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `harga_minuman` decimal(10,2) DEFAULT NULL,
  `stok_minuman` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `minuman`
--

INSERT INTO `minuman` (`id_minuman`, `id_supplier`, `nm_minuman`, `harga_minuman`, `stok_minuman`) VALUES
(1, 1, 'Teajus', '5000.00', 100),
(2, 2, 'Jasjus', '1000.00', 50),
(3, 3, 'Air Bening', '15000.00', 100);

-- --------------------------------------------------------

--
-- Table structure for table `supplier`
--

CREATE TABLE `supplier` (
  `id_supplier` int NOT NULL,
  `nm_supplier` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `alamat_supplier` text COLLATE utf8mb4_general_ci,
  `kota_supplier` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `no_tlp_supplier` varchar(15) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `supplier`
--

INSERT INTO `supplier` (`id_supplier`, `nm_supplier`, `alamat_supplier`, `kota_supplier`, `no_tlp_supplier`) VALUES
(1, 'PT PETE', 'Jl. Jalan No. 1', 'Malegang', '081234567893'),
(2, 'PT. Mencari Cinta Sejati', 'Jl. Jalan No. 6', 'Ngawi', '03284322'),
(3, 'PT. Agus Makmur Abadi', 'Jl. Kaki No. 3', 'Purojewo', '08324232');

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

CREATE TABLE `transaksi` (
  `id_transaksi` int NOT NULL,
  `id_customer` int DEFAULT NULL,
  `ttl_harga` decimal(10,2) DEFAULT NULL,
  `tgl_pesan` date DEFAULT NULL,
  `tgl_kirim` date DEFAULT NULL,
  `alamat_tujuan` text COLLATE utf8mb4_general_ci,
  `kota_tujuan` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `id_makanan` int DEFAULT NULL,
  `jmlh_makanan` int DEFAULT NULL,
  `id_minuman` int DEFAULT NULL,
  `jmlh_minuman` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transaksi`
--

INSERT INTO `transaksi` (`id_transaksi`, `id_customer`, `ttl_harga`, `tgl_pesan`, `tgl_kirim`, `alamat_tujuan`, `kota_tujuan`, `id_makanan`, `jmlh_makanan`, `id_minuman`, `jmlh_minuman`) VALUES
(1, 1, '15000.00', '2024-06-06', '2024-06-06', 'Ikan', 'Jauh', 3, 1, 3, 1),
(2, 2, '20000.00', '2024-06-06', '2024-06-06', 'Belakang', 'Seramang', 2, 1, 1, 1);

--
-- Triggers `transaksi`
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
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id_customer`);

--
-- Indexes for table `makanan`
--
ALTER TABLE `makanan`
  ADD PRIMARY KEY (`id_makanan`),
  ADD KEY `id_supplier` (`id_supplier`);

--
-- Indexes for table `minuman`
--
ALTER TABLE `minuman`
  ADD PRIMARY KEY (`id_minuman`),
  ADD KEY `id_supplier` (`id_supplier`);

--
-- Indexes for table `supplier`
--
ALTER TABLE `supplier`
  ADD PRIMARY KEY (`id_supplier`);

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id_transaksi`),
  ADD KEY `id_customer` (`id_customer`),
  ADD KEY `id_makanan` (`id_makanan`),
  ADD KEY `id_minuman` (`id_minuman`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `makanan`
--
ALTER TABLE `makanan`
  ADD CONSTRAINT `makanan_ibfk_1` FOREIGN KEY (`id_supplier`) REFERENCES `supplier` (`id_supplier`);

--
-- Constraints for table `minuman`
--
ALTER TABLE `minuman`
  ADD CONSTRAINT `minuman_ibfk_1` FOREIGN KEY (`id_supplier`) REFERENCES `supplier` (`id_supplier`);

--
-- Constraints for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD CONSTRAINT `transaksi_ibfk_1` FOREIGN KEY (`id_customer`) REFERENCES `customer` (`id_customer`),
  ADD CONSTRAINT `transaksi_ibfk_2` FOREIGN KEY (`id_makanan`) REFERENCES `makanan` (`id_makanan`),
  ADD CONSTRAINT `transaksi_ibfk_3` FOREIGN KEY (`id_minuman`) REFERENCES `minuman` (`id_minuman`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
