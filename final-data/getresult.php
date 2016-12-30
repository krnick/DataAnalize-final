<?php


$keyword=$_POST['keyword'];


$servername = "localhost";
$username = "root";
$password = "krnick";
$dbname = "DataMining";
$v=0;
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
mysqli_query($conn,"SET NAMES utf8");
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT filename,content  FROM file";
$newsql="SELECT k.filename as keywordname ,k.key_word,k.value,k.tf,k.tf_idf,f.filename as filename,f.content 
FROM keyword as k ,file as f
WHERE k.key_word  like '%$keyword%'
AND SUBSTRING( k.filename, 1,8)=SUBSTRING( f.filename, 1,8)
ORDER BY k.tf_idf DESC";




$result = $conn->query($newsql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {

	echo "<a href='newkeyword/$row[filename]'  >檔案來源$row[filename]</a> <br>" ;


        echo    "<p>".$row["filename"]."content" .$row["content"]." ". " </p><br><br><br><br><br>";
    }
} else {
    echo "0 results";
}
$conn->close();




?>
