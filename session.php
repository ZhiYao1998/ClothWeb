<?php
//echo $_POST["MyRadio"];
session_start();

$_SESSION['cloth_pant'] = $_POST["MyRadio"];
echo "What we got is: " . $_SESSION['cloth_pant'];
//print_r($_SESSION['cloth_pant']);
if ($_SESSION['cloth_pant']==0){
	header("Location: http://clothweb/cloth.html?cloth_pant=cloth_pant");
	//exit();
}else{
	header("Location: http://clothweb/pant.html?cloth_pant=pant_cloth");
	//exit();
}
?>
