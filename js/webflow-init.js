/**
 * Webflow Initialization Script
 * 
 * PURPOSE: Minimal script to handle custom functionality without breaking
 * Webflow's native interactions (ix2).
 *
 * KEY DESIGN DECISION: 
 *   - NO AJAX routing. Webflow exported sites require full page loads.
 *   - Let Webflow's native webflow.js initialize itself normally.
 *   - Force-calling ix2.init() can crash native continuous animations (like marquees).
 */

(function () {
    'use strict';

    // ─── 1. Refresh GSAP ScrollTrigger (if used) ────────────
    function refreshScrollTrigger() {
        if (typeof ScrollTrigger !== 'undefined' && typeof ScrollTrigger.refresh === 'function') {
            try {
                ScrollTrigger.refresh();
            } catch (e) {}
        }
    }

    // ─── 2. Services nav button highlight & content switch ──────────────────
    function setupServicesNavHighlight() {
        var navItems = document.querySelectorAll('.services-nav-item-inner');
        var contentItems = document.querySelectorAll('.services-item-box');
        if (!navItems.length) return;

        function setActive(index) {
            // 1. Update Buttons
            navItems.forEach(function(item, i) {
                if (i === index) {
                    item.classList.add('active');
                    // We still set inline styles to ensure it overrides any Webflow base styles
                    item.style.backgroundColor = '#000000';
                    item.style.color = '#ffffff';
                } else {
                    item.classList.remove('active');
                    item.style.backgroundColor = '';
                    item.style.color = '';
                }
            });

            // 2. Update Content (Image/Description)
            contentItems.forEach(function(content, i) {
                if (i === index) {
                    // Show active content
                    content.style.display = 'block';
                    content.style.position = 'relative';
                    content.style.opacity = '0';
                    // Simple fade-in animation
                    var opacity = 0;
                    var timer = setInterval(function() {
                        if (opacity >= 1) {
                            clearInterval(timer);
                        }
                        content.style.opacity = opacity;
                        opacity += 0.1;
                    }, 20);
                } else {
                    // Hide other content
                    content.style.display = 'none';
                    content.style.position = 'absolute';
                }
            });
        }

        navItems.forEach(function(item, index) {
            item.style.cursor = 'pointer';
            item.addEventListener('click', function(e) {
                e.preventDefault();
                setActive(index);
            });
        });

        // Initialize first item as active
        setActive(0);
    }

    // ─── 3. Make footer "Book Your Session" loop clickable ──────────────────
    function setupFooterLoop() {
        // Find all footer-loops
        var footerLoops = document.querySelectorAll('.footer-loop');
        footerLoops.forEach(function (loop) {
            // Set pointer cursor to indicate clickability
            loop.style.cursor = 'pointer';
            
            // If the user clicks anywhere in the marquee area, navigate to contact
            // We use standard link navigation (no AJAX)
            loop.addEventListener('click', function (e) {
                // Prevent interfering with actual <a> tags inside if any fire
                if (e.target.tagName !== 'A' && !e.target.closest('a')) {
                    window.location.href = 'contact.html';
                }
            });
        });

        // Ensure proper anchor tags styling isn't breaking the loop items
        var loopItems = document.querySelectorAll('.loop-2-item');
        loopItems.forEach(function(item) {
            item.style.textDecoration = 'none';
        });
    }

    // ─── 4. Main init sequence ───────────────────────────────────────────────
    function init() {
        refreshScrollTrigger();
        setupServicesNavHighlight();
        setupFooterLoop();
    }

    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Also run on window load to ensure all images constraints are met
    window.addEventListener('load', function () {
        refreshScrollTrigger();
        setupServicesNavHighlight();
        setupFooterLoop();
    });

    // Handle window resize for scroll trigger accuracy
    var resizeTimer;
    window.addEventListener('resize', function () {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(refreshScrollTrigger, 200);
    });

})();