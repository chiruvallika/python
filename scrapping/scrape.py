from bs4 import BeautifulSoup

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Form</title>
</head>
<body>
    <h1>Sample Form</h1>
    <form id="sample_form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="John Doe"><br><br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" value="john@example.com"><br><br>
        
        <label for="message">Message:</label><br>
        <textarea id="message" name="message">This is a sample message.</textarea><br><br>
        
        <label for="gender">Gender:</label>
        <select id="gender" name="gender">
            <option value="male" selected>Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
        </select><br><br>
        
        <label for="subscribe">Subscribe to newsletter:</label>
        <input type="checkbox" id="subscribe" name="subscribe" checked><br><br>
        
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

soup = BeautifulSoup(html_content, 'html.parser')

form = soup.find('form', {'id': 'sample_form'})

form_data = {}

inputs = form.find_all(['input', 'textarea', 'select'])
print(inputs)
for input_tag in inputs:
    if input_tag.name == 'input':
        input_type = input_tag.get('type', '')
        if input_type == 'submit':
            continue
        input_value = input_tag.get('value', '')
    elif input_tag.name == 'textarea':
        input_value = input_tag.text
    elif input_tag.name == 'select':
        selected_option = input_tag.find('option', {'selected': True})
        input_value = selected_option.text if selected_option else ''
    
    input_name = input_tag.get('name')
    form_data[input_name] = input_value

print(form_data)
