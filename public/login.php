<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user_name = $_POST["username"];
    $password = $_POST["password"];

    // Maybe later we will add code here to query against a dataframe or database

    // One of the three acceptable users currently, need to add querying to database if we want further functionality
    if (($user_name === "treasurer" && $password === "123") || ($user_name === "general" && $password === "abc") || ($user_name === "coach" && $password === "teacher")) {
        
        // if the user_name and password are valid, then go to this other html page which shows a success message
        // Then the user will be redirected to a portal depending on what kind of user is logging in
        header("Location: successful_login.html");

        // Exits the script
        exit();

    } else {
        
        // if the user_name and password are invalid, then go to this other html page which shows an unsuccessful message
        // Then the user will be redirected to the login page to re-enter valid information
        header("Location: unsuccessful_login.html");

        // Exits the script
        exit();
    }
}
?>
