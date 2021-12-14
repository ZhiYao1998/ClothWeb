<?php
	session_start();
	$var = $_SESSION["cloth_pant"];
	echo "what we got is: ". $var;
	echo $_POST["Name"];
	echo $_POST["Type"];
?>
