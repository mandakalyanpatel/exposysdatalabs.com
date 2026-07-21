import os

directory = r'C:\Users\manda\OneDrive\Desktop\New'

old_block = """            <!-- Expertise Links -->
            <div class="footer-col">
                <h3>Our Expertise</h3>
                <ul class="footer-links-list">
                    <li><a href="lance.html">Artificial Intelligence</a></li>
                    <li><a href="lance.html">Machine Learning</a></li>
                    <li><a href="lance.html">Data Science</a></li>
                    <li><a href="Aca1.html">Software Development</a></li>
                    <li><a href="Aca5.html">Web Application Development</a></li>
                    <li><a href="busness.html">Mobile Application Development</a></li>
                    <li><a href="lance.html">Cloud Computing</a></li>
                    <li><a href="lance.html">IoT</a></li>
                    <li><a href="lance.html">Blockchain</a></li>
                    <li><a href="lance.html">Cybersecurity</a></li>
                    <li><a href="fund.html">Research & Development</a></li>
                    <li><a href="lance.html">IT Consultancy</a></li>
                </ul>
            </div>"""

new_block = """            <!-- Expertise Links -->
            <div class="footer-col">
                <h3>Our Expertise</h3>
                <ul class="footer-links-list">
                    <li><a href="lance.html">Artificial Intelligence</a></li>
                    <li><a href="lance.html">Data Science</a></li>
                    <li><a href="Aca1.html">Software Development</a></li>
                    <li><a href="Aca5.html">Web Application Development</a></li>
                    <li><a href="lance.html">Cloud Computing</a></li>
                    <li><a href="fund.html">Research & Development</a></li>
                </ul>
            </div>"""

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if old_block in content:
            new_content = content.replace(old_block, new_block)
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

print("Finished updating expertise links.")
