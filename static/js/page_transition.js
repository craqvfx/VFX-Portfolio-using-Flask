// Fade in on page load
window.addEventListener('DOMContentLoaded', () => {
    document.body.classList.add('show');
});

// Fade out on link click
document.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', function(e) {
        const href = link.getAttribute('href');
        // skip links like # or external
        if (href.startsWith('#') || link.target === '_blank') return;
        
        e.preventDefault();
        document.body.classList.remove('show');
        setTimeout(() => {
            window.location.href = href;
        }, 500); // match CSS transition time
    });
});