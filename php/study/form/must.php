<!-- ������֤������� -->
<?php
$nameErr = $emailErr = $websiteErr = $genderErr = "";
$name = $email = $website = $comment =$gender = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (empty($_POST["name"])){
        $nameErr = "Name is requried!";
    }else {
        $name = test_input($_POST["name"]);
    }
    if (empty($_POST["email"])){
        $emailErr = "email is requried!";
    }else {
        $email = test_input($_POST["email"]);
    }
    if (empty($_POST["website"])){
        $website = "";
    }else {
        $website = test_input($_POST["website"]);
    }
    if (empty($_POST["comment"])){
        $comment = "";
    }else {
        $comment = test_input($_POST["comment"]);
    }
    if (empty($_POST["gender"])){
        $genderErr = "gender is requried!";
    }else {
        $gender = test_input($_POST["gender"]);
    }
}

function test_input($data){
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}
?>
<!DOCTYPE html>
<html>
<body>
	<!-- ������֤ -->
	<h1>PHP������֤</h1>
	<p>*�����ֶ�</p>
	<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
	����:
		<input type="text" name="name">
		<span class="error">* <?php echo $nameErr;?> </span>
		<br><br>
	�ʼ�:
        <input type="text" name="email">
        <span class="error">* <?php echo $emailErr;?> </span>
        <br><br> 
	��վ:
        <input type="text" name="website">
        <span class="error"><?php echo $websiteErr;?> </span>
        <br><br>
	<label>����:
        <textarea name="comment" rows="5" clos="40"></textarea>
        <br><br>
	�Ա�:
        <input type="radio" name="gender" value="man">���� 
		<input type="radio" name="gender" value="woman">Ů��
		<span class="error">* <?php echo $genderErr;?> </span>
		<br><br> 
		<input type="submit">
	</form>
</body>
</html>
