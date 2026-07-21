import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to match the entire PROMOTIONS nav block
        promotions_pattern = r'\s*<li class="nav-item">\s*<a href="#" class="nav-link">PROMOTIONS <i[^>]+></i></a>\s*<ul class="dropdown-menu">\s*<li><a href="[^"]+" class="dropdown-item">PROMOTIONS</a></li>\s*</ul>\s*</li>'
        
        new_content = re.sub(promotions_pattern, '', content)

        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Removed PROMOTIONS from {filepath}")
    except Exception as e:
        print(f"Error in {filepath}: {e}")
