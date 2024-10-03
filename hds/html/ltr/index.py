#!C:\Python312\python.exe
import header
print(header.homehtml)
print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hearing Test</title>
    <link rel="stylesheet">
</head>
<body>
    <h1>Hearing Test</h1>
    <form action="display_test.py" method="post">
        <label for="age_group">Select Age Group:</label><br>
        <select id="age_group" name="age_group" required>
            <option value="child">Child</option>
            <option value="adult">Adult</option>
            <option value="senior">Senior</option>
        </select><br><br>
        
        <input type="submit" value="Start Test">
    </form>
</body>
</html>
''')