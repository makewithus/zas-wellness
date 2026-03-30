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

    // ─── 2. Services nav button highlight (active state on click) ────────────
    function setupServicesNavHighlight() {
        // All four nav inner items
        var navItems = document.querySelectorAll('.services-nav-item-inner');
        if (!navItems.length) return;

        // The CSS already styles .item-one with the active (dark) look.
        // We replicate that exact inline style on click for any button,
        // and reset all others — without touching classes or layout.
        var ACTIVE_BG   = 'var(--_colors---primary)';
        var ACTIVE_FG   = 'var(--_colors---tertiary)';
        var DEFAULT_BG  = '';
        var DEFAULT_FG  = '';

        function setActive(target) {
            navItems.forEach(function(item) {
                if (item === target) {
                    item.style.backgroundColor = ACTIVE_BG;
                    item.style.color           = ACTIVE_FG;
                } else {
                    item.style.backgroundColor = DEFAULT_BG;
                    item.style.color           = DEFAULT_FG;
                }
            });
        }

        navItems.forEach(function(item) {
            item.style.cursor = 'pointer';
            item.addEventListener('click', function() {
                setActive(item);
            });
        });

        // Keep item-one active by default on page load (matches the CSS default)
        var itemOne = document.querySelector('.services-nav-item-inner.item-one');
        if (itemOne) setActive(itemOne);
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