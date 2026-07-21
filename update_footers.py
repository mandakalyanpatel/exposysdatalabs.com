import os
import re

new_footer_root = """    <!-- Global Premium Footer -->
    <footer class="global-footer reveal">
        <div class="footer-grid">
            <!-- Branding -->
            <div class="footer-col footer-branding">
                <h3>Exposys Data Labs</h3>
                <p><strong>"Empowering Innovation Through Technology"</strong></p>
                <p>Exposys Data Labs is a technology-driven company specializing in Artificial Intelligence, Machine Learning, Data Science, Software Development, Cloud Computing, IoT, Blockchain, Cybersecurity, Research & Development, and IT Consultancy. We help businesses, startups, educational institutions, and enterprises build innovative digital solutions.</p>
            </div>
            
            <!-- Expertise Links -->
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
            </div>
            
            <!-- Contact Info -->
            <div class="footer-col">
                <h3>Contact Us</h3>
                
                <div class="footer-contact-item">
                    <i data-feather="phone"></i>
                    <a href="tel:+917795207065">+91 77952 07065</a>
                </div>
                
                <div class="footer-contact-item">
                    <i data-feather="mail"></i>
                    <a href="mailto:hr@exposysdata.com">hr@exposysdata.com</a>
                </div>
                
                <div class="footer-contact-item">
                    <i data-feather="map-pin"></i>
                    <a href="https://maps.google.com/?q=4th+Floor,+YVR+Cave,+56,+Kakolu+Road,+Yelahanka,+Rajanukunte,+Bengaluru,+Karnataka+560064" target="_blank" rel="noopener noreferrer">
                        4th Floor, YVR Cave,<br>
                        56, Kakolu Road, Yelahanka,<br>
                        Rajanukunte, Bengaluru,<br>
                        Karnataka 560064
                    </a>
                </div>
                
                <div class="footer-contact-item">
                    <i data-feather="clock"></i>
                    <p>Monday – Saturday<br>9:00 AM – 6:00 PM</p>
                </div>
            </div>
            
            <!-- Follow Us -->
            <div class="footer-col">
                <h3>Follow Us</h3>
                <div class="footer-social">
                    <a href="https://www.facebook.com/share/17LaBwfMkF/" target="_blank" rel="noopener noreferrer" class="footer-social-btn" aria-label="Facebook">
                        <i data-feather="facebook"></i>
                    </a>
                    <a href="https://www.instagram.com/exposysdatalabs?igsh=M3YwN3dwMm8xNG1s" target="_blank" rel="noopener noreferrer" class="footer-social-btn" aria-label="Instagram">
                        <i data-feather="instagram"></i>
                    </a>
                    <a href="https://www.linkedin.com/company/upchat-technologies/" target="_blank" rel="noopener noreferrer" class="footer-social-btn" aria-label="LinkedIn">
                        <i data-feather="linkedin"></i>
                    </a>
                    <a href="https://x.com/ExposysDataLabs" target="_blank" rel="noopener noreferrer" class="footer-social-btn" aria-label="Twitter">
                        <i data-feather="twitter"></i>
                    </a>
                    <a href="https://youtube.com/@exposysdatalabs4156?si=uMDS8_tzNH32xUF7" target="_blank" rel="noopener noreferrer" class="footer-social-btn" aria-label="YouTube">
                        <i data-feather="youtube"></i>
                    </a>
                </div>
            </div>
        </div>
        
        <!-- Bottom Footer -->
        <div class="footer-bottom">
            <p>© 2026 Exposys Data Labs. All Rights Reserved.</p>
            <div class="footer-legal-links">
                <a href="privacy-policy.html">Privacy Policy</a>
                <a href="terms-and-conditions.html">Terms & Conditions</a>
                <a href="terms-and-conditions.html#disclaimer">Disclaimer</a>
            </div>
        </div>
    </footer>"""

new_footer_sub = new_footer_root.replace('href="', 'href="../')
# Fix external links which got corrupted
new_footer_sub = new_footer_sub.replace('href="../tel:', 'href="tel:')
new_footer_sub = new_footer_sub.replace('href="../mailto:', 'href="mailto:')
new_footer_sub = new_footer_sub.replace('href="../https://', 'href="https://')
new_footer_sub = new_footer_sub.replace('href="../#', 'href="#')

def replace_footer_in_file(filepath, is_sub=False):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        footer_to_use = new_footer_sub if is_sub else new_footer_root
        
        # Regex to find existing footer
        # Matches <footer ...> ... </footer>
        new_content = re.sub(r'<footer.*?</footer>', footer_to_use, content, flags=re.DOTALL)
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {filepath}")
    except Exception as e:
        print(f"Error updating {filepath}: {e}")

if __name__ == '__main__':
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                # Skip templates or unrelated stuff if necessary, but we want all.
                is_sub = 'workshop' in root
                replace_footer_in_file(filepath, is_sub)
