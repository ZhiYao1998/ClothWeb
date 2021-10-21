<?php
$cloth=$_POST["Cloth"];
$color=$_POST["Color"];
$shade=$_POST["Shade"];
$pant=$_POST["Pant"];
$color2=$_POST["Color2"];
$shade2=$_POST["Shade2"];

$servername = "localhost";
$username = "root";
$password = "";

try {
  $conn = new PDO("mysql:host=$servername;dbname=clothweb", $username, $password);
  // set the PDO error mode to exception
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  echo "Connected successfully"."<br>";

  $sql = "INSERT INTO cloth (cloth,color,shade,pant,color2,shade2) 
  VALUES ('$cloth','$color','$shade','$pant','$color2','$shade2')";
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