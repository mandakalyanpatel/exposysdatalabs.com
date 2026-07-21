import re

with open('Aca3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to extract the why-us-section
pattern = r'\s*<section class="why-us-section">.*?</section>'
new_content = re.sub(pattern, '', content, flags=re.DOTALL)

if new_content != content:
    with open('Aca3.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully removed why-us-section from Aca3.html")
else:
    print("Could not find why-us-section in Aca3.html")
