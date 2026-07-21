import os
import re

directory = r'C:\Users\manda\OneDrive\Desktop\New'

# Regex to capture the HOME block
# Group 1 is the HOME block
home_pattern = re.compile(r'(<li class="nav-item">\s*<a href="index\.html" class="nav-link[^>]*>HOME</a>\s*</li>)', re.DOTALL)

# Regex to capture the ABOUT US block
# Group 1 is the ABOUT US block
about_pattern = re.compile(r'(\s*<li class="nav-item">\s*<a href="#" class="nav-link[^>]*>ABOUT US <i data-feather="chevron-down"[^>]*></i></a>\s*<ul class="dropdown-menu">\s*<li><a href="about-us\.html" class="dropdown-item">ABOUT US</a></li>\s*<li><a href="team\.html" class="dropdown-item">TEAM</a></li>\s*</ul>\s*</li>)', re.DOTALL)

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # If it has both blocks
        if home_pattern.search(content) and about_pattern.search(content):
            # Check if ABOUT US is already right after HOME
            home_match = home_pattern.search(content)
            about_match = about_pattern.search(content)
            
            # Remove the ABOUT US block from its current location
            new_content = about_pattern.sub('', content)
            
            # Insert the ABOUT US block right after the HOME block
            # Re-search home in the new content
            home_match_new = home_pattern.search(new_content)
            if home_match_new:
                insertion_point = home_match_new.end()
                about_block = about_match.group(1)
                
                final_content = new_content[:insertion_point] + about_block + new_content[insertion_point:]
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(final_content)
                print(f'Updated {filepath}')
    except Exception as e:
        print(f'Error processing {filepath}: {e}')

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            process_file(filepath)

print("Finished reordering nav.")
