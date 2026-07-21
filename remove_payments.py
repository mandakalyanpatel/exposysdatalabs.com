import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to match the ONLINE PAYMENTS nav block
        payments_pattern = r'\s*<li class="nav-item">\s*<a href="[^"]+" class="nav-link">ONLINE PAYMENTS</a>\s*</li>'
        
        new_content = re.sub(payments_pattern, '', content)

        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Removed ONLINE PAYMENTS from {filepath}")
    except Exception as e:
        print(f"Error in {filepath}: {e}")
