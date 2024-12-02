// Get all menu items
const menuItems = document.querySelectorAll('.menu-item');

// Get the current URL's path (e.g., 'me.html')
const currentPath = window.location.pathname.split('/').pop();

// Loop through menu items and add 'active' to the matching one
menuItems.forEach(item => {
    const href = item.getAttribute('href'); // Get the link
    if (href === currentPath) {
        item.classList.add('active'); // Mark as active
    } else {
        item.classList.remove('active'); // Remove active class from others
    }
});
