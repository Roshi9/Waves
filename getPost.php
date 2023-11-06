<?php

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
if(array_key_exists('latitude', $_POST) && array_key_exists('longitude', $_POST) && array_key_exists('datetime', $_POST)) {
    $latitude = $_POST['latitude'];
    $longitude = $_POST['longitude'];
    $datetime = $_POST['datetime'];
} else {
    die("Data not set");
}
$sql = "INSERT INTO catture (latitude, longitude, datetime)
VALUES ('$latitude', '$longitude', '$datetime')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>