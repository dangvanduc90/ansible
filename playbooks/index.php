<?php
$servername = "10.10.20.113";
$username = "ducdv_dev";
$password = "cECEw&heCH7cron7SAsi";

try {
  $conn = new PDO("mysql:host=$servername;dbname=9prints_master_fog", $username, $password);
  // set the PDO error mode to exception
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  echo "Connected successfully";
} catch(PDOException $e) {
  echo "Connection failed: " . $e->getMessage();
}
?>