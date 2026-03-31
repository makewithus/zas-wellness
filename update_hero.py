import codecs

file_path = r"c:\Downloaded Web Sites\fitcore-ttm.webflow.io\test4.html"

with codecs.open(file_path, "r", "utf-8") as f:
    lines = f.readlines()

new_hero = """            <!-- ===== Premium Video-Matched Hero Section ===== -->
            <style>
                /* Scoped styles specifically for hero-premium */
                .hero-premium {
                    position: relative;
                    width: 100%;
                    min-height: 100vh;
                    background-color: #060606;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    overflow: hidden;
                    box-sizing: border-box;
                    padding: 6rem 2rem 4rem;
                    z-index: 10;
                }
                
                .hero-content {
                    position: relative;
                    z-index: 20;
                    text-align: center;
                    max-width: 900px;
                    pointer-events: none;
                }

                .hero-premium-heading {
                    font-family: 'Inter', sans-serif;
                    font-size: clamp(3.5rem, 8vw, 7rem);
                    font-weight: 800;
                    line-height: 1.05;
                    color: #ffffff;
                    margin-bottom: 1.5rem;
                    letter-spacing: -0.03em;
                    text-transform: uppercase;
                    opacity: 0;
                    transform: translateY(50px);
                    transition: opacity 1.2s cubic-bezier(0.165, 0.84, 0.44, 1), transform 1.2s cubic-bezier(0.165, 0.84, 0.44, 1);
                }
                .hero-premium-heading.entry-active {
                    opacity: 1;
                    transform: translateY(0);
                }

                .hero-premium-subtitle {
                    font-family: 'Inter', sans-serif;
                    font-size: clamp(1.1rem, 2vw, 1.4rem);
                    color: rgba(255, 255, 255, 0.8);
                    margin-bottom: 2.5rem;
                    max-width: 650px;
                    margin-left: auto;
                    margin-right: auto;
                    font-weight: 400;
                    opacity: 0;
                    transform: translateY(20px);
                    transition: opacity 1s ease-out 0.3s, transform 1s cubic-bezier(0.165, 0.84, 0.44, 1) 0.3s;
                }
                .hero-premium-subtitle.entry-active {
                    opacity: 1;
                    transform: translateY(0);
                }

                .hero-premium-cta {
                    display: inline-block;
                    padding: 1.25rem 3rem;
                    background-color: #ffffff;
                    color: #000000;
                    text-decoration: none;
                    font-family: 'Inter', sans-serif;
                    font-weight: 600;
                    font-size: 1.125rem;
                    border-radius: 50px;
                    pointer-events: auto;
                    transition: transform 0.3s ease, background-color 0.3s ease, box-shadow 0.3s ease, opacity 1s ease-out 0.6s;
                    opacity: 0;
                    transform: translateY(20px);
                }
                .hero-premium-cta.entry-active {
                    opacity: 1;
                    transform: translateY(0);
                }
                .hero-premium-cta.entry-active:hover {
                    background-color: #f0f0f0;
                    transform: translateY(-4px) scale(1.02);
                    box-shadow: 0 15px 30px rgba(255, 255, 255, 0.2);
                }

                /* Container for images (will handle mouse interactivity internally) */
                .hero-images {
                    position: absolute;
                    inset: 0;
                    width: 100%;
                    height: 100%;
                    pointer-events: none;
                    z-index: 5;
                }

                /* Wrapper for each card to handle Parallax and Entry Animation cleanly */
                .hero-card-wrapper {
                    position: absolute;
                    opacity: 0;
                    transform: scale(0.85);
                    transition: opacity 1.2s ease-out, transform 1.2s cubic-bezier(0.165, 0.84, 0.44, 1);
                    will-change: transform, opacity;
                }
                .hero-card-wrapper.entry-active {
                    opacity: 1;
                    transform: scale(1);
                    /* Once entry is done, we swap to a very quick transition so JS scroll/mouse updates are smooth but slightly damped */
                    transition: opacity 1.2s ease-out, transform 0.1s linear; 
                }

                /* The actual card that handles the Hover and floating */
                .hero-card {
                    width: 100%;
                    height: 100%;
                    pointer-events: auto;
                    border-radius: 18px;
                    overflow: hidden;
                    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4), inset 0 0 0 1px rgba(255,255,255,0.05); /* Soft border glow */
                    transition: transform 0.3s cubic-bezier(0.25, 1, 0.5, 1), box-shadow 0.3s ease, filter 0.3s ease;
                    will-change: transform;
                    cursor: default;
                }
                .hero-card img {
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
                    display: block;
                    transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1);
                }

                /* Hover Interactions */
                .hero-card-wrapper:hover {
                    z-index: 30;
                }
                .hero-card-wrapper:hover .hero-card {
                    transform: scale(1.05) !important;
                    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.8), 0 0 30px rgba(255, 255, 255, 0.1);
                    filter: brightness(1.1);
                }

                /* Continuous Floating Animations */
                @keyframes heroFloat1 {
                    0%   { transform: translate(0px, 0px) rotate(0deg) scale(0.97); }
                    33%  { transform: translate(10px, -20px) rotate(1.5deg) scale(1); }
                    66%  { transform: translate(-8px, 15px) rotate(-1deg) scale(0.98); }
                    100% { transform: translate(0px, 0px) rotate(0deg) scale(0.97); }
                }
                @keyframes heroFloat2 {
                    0%   { transform: translateY(0px) rotate(0deg) scale(0.98); }
                    50%  { transform: translateY(-25px) rotate(-1.5deg) scale(1.01); }
                    100% { transform: translateY(0px) rotate(0deg) scale(0.98); }
                }
                @keyframes heroFloat3 {
                    0%   { transform: translate(0px, 0px) rotate(0deg) scale(0.97); }
                    50%  { transform: translate(-15px, -20px) rotate(2deg) scale(1); }
                    100% { transform: translate(0px, 0px) rotate(0deg) scale(0.97); }
                }

                /* Applying floats */
                .hero-float-1 { animation: heroFloat1 12s ease-in-out infinite; }
                .hero-float-2 { animation: heroFloat2 8s ease-in-out infinite 1s; }
                .hero-float-3 { animation: heroFloat3 15s ease-in-out infinite 2s; }
                .hero-float-4 { animation: heroFloat1 11s ease-in-out infinite 0.5s reverse; }
                .hero-float-5 { animation: heroFloat2 9s ease-in-out infinite 1.5s reverse; }
                .hero-float-6 { animation: heroFloat3 13s ease-in-out infinite 0.2s; }

                /* Card Placements & Depths */
                .hc-1 { width: 14vw; max-width: 180px; height: 240px; top: 12%; left: 8%; z-index: 10; filter: blur(2px); opacity: 0.8; }
                .hc-2 { width: 20vw; max-width: 250px; height: 340px; top: 18%; right: 6%; z-index: 15; }
                .hc-3 { width: 22vw; max-width: 290px; height: 180px; bottom: 15%; left: 3%; z-index: 18; }
                .hc-4 { width: 12vw; max-width: 150px; height: 150px; bottom: 25%; right: 28%; z-index: 8; filter: blur(3px); opacity: 0.6; }
                .hc-5 { width: 16vw; max-width: 220px; height: 300px; bottom: 8%; right: 12%; z-index: 12; }
                .hc-6 { width: 15vw; max-width: 200px; height: 260px; top: 10%; right: 30%; z-index: 9; filter: blur(1px); opacity: 0.9; }

                /* Mobile/Responsive Adjustments */
                @media (max-width: 991px) {
                    .hc-4, .hc-6 { display: none; }
                    .hc-1 { width: 180px; height: 240px; top: 8%; left: 2%; }
                    .hc-2 { width: 210px; height: 280px; top: 12%; right: 2%; }
                    .hc-3 { width: 240px; height: 160px; bottom: 10%; left: 5%; }
                    .hc-5 { width: 170px; height: 240px; bottom: 5%; right: 5%; }
                }

                @media (max-width: 767px) {
                    .hero-premium {
                        flex-direction: column;
                        padding: 8rem 1rem 4rem;
                    }
                    .hero-premium-heading { font-size: clamp(2.8rem, 12vw, 4rem); margin-bottom: 1rem; }
                    .hero-premium-subtitle { font-size: 1.1rem; margin-bottom: 2rem; }
                    .hero-images { display: none; } /* Hide complex setup on mobile for performance/clutter */
                    .hero-mobile-stack {
                        display: flex;
                        flex-direction: column;
                        gap: 1rem;
                        width: 100%;
                        margin-top: 3rem;
                    }
                    .hero-mobile-stack .hero-card {
                        width: 100%;
                        height: 300px;
                        filter: none;
                        opacity: 1;
                        pointer-events: none;
                    }
                }
                @media (min-width: 768px) {
                    .hero-mobile-stack { display: none; }
                }
            </style>

            <section class="hero-premium" id="premium-hero-main">
                <div class="hero-images" id="hero-interactive-layer">
                    <!-- Layer 1 (Background - Slow) -->
                    <div class="hero-card-wrapper hc-1 hero-parallax-item" data-speed="0.08" data-mouse="0.02">
                        <div class="hero-card hero-float-1"><img src="https://cdn.prod.website-files.com/691ea5c2d38e36d02b948f36/696b7878e51cdabde67ab71a_about-1.avif" alt="Background Left"></div>
                    </div>
                    <!-- Layer 4 (Background - Slow) -->
                    <div class="hero-card-wrapper hc-4 hero-parallax-item" data-speed="-0.05" data-mouse="-0.015">
                        <div class="hero-card hero-float-4"><img src="https://cdn.prod.website-files.com/691eefbafb5f1e6cbbc807b3/691efea284d276bf9ed2cddc_service%20-%202.avif" alt="Background Right"></div>
                    </div>
                    <!-- Layer 6 (Back-Mid - Slow/Med) -->
                    <div class="hero-card-wrapper hc-6 hero-parallax-item" data-speed="0.1" data-mouse="0.03">
                        <div class="hero-card hero-float-6"><img src="https://cdn.prod.website-files.com/691eefbafb5f1e6cbbc807b3/691efe85fdd0c3500096d008_service%20-%204.avif" alt="Back Mid Right"></div>
                    </div>
                    
                    <!-- Layer 5 (Mid - Medium) -->
                    <div class="hero-card-wrapper hc-5 hero-parallax-item" data-speed="-0.12" data-mouse="-0.04">
                        <div class="hero-card hero-float-5"><img src="https://cdn.prod.website-files.com/691eefbafb5f1e6cbbc807b3/691efeadca6c1dc18f18ab70_service%20-%201.avif" alt="Mid Right Base"></div>
                    </div>

                    <!-- Layer 2 (Foreground - Fast) -->
                    <div class="hero-card-wrapper hc-2 hero-parallax-item" data-speed="0.25" data-mouse="0.07">
                        <div class="hero-card hero-float-2"><img src="https://cdn.prod.website-files.com/691eefbafb5f1e6cbbc807b3/691efe9138135ae16184553d_service%20-%203.avif" alt="Fore Right"></div>
                    </div>
                    <!-- Layer 3 (Foreground - Fast) -->
                    <div class="hero-card-wrapper hc-3 hero-parallax-item" data-speed="0.18" data-mouse="0.05">
                        <div class="hero-card hero-float-3"><img src="https://cdn.prod.website-files.com/691ea5c2d38e36d02b948f36/696b78797cedc44d5ecdf7f7_about-2.avif" alt="Fore Left"></div>
                    </div>
                </div>

                <div class="hero-content">
                    <h1 class="hero-premium-heading">ZAS Wellness</h1>
                    <p class="hero-premium-subtitle">At ZAS, we don't just move bodies. We awaken energy, rhythm, and a way of living that stays with you.</p>
                    <a href="services.html" class="hero-premium-cta">Join The Motion</a>
                </div>

                <!-- Mobile Fallback Structure -->
                <div class="hero-mobile-stack">
                    <div class="hero-card"><img src="https://cdn.prod.website-files.com/691eefbafb5f1e6cbbc807b3/691efe9138135ae16184553d_service%20-%203.avif" loading="lazy"></div>
                    <div class="hero-card"><img src="https://cdn.prod.website-files.com/691ea5c2d38e36d02b948f36/696b78797cedc44d5ecdf7f7_about-2.avif" loading="lazy"></div>
                </div>
            </section>

            <script>
            document.addEventListener('DOMContentLoaded', () => {
                const heroSection = document.getElementById('premium-hero-main');
                if (!heroSection) return;

                const heading = heroSection.querySelector('.hero-premium-heading');
                const subtitle = heroSection.querySelector('.hero-premium-subtitle');
                const cta = heroSection.querySelector('.hero-premium-cta');
                const contentWrapper = heroSection.querySelector('.hero-content');
                const parallaxItems = Array.from(heroSection.querySelectorAll('.hero-parallax-item'));
                const interactiveLayer = document.getElementById('hero-interactive-layer');

                // 1. Precise Entry Reveal (On Load / View)
                const observer = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            heading.classList.add('entry-active');
                            subtitle.classList.add('entry-active');
                            cta.classList.add('entry-active');
                            
                            // Staggered image entry
                            parallaxItems.forEach((item, index) => {
                                setTimeout(() => {
                                    item.classList.add('entry-active');
                                }, 100 + (index * 150)); 
                            });
                            
                            observer.disconnect();
                        }
                    });
                }, { threshold: 0.1 });
                observer.observe(heroSection);

                // Variables for scroll/mouse tracking
                let currentScroll = window.scrollY;
                let mouseX = 0;
                let mouseY = 0;
                let easedMouseX = 0;
                let easedMouseY = 0;
                let rafId = null;

                // 2. Event Listeners
                window.addEventListener('scroll', () => {
                    if (window.innerWidth <= 767) return; // Disable on mobile
                    currentScroll = window.scrollY;
                    requestRender();
                }, { passive: true });

                heroSection.addEventListener('mousemove', (e) => {
                    if (window.innerWidth <= 767) return;
                    
                    const rect = heroSection.getBoundingClientRect();
                    const centerX = rect.left + rect.width / 2;
                    const centerY = rect.top + rect.height / 2;
                    
                    // Mouse distance from center of hero section
                    mouseX = e.clientX - centerX; 
                    mouseY = e.clientY - centerY;
                    
                    requestRender();
                });
                
                heroSection.addEventListener('mouseleave', () => {
                    mouseX = 0;
                    mouseY = 0;
                    requestRender();
                });

                function requestRender() {
                    if (!rafId) {
                        rafId = requestAnimationFrame(renderLoop);
                    }
                }

                function renderLoop() {
                    // Ease the mouse movement for that premium Apple feel
                    easedMouseX += (mouseX - easedMouseX) * 0.08;
                    easedMouseY += (mouseY - easedMouseY) * 0.08;

                    // Apply unified transforms to items
                    parallaxItems.forEach(item => {
                        if (!item.classList.contains('entry-active')) return;
                        
                        const scrollSpeed = parseFloat(item.getAttribute('data-speed') || 0);
                        const mouseSpeed = parseFloat(item.getAttribute('data-mouse') || 0);
                        
                        const scrollYOffset = currentScroll * scrollSpeed;
                        const mouseXOffset = easedMouseX * mouseSpeed;
                        const mouseYOffset = easedMouseY * mouseSpeed;
                        
                        // Combine the base scale(1) with translated values
                        item.style.transform = `scale(1) translate3d(${mouseXOffset}px, ${scrollYOffset + mouseYOffset}px, 0px)`;
                    });

                    // Subtle text scroll parallax
                    if (heading.classList.contains('entry-active')) {
                        contentWrapper.style.transform = `translateY(${currentScroll * 0.05}px)`;
                    }

                    // Continue animating if mouse hasn't caught up
                    if (Math.abs(mouseX - easedMouseX) > 0.1 || Math.abs(mouseY - easedMouseY) > 0.1) {
                        rafId = requestAnimationFrame(renderLoop);
                    } else {
                        rafId = null;
                    }
                }
            });
            </script>
            <!-- ===== End Premium Video-Matched Hero Section ===== -->
\n"""

lines = lines[:361] + [new_hero] + lines[778:]

with codecs.open(file_path, "w", "utf-8") as f:
    f.writelines(lines)

print("Hero section updated successfully.")
