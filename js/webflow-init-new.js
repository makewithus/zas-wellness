/**
 * Webflow Master Animation Initialization
 * Simple, reliable animation trigger for Webflow pages
 */

(function() {
    'use strict';

    // Flag to track if we've already initialized
    var initialized = false;

    /**
     * Trigger Webflow animations and interactions
     */
    function triggerWebflowAnimations() {
        // Method 1: Use Webflow.ready if available
        if (window.Webflow && typeof window.Webflow.ready === 'function') {
            window.Webflow.ready();
        }

        // Method 2: Try to access and initialize ix2
        if (window.Webflow && typeof window.Webflow.require === 'function') {
            try {
                var ix = window.Webflow.require('ix');
                if (ix && typeof ix === 'object') {
                    if (typeof ix.all === 'function') {
                        ix.all();
                    }
                    if (typeof ix.trigger === 'function') {
                        ix.trigger();
                    }
                }
            } catch (e) {
                // ix2 path
                try {
                    var ix2 = window.Webflow.require('ix2');
                    if (ix2 && typeof ix2.init === 'function') {
                        ix2.init();
                    }
                } catch (e2) {
                    // Silent fail
                }
            }
        }

        // Method 3: Manually trigger animation class resolution
        try {
            if (window.Webflow && window.Webflow.XAttribute) {
                window.Webflow.XAttribute.queryAll('[data-w-id]').forEach(function(el) {
                    if (el && el.style) {
                        // Force element reflow to trigger animations
                        void el.offsetHeight;
                    }
                });
            }
        } catch (e) {
            // Silent fail
        }

        // Method 4: Refresh GSAP ScrollTrigger if available
        if (typeof ScrollTrigger !== 'undefined' && typeof ScrollTrigger.refresh === 'function') {
            try {
                ScrollTrigger.getAll().forEach(function(trigger) {
                    trigger.refresh();
                });
                ScrollTrigger.refresh();
            } catch (e) {
                // Silent fail
            }
        }
    }

    /**
     * Wait for Webflow script to load
     */
    function waitForWebflow(callback, attempts) {
        attempts = attempts || 0;
        if (attempts > 100) {
            console.warn('Webflow not found after 10 seconds, initializing anyway');
            callback();
            return;
        }

        if (window.Webflow) {
            callback();
        } else {
            setTimeout(function() {
                waitForWebflow(callback, attempts + 1);
            }, 100);
        }
    }

    /**
     * Initialize animations
     */
    function init() {
        if (initialized) return;
        initialized = true;

        // Trigger animations with multiple attempts
        triggerWebflowAnimations();

        // Additional trigger after a small delay
        setTimeout(function() {
            triggerWebflowAnimations();
        }, 50);

        // Final trigger on load event
        setTimeout(function() {
            triggerWebflowAnimations();
        }, 200);
    }

    /**
     * Start initialization
     */
    function start() {
        waitForWebflow(function() {
            // Initialize on different document states
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', init);
                window.addEventListener('load', init);
            } else {
                init();
                window.addEventListener('load', init);
            }

            // Re-initialize on visibility change (tab becomes active)
            document.addEventListener('visibilitychange', function() {
                if (!document.hidden) {
                    setTimeout(init, 100);
                }
            });
        });
    }

    // Start when page loads
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', start);
    } else {
        start();
    }

    // Expose functions for manual triggers
    window.reInitWebflowAnimations = function() {
        initialized = false;
        init();
    };

    window.triggerAnimations = function() {
        triggerWebflowAnimations();
    };

})();