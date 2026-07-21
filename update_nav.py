import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Extract the WORKSHOP URL
        workshop_match = re.search(r'<a\s+href="([^"]+)"\s+class="nav-link(\s+active)?">WORKSHOP</a>', content)
        if not workshop_match:
            print(f"WORKSHOP link not found in {filepath}. Skipping.")
            continue
        workshop_url = workshop_match.group(1)

        # 2. Add WORKSHOP to RESEARCH & DEVELOPMENT dropdown
        # The preceding item is CONSULTANCY PROJECTS
        # We need to add it to the dropdown-menu
        consultancy_pattern = r'(<li>\s*<a\s+href="[^"]+"\s+class="dropdown-item">CONSULTANCY PROJECTS</a>\s*</li>)'
        
        # Check if we already added it (idempotency)
        if 'class="dropdown-item">WORKSHOP</a>' not in content:
            replacement = r'\1\n                    <li><a href="{}" class="dropdown-item">WORKSHOP</a></li>'.format(workshop_url)
            content = re.sub(consultancy_pattern, replacement, content)

        # 3. Remove the standalone WORKSHOP tab
        workshop_tab_pattern = r'\s*<li class="nav-item">\s*<a href="[^"]+" class="nav-link(\s+active)?">WORKSHOP</a>\s*</li>'
        content = re.sub(workshop_tab_pattern, '', content)

        # 4. Remove the standalone FREELANCER tab
        freelancer_tab_pattern = r'\s*<li class="nav-item">\s*<a href="[^"]+" class="nav-link(\s+active)?">FREELANCER</a>\s*</li>'
        content = re.sub(freelancer_tab_pattern, '', content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated {filepath}")
    except Exception as e:
        print(f"Error in {filepath}: {e}")
