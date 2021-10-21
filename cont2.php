<?php
$checkbox_select=$_POST["Color"];

$servername = "localhost";
$username = "root";
$password = "";

try {
  $conn = new PDO("mysql:host=$servername;dbname=clothweb", $username, $password);
  // set the PDO error mode to exception
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  echo "Connected successfully"."<br>";

  $sql = "INSERT INTO color (color1,color2,color3,color4,color5,color6,color7,color8,color9,color10,color11,color12) 
  VALUES ('$checkbox_select[0]','$checkbox_select[1]','$checkbox_select[2]','$checkbox_select[3]','$checkbox_select[4]','$checkbox_select[5]','$checkbox_select[6]','$checkbox_select[7]','$checkbox_select[8]','$checkbox_select[9]','$checkbox_select[10]','$checkbox_select[11]')";
  // use exec() because no results are returned
  $conn->exec($sql);
  //echo "New record created successfully";

  $last_id = $conn->lastInsertId();
  echo "New record created successfully."."<br>". "Last inserted ID is: " . $last_id;
} catch(PDOException $e) {
  echo "Connection failed: " . $e->getMessage();
}

$conn = null;
?>