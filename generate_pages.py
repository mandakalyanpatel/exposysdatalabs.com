import os
import re

base_file = "Aca5.html"

with open(base_file, 'r', encoding='utf-8') as f:
    template = f.read()

pages = [
    {
        "filename": "Aca1.html",
        "title": "Software Development",
        "subtitle": "Custom Software Engineering",
        "desc": "We build robust, scalable, and secure software applications tailored to meet your unique business requirements."
    },
    {
        "filename": "Aca3.html",
        "title": "IT Outsource Services",
        "subtitle": "Strategic Partnership",
        "desc": "Leverage our extensive pool of IT talent and infrastructure. From managed services to staff augmentation."
    },
    {
        "filename": "internship.html",
        "title": "Internships",
        "subtitle": "Online & Offline Internships",
        "desc": "Kickstart your career by working on real-world projects with Exposys Data Labs."
    },
    {
        "filename": "busness.html",
        "title": "Startup Solutions",
        "subtitle": "Incubation & Acceleration",
        "desc": "We help startups scale fast with dedicated technical teams, innovative architectures, and reliable product development strategies."
    },
    {
        "filename": "freel.html",
        "title": "Free Lance Projects",
        "subtitle": "Independent Development",
        "desc": "Access top-tier freelance engineering talent for your short-term projects and rapid prototyping needs."
    },
    {
        "filename": "lance.html",
        "title": "Consultancy Projects",
        "subtitle": "Expert Technical Guidance",
        "desc": "Our industry experts provide deep technical consulting to solve complex architectural and operational challenges."
    },
    {
        "filename": "sms.html",
        "title": "Promotions",
        "subtitle": "Digital Marketing",
        "desc": "Boost your digital presence with our targeted promotional campaigns and data-driven marketing strategies."
    },
    {
        "filename": "careers.html",
        "title": "Careers",
        "subtitle": "Join Our Team",
        "desc": "We are always looking for passionate engineers, designers, and innovators. Come build the future with us."
    },
    {
        "filename": "about-us.html",
        "title": "About Us",
        "subtitle": "Imagination Behind Technology",
        "desc": "Exposys Data Labs is a pioneering technology company dedicated to advancing research, development, and delivering world-class IT solutions."
    },
    {
        "filename": "team.html",
        "title": "Our Team",
        "subtitle": "The Minds Behind Exposys",
        "desc": "Meet our diverse group of visionaries, developers, and researchers committed to creating positive global impact through technology."
    },
    {
        "filename": "fund.html",
        "title": "Funding Projects",
        "subtitle": "Investment & Grants",
        "desc": "Explore our funding opportunities and grants designed to support innovative technology research and sustainable projects."
    },
    {
        "filename": "workshop/index.html",
        "title": "Workshop",
        "subtitle": "Interactive Learning",
        "desc": "Participate in our hands-on technical workshops to gain practical experience with modern development tools and frameworks."
    },
    {
        "filename": "workshop/freelancer.php",
        "title": "Freelancer Platform",
        "subtitle": "Connect & Collaborate",
        "desc": "Join our network of elite freelancers to collaborate on cutting-edge projects and expand your professional portfolio."
    }
]

for page in pages:
    content = template
    
    # Replace Title
    content = re.sub(r'<title>.*?</title>', f'<title>{page["title"]} - Exposys Data Labs</title>', content)
    
    # Replace Hero H1
    # Split title for span style if multiple words
    words = page["title"].split(' ')
    if len(words) > 1:
        h1 = ' '.join(words[:-1]) + f' <span>{words[-1]}</span>'
    else:
        h1 = f'<span>{words[0]}</span>'
    content = re.sub(r'<h1>Web Application <span>Development</span></h1>', f'<h1>{h1}</h1>', content)
    
    # Replace Hero P
    content = re.sub(r'<p>Modern, responsive, and high-performance web applications built for the future of the internet.</p>', f'<p>Empowering your vision through {page["title"].lower()}.</p>', content)
    
    # Replace Subtitle
    content = re.sub(r'<h3 style="font-size: 1.8rem;">Digital Excellence</h3>', f'<h3 style="font-size: 1.8rem;">{page["subtitle"]}</h3>', content)
    
    # Replace Description
    content = re.sub(r'<p style="font-size: 1.1rem; margin-top: 1rem;">We specialize in creating dynamic web applications.*?</p>', f'<p style="font-size: 1.1rem; margin-top: 1rem;">{page["desc"]}</p>', content)
    
    # Adjust paths if in subdirectory
    if '/' in page["filename"]:
        os.makedirs(os.path.dirname(page["filename"]), exist_ok=True)
        # Update css/js links
        content = content.replace('href="styles.css"', 'href="../styles.css"')
        content = content.replace('src="script.js"', 'src="../script.js"')
        # Update standard html links in the nav
        content = re.sub(r'href="([a-zA-Z0-9_-]+\.html)"', r'href="../\1"', content)
        # Exception for workshop links that were originally workshop/index.html
        content = content.replace('href="../workshop/', 'href="')

    filepath = page["filename"]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Generated {filepath}")

print("Done!")
