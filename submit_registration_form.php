<?php
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the form data
    $firstname = $_POST["firstname"];
    $lastname = $_POST["lastname"];
    $username = $_POST["username"];
    $email = $_POST["email"];
    $phone = $_POST["phone"];
    $password = $_POST["password"];

    // Here, you can perform further validation or database operations as needed

    // For demonstration purposes, let's just display the received data
    echo "<h2>Success! Welcome to Shops' Salsa Studio!</h2>";
    echo "<p>First Name: $firstname</p>";
    echo "<p>Last Name: $lastname</p>";
    echo "<p>User Name: $username</p>";
    echo "<p>Email: $email</p>";
    echo "<p>Phone Number: $phone</p>";

    // Security Note: In a real application, make sure to handle the password securely (e.g., hashing it) before storing it in the database
}
?>
