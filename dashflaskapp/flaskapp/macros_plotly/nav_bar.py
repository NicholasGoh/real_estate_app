# code to prepend to dash apps to get the nav bar working in dash apps as well, instead of just in flask
nav_bar_template = """
<!DOCTYPE html>
<html lang="en">
<html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    </head>
    <body>
        <nav class="navbar navbar-default">
            <div class="container-fluid">
                <div class="navbar-header">
                    <a class="navbar-brand" href="#">propViewer</a>
                </div>
                <ul class="nav navbar-nav">
                    <li class="active" id='home-btn'><a href="/homepage">Home</a></li>
                    <li id='calculator-btn'><a href=/personal_info>Financial Schemes</a></li>
                    <li id="macros-btn"><a href=/macros/>Macros</a></li>
                    <li id="transactions-btn"><a href=/transactions/>Transactions</a></li>
                </ul>
            </div>
        </nav>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
"""
