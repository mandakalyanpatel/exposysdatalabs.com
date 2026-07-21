import re

# 1. Extract from Aca1.html
with open('Aca1.html', 'r', encoding='utf-8') as f:
    aca1_content = f.read()

# Pattern to extract the section
pattern = r'(<section class="why-us-section">.*?</section>)'
match = re.search(pattern, aca1_content, flags=re.DOTALL)

if match:
    why_us_html = match.group(1)
    
    # 2. Insert into index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()
        
    # Find insertion point (right before <!-- Integrated Footer -->)
    insertion_point = '    <!-- Integrated Footer -->'
    if insertion_point in index_content:
        new_index_content = index_content.replace(insertion_point, f'    {why_us_html}\n\n{insertion_point}')
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_index_content)
        print("Inserted into index.html")
    
    # 3. Remove from Aca1.html
    new_aca1_content = aca1_content.replace(why_us_html, '')
    with open('Aca1.html', 'w', encoding='utf-8') as f:
        f.write(new_aca1_content)
    print("Removed from Aca1.html")
    
    # 4. Remove from Aca5.html
    with open('Aca5.html', 'r', encoding='utf-8') as f:
        aca5_content = f.read()
    
    # The content might be slightly different in Aca5 (the text), so we use regex to remove any why-us-section
    new_aca5_content = re.sub(pattern, '', aca5_content, flags=re.DOTALL)
    if new_aca5_content != aca5_content:
        with open('Aca5.html', 'w', encoding='utf-8') as f:
            f.write(new_aca5_content)
        print("Removed from Aca5.html")
else:
    print("Could not find why-us-section in Aca1.html")
