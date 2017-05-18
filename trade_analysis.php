<!DOCTYPE html>
<html>
<head>
  <title>Movie Trade Analysis</title>
  <link rel="stylesheet" type="text/css" href="trade_analysis.css">
<style media="screen" type="text/css">
.longText {

  white-space : nowrap;
  overflow : hidden;
  outline: none;

  

 }

 .longText:hover {
  overflow : scroll;
  overflow-y: hidden;
  
  z-index: 1;
  
  /*width: 100%;*/
}
</style>

</head>

<body>
<?php 
//echo "I have a color car.";
?>

<?php
$servername = "127.0.0.1:3306";
$username = "root";
$password = "Lmy19940219";
$dbname = "trade_analysis";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT * FROM trade_analysis";
$result = $conn->query($sql);



?>


<section>
  <!--for demo wrap-->

  <h1>Movie Trade Analysis</h1>
  <div class="tbl-header">
    <table cellpadding="0" cellspacing="0" border="0">
      <thead>
        <tr>
          <th>Movie</th>
          <th>Actors</th>
          <th>Director</th>
          <!--<th>Logline</th>-->
          <th>Producer</th>
          <th>Representation</th>
          <th>Development Stage</th>
          <th>Date Published</th>
        </tr>
      </thead>
    </table>
  </div>
  <div class="tbl-content">
    <table cellpadding="0" cellspacing="0" border="0">
      <tbody>
      <?php
      if ($result->num_rows > 0) {
      // output data of each row
        while($row = $result->fetch_assoc()) {
          //echo "movie: " . $row["Title"]. " - Name: " . $row["Title"]. " " . $row["Title"]. "<br>";

          echo "<tr>";
          echo "<td>" . $row['Title'] . "</td>";
          echo "<td>" . $row['Actors'] . "</td>";
          echo "<td>" . $row['Director'] . "</td>";
          //echo "<td class='longText'>" . $row['Logline'] . "</td>";
          echo "<td>" . $row['Producers'] . "</td>";
          echo "<td>" . $row['Representation'] . "</td>";
          echo "<td>" . $row['Development_Stage'] . "</td>";
          echo "<td>" . $row['Date_Published'] . "</td>";
          echo "</tr>";
        }
      } else {
        echo "0 results";
      }
      $conn->close();
?>
      
       
        
      </tbody>
    </table>
  </div>
</section>



  <script>
  

  </script>
</body>
</html>
