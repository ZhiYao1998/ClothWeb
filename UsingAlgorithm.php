<?php

//$name = $_POST["Name"];
$name = '方志堯';
$type = 11;

$locale = 'en_US.utf-8';
setlocale(LC_ALL, $locale);
putenv('LC_ALL='.$locale);

//$name=escapeshellarg($name);
//$number=escapeshellarg($number);

//Must use " to enclose the string of command.
$result = shell_exec("/var/www/ClothWeb/venv/bin/python3 algorithm.py $name $type");

echo "<pre>";
printf($result);
echo "</pre>";
?>
