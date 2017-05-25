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

?>


<section>
  <!--for demo wrap-->

  <h1>Movie Trade Analysis</h1>

  <form action='<?php echo $_SERVER['PHP_SELF']; ?>' method='post' name='form_filter' >

    <select name="value">
        <option value="all">All</option>
        <option value="Open">Open for acquisition</option>
        <option value="Acquired">Acquired</option>
    </select>
  
    <br />
  
    <input type='submit' value = 'Filter'>

</form>


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

      if(!$_POST){
        $query = "SELECT * FROM trade_analysis";
      }else{
        if($_POST['value'] == 'Open') {
    // query to get all Fitzgerald records
        $query = "SELECT * FROM trade_analysis WHERE Development_Stage='Open for acquisition'";

      }
      elseif($_POST['value'] == 'Acquired') {
    // query to get all Herring records
        $query = "SELECT * FROM trade_analysis WHERE Development_Stage='Acquired'";
      } else {
    // query to get all records
        $query = "SELECT * FROM trade_analysis";
      }
      }

      


      #$sql = "SELECT * FROM trade_analysis";
      $sql = $query;
      $result = $conn->query($sql);


      if ($result->num_rows > 0) {
      // output data of each row
        while($row = $result->fetch_assoc()) {
          //echo "movie: " . $row["Title"]. " - Name: " . $row["Title"]. " " . $row["Title"]. "<br>";

          echo "<tr>";
          echo "<td>" . $row['Title'] . "</td>";
          if ($row['Actors'] == ""){
            echo "<td>" . "Not Found" . "</td>";
          }else{
            echo "<td>" . $row['Actors'] . "</td>";
          }

          if ($row['Director'] == ""){
            echo "<td>" . "Not Found" . "</td>";
          }else{
            echo "<td>" . $row['Director'] . "</td>";
          }

          if ($row['Producers'] == ""){
            echo "<td>" . "Not Found" . "</td>";
          }else{
            echo "<td>" . $row['Producers'] . "</td>";
          }

          if ($row['Representation'] == ""){
            echo "<td>" . "Not Available" . "</td>";
          }else{
            echo "<td>" . $row['Representation'] . "</td>";
          }
          
          //echo "<td class='longText'>" . $row['Logline'] . "</td>";
          
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
