-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 06, 2024 at 08:54 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `2340506065_final_dbms`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `TransaksiCustomer` (IN `id_customer` INT(255))   BEGIN
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
  `id_customer` int(11) NOT NULL,
  `nm_customer` varchar(100) DEFAULT NULL,
  `alamat_customer` text DEFAULT NULL,
  `kota` varchar(100) DEFAULT NULL,
  `no_tlp` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id_customer`, `nm_customer`, `alamat_customer`, `kota`, `no_tlp`, `email`) VALUES
(1, 'Amano', 'Jl. Tokyo No. 10', 'Jakarta', '081234567890', 'amano@gmail.com'),
(2, 'Kurt Cobain', 'Jl. Seattle No. 20', 'Bandung', '081234567891', 'kurt.cobain@gmail.com'),
(3, 'John Lennon', 'Jl. Liverpool No. 30', 'Surabaya', '081234567892', 'lennon@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `makanan`
--

CREATE TABLE `makanan` (
  `id_makanan` int(11) NOT NULL,
  `id_supplier` int(11) DEFAULT NULL,
  `nm_makanan` varchar(100) DEFAULT NULL,
  `harga_makanan` decimal(10,2) DEFAULT NULL,
  `stok_makanan` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `makanan`
--

INSERT INTO `makanan` (`id_makanan`, `id_supplier`, `nm_makanan`, `harga_makanan`, `stok_makanan`) VALUES
(1, 1, 'Nasi Goreng', 14000.00, 98),
(2, 2, 'Nasi Kering', 5000.00, 199),
(3, 3, 'Ayam Gosong', 50000.00, 147);

-- --------------------------------------------------------

--
-- Table structure for table `minuman`
--

CREATE TABLE `minuman` (
  `id_minuman` int(11) NOT NULL,
  `id_supplier` int(11) DEFAULT NULL,
  `nm_minuman` varchar(100) DEFAULT NULL,
  `harga_minuman` decimal(10,2) DEFAULT NULL,
  `stok_minuman` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `minuman`
--

INSERT INTO `minuman` (`id_minuman`, `id_supplier`, `nm_minuman`, `harga_minuman`, `stok_minuman`) VALUES
(1, 1, 'Teh Comberan', 50000.00, 299),
(2, 2, 'Kopi Kluwek', 30000.00, 192),
(3, 3, 'Jus Kecubung', 69000.00, 97);

-- --------------------------------------------------------

--
-- Table structure for table `supplier`
--

CREATE TABLE `supplier` (
  `id_supplier` int(11) NOT NULL,
  `nm_supplier` varchar(100) DEFAULT NULL,
  `alamat_supplier` text DEFAULT NULL,
  `kota_supplier` varchar(100) DEFAULT NULL,
  `no_tlp_supplier` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `supplier`
--

INSERT INTO `supplier` (`id_supplier`, `nm_supplier`, `alamat_supplier`, `kota_supplier`, `no_tlp_supplier`) VALUES
(1, 'Supplier 1', 'Jl. Bermuda No. 1', 'Segitiga', '081234567893'),
(2, 'Supplier 2', 'Jl. Bekasi No. 2', 'Panas', '081234567894'),
(3, 'Supplier 3', 'Jl. Purbalingga No. 3', 'Kalimanah', '081234567895');

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
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
-- Dumping data for table `transaksi`
--

INSERT INTO `transaksi` (`id_transaksi`, `id_customer`, `ttl_harga`, `tgl_pesan`, `tgl_kirim`, `alamat_tujuan`, `kota_tujuan`, `id_makanan`, `jmlh_makanan`, `id_minuman`, `jmlh_minuman`) VALUES
(0, 3, 30000.00, '2024-06-06', '2024-06-06', 'Disitu', 'Kota sono', 3, 1, 2, 2),
(1, 1, NULL, '2024-06-05', '2024-06-05', 'jakarta', 'magelang', 3, 1, 3, 1),
(2, 2, 20000.00, '2024-06-05', '2024-06-05', 'magelang', 'tmg', 2, 1, 1, 1),
(3, 3, 30000.00, '2024-06-06', '2024-06-06', 'Disitu', 'Kota sono', 3, 1, 2, 2),
(4, 2, 20000.00, '2024-06-06', '2024-06-06', 'situ', 'Seattle', 1, 2, 3, 3),
(5, 2, 69000.00, '2024-06-06', '2024-06-06', 'Sprung', 'Seattle', 3, 1, 2, 4);

--
-- Triggers `transaksi`
--
DELIMITER $$
CREATE TRIGGER `transaksi` AFTER INSERT ON `transaksi` FOR EACH ROW BEGIN
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
