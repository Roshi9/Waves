<?php
// Replace the values of these variables with your own values
$servername = "localhost";
$username = "Roshi";
$password = "";
$dbname = "waves";

// Create a new connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get the data from the URL
$data = file_get_contents("https://dati.venezia.it/sites/default/files/dataset/opendata/tempacqua.json");

// Decode the JSON data
$jsonData = json_decode($data, true);

// Create the SQL query to insert the data into the MySQL db
$sql = "INSERT INTO temperaturaacqua (ordine, ID_stazione, stazione, nome_abbr, latDMSN, lonDMSE, latDDN, lonDDE, data, valore) VALUES ";

// Loop through the JSON data and create a new set of values for each data item
foreach ($jsonData as $item) {
    $sql .= "('" . $item['ordine'] . "', '" . $item['ID_stazione'] . "', '" . $item['stazione'] . "', '" . $item['nome_abbr'] . "', '" . $item['latDMSN'] . "', '" . $item['lonDMSE'] . "', '" . $item['latDDN'] . "', '" . $item['lonDDE'] . "', '" . $item['data'] . "', '" . $item['valore'] . "'),";
}

// Remove the last comma from the SQL query
$sql = rtrim($sql, ',');

// Execute the SQL query
if ($conn->query($sql) === TRUE) {
    echo "New records created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Get the data from the other URL
$data2 = file_get_contents("https://dati.venezia.it/sites/default/files/dataset/opendata/livello.json");

// Decode the JSON data
$jsonData2 = json_decode($data2, true);

// Create the SQL query to insert the data into the MySQL db
$sql2 = "INSERT INTO livello (ordine, ID_stazione, stazione, nome_abbr, latDMSN, lonDMSE, latDDN, lonDDE, data, valore) VALUES ";

// Loop through the JSON data and create a new set of values for each data item
foreach ($jsonData2 as $item) {
    $sql2 .= "('" . $item['ordine'] . "', '" . $item['ID_stazione'] . "', '" . $item['stazione'] . "', '" . $item['nome_abbr'] . "', '" . $item['latDMSN'] . "', '" . $item['lonDMSE'] . "', '" . $item['latDDN'] . "', '" . $item['lonDDE'] . "', '" . $item['data'] . "', '" . $item['valore'] . "'),";
}

// Remove the last comma from the SQL query
$sql2 = rtrim($sql2, ',');

// Execute the SQL query
if ($conn->query($sql2) === TRUE) {
    echo "New records created successfully";
} else {
    echo "Error: " . $sql2 . "<br>" . $conn->error;
}


// Get the data from the other URL
$data3 = file_get_contents("https://dati.venezia.it/sites/default/files/dataset/opendata/vento.json");

// Decode the JSON data
$jsonData3 = json_decode($data3, true);

// Create the SQL query to insert the data into the MySQL db
$sql3 = "INSERT INTO vento ( ID_stazione, stazione, data, gradi, velocita1, velocita2) VALUES ";

// Loop through the JSON data and create a new set of values for each data item
foreach ($jsonData3 as $item) {
    // Split the "valore" column into three separate columns
    $valoreArray = explode(", ", $item['valore']);

    // Assign the values from the array to the appropriate columns
    $gradi = str_replace(" Gradi", "", $valoreArray[0]);
    $velocita1 = str_replace(" m\/s", "", $valoreArray[1]);
    $velocita2 = str_replace(" m\/s", "", $valoreArray[2]);

    // Add the data to the SQL query
    $sql3 .= "('" . $item['ID_stazione'] . "', '" . $item['stazione'] ."', '" . $item['data'] . "', '" . $gradi . "', '" . $velocita1 . "', '" . $velocita2 . "'),";
}

// Remove the last comma from the SQL query
$sql3 = rtrim($sql3, ',');

// Execute the SQL query
if ($conn->query($sql3) === TRUE) {
    echo "New records created successfully";
} else {
    echo "Error: " . $sql3 . "<br>" . $conn->error;
}
// Get the data from the other URL
$data4 = file_get_contents("https://dati.venezia.it/sites/default/files/dataset/opendata/pressione.json");

// Decode the JSON data
$jsonData4 = json_decode($data4, true);

// Create the SQL query to insert the data into the MySQL db
$sql4 = "INSERT INTO pressione (ordine, ID_stazione, stazione, nome_abbr, latDMSN, lonDMSE, latDDN, lonDDE, data, valore) VALUES ";
// Loop through the JSON data and create a new set of values for each data item
foreach ($jsonData4 as $item) {
    $sql4 .= "('" . $item['ordine'] . "', '" . $item['ID_stazione'] . "', '" . $item['stazione'] . "', '" . $item['nome_abbr'] . "', '" . $item['latDMSN'] . "', '" . $item['lonDMSE'] . "', '" . $item['latDDN'] . "', '" . $item['lonDDE'] . "', '" . $item['data'] . "', '" . $item['valore'] . "'),";
}

// Remove the last comma from the SQL query
$sql4 = rtrim($sql4, ',');

// Execute the SQL query
if ($conn->query($sql4) === TRUE) {
    echo "New records created successfully";
} else {
    echo "Error: " . $sql4 . "<br>" . $conn->error;
}

// Close the connection
$conn->close();
?>