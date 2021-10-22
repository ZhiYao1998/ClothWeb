<?php
$checkbox_select=$_POST["Color"];

$conn=new mysqli('localhost','root','','clothweb');

if (mysqli_connect_error()) {
	die("Database connection failed: " . mysqli_connect_error());
}else{
	echo "Connected Successfully";
	
	$stmt=$conn->prepare("INSERT INTO color(color1,color2,color3,color4,color5,color6,color7,color8,color9,color10,color11,color12) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)");
	$stmt->bind_param("iiiiiiiiiiii",$checkbox_select[0],$checkbox_select[1],$checkbox_select[2],$checkbox_select[3],$checkbox_select[4],$checkbox_select[5],$checkbox_select[6],$checkbox_select[7],$checkbox_select[8],$checkbox_select[9],$checkbox_select[10],$checkbox_select[11]);
	$stmt->execute();
	$stmt->close();
	$conn->close();
	//
}

/* if($conn->connect_error){
	die('Connect Failed :'.$conn->connect_error);	
}else{

	echo "Connected Successfully";
	
	$stmt=$conn->prepare("INSERT INTO color(color1,color2,color3,color4,color5,color6,color7,color8,color9,color10,color11,color12) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)");
	$stmt->bind_param("iiiiiiiiiiii",$checkbox_select[0],$checkbox_select[1],$checkbox_select[2],$checkbox_select[3],$checkbox_select[4],$checkbox_select[5],$checkbox_select[6],$checkbox_select[7],$checkbox_select[8],$checkbox_select[9],$checkbox_select[10],$checkbox_select[11]);
	$stmt->execute();
	echo "success";
	$stmt->close();
	$conn->close(); */
	
	
	
	/* $sql = 'INSERT INTO color(color1,color2,color3,color4,color5,color6,color7,color8,color9,color10,color11,color12) 
	VALUES($checkbox_select[0], $checkbox_select[1], $checkbox_select[2], $checkbox_select[3], $checkbox_select[4], $checkbox_select[5], $checkbox_select[6], $checkbox_select[7], $checkbox_select[8], $checkbox_select[9], $checkbox_select[10], $checkbox_select[11])';
	if (mysqli_query($conn, $sql)) {
		echo "New record created successfully";
	  } else {
		echo "Error: " . $sql . "<br>" . mysqli_error($conn);
	  }
	  
	  mysqli_close($conn); */
	





/*for($i=0;$i<count($checkbox_select);$i++)
{
echo "選項".$checkbox_select[$i]."被選中<br />";
}*/
?>