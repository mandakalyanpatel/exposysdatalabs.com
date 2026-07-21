import glob
import re
import os

html_files = glob.glob('**/*.html', recursive=True)

for filepath in html_files:
    # Skip workshop directory files if any logic relies on relative paths, but for navbar it's usually fine
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if PROMOTIONS is already added
        if 'class="dropdown-item">PROMOTIONS</a>' in content:
            print(f"PROMOTIONS already in {filepath}. Skipping.")
            continue

        # Look for the TRAINING link in the SERVICES dropdown
        training_pattern = r'(<li>\s*<a\s+href="Aca6\.html"\s+class="dropdown-item">TRAINING</a>\s*</li>)'
        
        if re.search(training_pattern, content):
            # We add PROMOTIONS right after TRAINING
            replacement = r'\1\n                    <li><a href="sms.html" class="dropdown-item">PROMOTIONS</a></li>'
            
            # Since workshop/index.html needs a relative path ../sms.html
            if 'workshop' in filepath:
                 replacement = r'\1\n                    <li><a href="../sms.html" class="dropdown-item">PROMOTIONS</a></li>'

            content = re.sub(training_pattern, replacement, content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filepath}")
        else:
            print(f"TRAINING link not found in {filepath}. Skipping.")

    except Exception as e:
        print(f"Error in {filepath}: {e}")
