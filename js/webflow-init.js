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

    // ─── 2. Make footer "Book Your Session" loop clickable ──────────────────
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

    // ─── 3. Main init sequence ───────────────────────────────────────────────
    function init() {
        refreshScrollTrigger();
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
        setupFooterLoop();
    });

    // Handle window resize for scroll trigger accuracy
    var resizeTimer;
    window.addEventListener('resize', function () {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(refreshScrollTrigger, 200);
    });

})();