import os

directory = r'C:\Users\manda\OneDrive\Desktop\New'
target_text = '© 2026 Exposys Data Labs. All Rights Reserved.'
replacement_text = '© 2019 Exposys Data Labs. All Rights Reserved.'

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if target_text in content:
            new_content = content.replace(target_text, replacement_text)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {filepath}')
    except Exception as e:
        print(f'Error processing {filepath}: {e}')

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            replace_in_file(filepath)

print("Finished updating copyright year.")
