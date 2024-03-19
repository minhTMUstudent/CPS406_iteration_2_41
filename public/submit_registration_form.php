<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration - Shops' Salsa Studio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;  
            padding: 25px;      
        }
        .container {
            max-width: 600px;
            border-radius: 6px;
            margin: 0 auto;
            background: #fff;
            padding: 35px;
            box-shadow: 0 5 10px rgba(0, 0, 0, 0.5);
        }
        .container h2 {
            text-align: center;
        }
        .container p {
            margin-bottom: 10px;
        }
        .success {
            color: #0c9e08;
            font-weight: bold;
        }
        .repeat_info {
            text-align: center;
        }
        .error {
            color: #f12700;
            font-weight: bold;
        }
        .error_fix {
            font-weight: bold;
            text-align: center;
        }
        .error_msg {
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <?php
        // Check if the form is submitted
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            // Get the form data
            $firstName = $_POST["firstname"];
            $lastName = $_POST["lastname"];
            $userName = $_POST["username"];
            $email = $_POST["email"];
            $phone = $_POST["phone"];
            $password = $_POST["password"];

            // Validation
            $isValid = true;
            $errorMessage = "";

            // Email validation
            if (filter_var($email, FILTER_VALIDATE_EMAIL) == false) {
                $isValid = false;
                $errorMessage .= "Invalid email format. ";
            }

            // Phone number validation (10 digits)
            if (preg_match("/^\d{10}$/", $phone) == 0 || preg_match("/^\d{10}$/", $phone) == false) {
                $isValid = false;
                $errorMessage .= "Phone number must be 10 digits long. ";
            }

            // Display success message or error message
            if ($isValid) {
                echo "<h2 class='success'>Success! Welcome to Shops' Salsa Studio!</h2>";
                echo "<p class='error_fix'>Here are the details we have for your member account.<br> We look forward to seeing you!</p>";
                echo "<p class='repeat_info'>First Name: $firstName</p>";
                echo "<p class='repeat_info'>Last Name: $lastName</p>";
                echo "<p class='repeat_info'>User Name: $userName</p>";
                echo "<p class='repeat_info'>Email: $email</p>";
                echo "<p class='repeat_info'>Phone Number: $phone</p>";
            } else {
                echo "<h2 class='error'>Registration Failed!</h2>";
                echo "<p class='error_fix'>Please go back to the previous page, fix the errors shown below and try again:</p>";
                echo "<p class='error_msg'>$errorMessage</p>";
            }
        }
        ?>
    </div>
</body>
</html>
