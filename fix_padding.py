import glob
import re

files = glob.glob("**/*.html", recursive=True)
for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the problematic calc() padding
        new_content = re.sub(
            r'padding-top:\s*calc\(var\(--nav-height\)\s*\+\s*6rem\);',
            r'padding-top: 240px;',
            content
        )
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated padding in {filepath}")
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

print("Done updating padding-top across HTML files.")
