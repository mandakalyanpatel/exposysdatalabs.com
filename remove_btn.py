import glob
import re

files = glob.glob("**/*.html", recursive=True)
for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = re.sub(
            r'class="nav-link btn btn-primary" style="margin-left: 1rem; color: #fff;"',
            r'class="nav-link"',
            content
        )
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

print("Done removing btn class from Contact Us.")
