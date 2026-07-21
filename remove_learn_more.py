import re

with open('Aca6.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the learn-more-btn tags completely, including leading whitespace
content = re.sub(r'\s*<a href="#" class="learn-more-btn">Learn More <i data-feather="arrow-right" style="width:16px; height:16px;"></i></a>', '', content)

with open('Aca6.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Buttons removed successfully.")
