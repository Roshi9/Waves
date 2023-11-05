<?php
include 'db_connect.php';

$servername = "localhost";
$username = "Roshi";
$password = "";
$dbname = "waves";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$latitude = $_POST['latitude'];
$longitude = $_POST['longitude'];
$datetime = $_POST['datetime'];

$sql = "INSERT INTO catture (latDDN, lonDDE, data)
VALUES ('$latitude', '$longitude', '$datetime')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>