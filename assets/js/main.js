// Notion-style collapsible sections
document.addEventListener('DOMContentLoaded', function() {
  // Add collapse functionality to sections with collapse class
  const collapsibleSections = document.querySelectorAll('.collapsible-section');

  collapsibleSections.forEach(section => {
    const header = section.querySelector('.section-toggle');
    const content = section.querySelector('.section-content');

    if (header && content) {
      // Check if section should be collapsed by default
      if (section.classList.contains('collapsed')) {
        content.style.display = 'none';
        header.classList.add('collapsed');
      }

      header.addEventListener('click', function() {
        content.style.display = content.style.display === 'none' ? 'block' : 'none';
        header.classList.toggle('collapsed');
      });
    }
  });

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href !== '#') {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      }
    });
  });
});
