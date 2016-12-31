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

?>

<link rel="stylesheet" href="all.css">

<div class="header">
 <div class="demo">
    <form class="" action="getresult.php" method="post">
      <input type="text" placeholder="搜尋" name="keyword">
      <input type="submit" value="確認">
    </form>

  </div>


</div>


<div class="container">

<?php


    while($row = $result->fetch_assoc()) {

	echo "<a href='newkeyword/$row[filename]'  >檔案來源$row[filename]</a> <br>" ;


        echo    "<p>".$row["filename"]."content" .$row["content"]." ". " </p><br><br><br><br><br>";
    }
} else {
    echo "<img src='no-result.png'>";
}
$conn->close();
?>


</div>


<style>
    input[type="submit"]{padding:5px 15px; background:#ccc; border:0 none;
cursor:pointer;
-webkit-border-radius: 5px;
border-radius: 5px; }

    input[type="text"]{padding:5px 15px; border:2px black solid;
cursor:pointer;
-webkit-border-radius: 5px;
border-radius: 5px; }

.demo{
    padding-top: 50px;
    text-align: center
}
</style>

