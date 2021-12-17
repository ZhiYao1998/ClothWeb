<?php
session_start();
$flag = $_SESSION["cloth_pant"];
$name = $_POST["Name"];
$type = $_POST["Type"];
$color = $_POST["Color"];
$shade = $_POST["Shade"];
//$flag = $_POST["Flag"];

//$name = '方志堯';
//$type = 11;
//$flag = 0;

$locale = 'en_US.utf-8';
setlocale(LC_ALL, $locale);
putenv('LC_ALL='.$locale);

//$name=escapeshellarg($name);
//$number=escapeshellarg($number);

//Must use " to enclose the string of command.
$result = shell_exec("/var/www/ClothWeb/venv/bin/python3 algorithm_alter2.py $name $type $flag $color $shade ");

echo "<pre>";
printf($result);
echo "</pre>";
?>
