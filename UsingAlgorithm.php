<?php

$name = $_POST["Name"];
//print(phpinfo());
//$hello = 'world';
//echo getcwd() . "<br>";
//print(shell_exec("sudo apache2 -v"));
//$result = shell_exec('python algorithm.py 方韋傑');
// C:\Users\sappa\AppData\Local\Microsoft\WindowsApps\python.exe
// D:\Program_Files\xampp\htdocs\ClothWeb\algorithm.py
$result = shell_exec('python algorithm.py 方韋傑');

printf($result);
//system('ls > output.txt');
/* $command = 'python algorithm.py 方志堯';
$output = shell_exec($command);
echo $output; */
//passthru($command, $name);
/* $result = passthru('python algorithm.py 方志堯 ');
print($result); */
//printf($name);
printf("This file did run.");

//$path="python algorithm.py "; //需要注意的是：末尾要加一个空格

//passthru($path, $name);//等同于命令`python python.py 参数`，并接收打印出来的信息

?>