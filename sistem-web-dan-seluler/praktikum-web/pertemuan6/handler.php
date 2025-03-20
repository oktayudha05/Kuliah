<?php 
include 'koneksi.php';

$username = $_POST['username'];
$nama_toko = $_POST['nama_toko'];
$alamat = $_POST['alamat'];

$query = "INSERT INTO penjual (username, nama_toko, alamat) VALUES ('$username', '$nama_toko', '$alamat')";
mysqli_query($koneksi, $query) or die(mysqli_error($koneksi));
?>