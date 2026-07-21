document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialize Feather Icons
    feather.replace();

    // 2. Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 3. Mobile Menu Toggle
    const mobileToggle = document.querySelector('.mobile-toggle');
    const navLinks = document.querySelector('.nav-links');
    const navItems = document.querySelectorAll('.nav-item');

    if (mobileToggle) {
        mobileToggle.addEventListener('click', () => {
            navLinks.classList.toggle('open');
            // Change icon
            const isOpen = navLinks.classList.contains('open');
            mobileToggle.innerHTML = isOpen ? '<i data-feather="x"></i>' : '<i data-feather="menu"></i>';
            feather.replace();
        });
    }

    // Mobile dropdown toggle
    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            // Only active on mobile view
            if (window.innerWidth <= 1024 && item.querySelector('.dropdown-menu')) {
                // If clicked on the link itself, allow navigation, but if it's a "#" toggle dropdown
                const link = item.querySelector('.nav-link');
                if (link.getAttribute('href') === '#') {
                    e.preventDefault();
                    item.classList.toggle('active');
                }
            }
        });
    });

    // 4. Scroll Reveal Animation
    const revealElements = document.querySelectorAll('.reveal');
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                // Optional: Stop observing once revealed
                // observer.unobserve(entry.target); 
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    });

    revealElements.forEach(el => revealObserver.observe(el));

    // 5. Card Hover Glow Effect (Vercel/Linear style)
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);
        });
    });

    // 6. Dynamic Active Tab Highlighting
    const currentUrl = window.location.href;
    const isRootUrl = currentUrl.endsWith('/') || currentUrl.endsWith('\\');
    
    const allLinks = document.querySelectorAll('.nav-links a');
    allLinks.forEach(link => {
        // Ignore the Contact Us button
        if (link.classList.contains('btn')) return;

        // link.href returns the full absolute URL
        if (link.href === currentUrl || (isRootUrl && link.getAttribute('href') === 'index.html')) {
            link.classList.add('active-tab');
            
            // Highlight parent nav-link if it's in a dropdown
            const parentDropdown = link.closest('.dropdown-menu');
            if (parentDropdown) {
                const parentSibling = parentDropdown.previousElementSibling;
                if (parentSibling && parentSibling.classList.contains('nav-link')) {
                    parentSibling.classList.add('active-tab');
                }
            }
        }
    });
});
