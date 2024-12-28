// Example of a simple script to handle navigation highlighting
document.querySelectorAll('nav ul li a').forEach(link => {
    link.addEventListener('click', function() {
        document.querySelectorAll('nav ul li a').forEach(navLink => {
            navLink.classList.remove('active');
        });
        this.classList.add('active');
    });
});
