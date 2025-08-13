document.addEventListener('DOMContentLoaded', () => {
  const titles = document.querySelectorAll('.section-title');
  const TITLE_HEIGHT = 40;

  const sections = Array.from(titles).map(title => {
    const id = title.dataset.section;
    return {
      id,
      element: document.getElementById(id),
      title,
    };
  });

  function onScroll() {
    const viewportHeight = window.innerHeight;

    sections.forEach(({ title }) => {
      title.style.position = '';
      title.style.top = '';
      title.style.bottom = '';
      title.style.transform = '';
    });

    const topStuck = [];
    const bottomStuck = [];

    // Determine which titles stick to top
    for (const { element, title } of sections) {
      const rect = element.getBoundingClientRect();
      const sectionTop = rect.top + 45;
      const topOffset = topStuck.length * TITLE_HEIGHT;

      if (sectionTop <= topOffset) {
        topStuck.push(title);
      }
    }

    // Determine which titles stick to bottom
    // This time, process bottom stuck titles from bottom to top
    // to assign offsets in stacking order
    for (let i = sections.length - 1; i >= 0; i--) {
      const { element, title } = sections[i];
      if (topStuck.includes(title)) continue;

      const rect = element.getBoundingClientRect();
      const sectionTop = rect.top + 45;
      const bottomOffset = bottomStuck.length * TITLE_HEIGHT;

      // Stick to bottom if sectionTop is below or equal to
      // the stacking position from bottom
      if (sectionTop >= viewportHeight - bottomOffset - TITLE_HEIGHT) {
        bottomStuck.push(title);
      }
    }

    // Apply top stuck titles (stack downwards)
    topStuck.forEach((title, i) => {
      title.style.position = 'fixed';
      title.style.top = `${i * TITLE_HEIGHT}px`;
      title.style.bottom = '';
    });

    // Apply bottom stuck titles (stack upwards)
    bottomStuck.forEach((title, i) => {
      title.style.position = 'fixed';
      title.style.bottom = `${(i * TITLE_HEIGHT)}px`;
      title.style.top = '';
    });

    // Position visible titles to track their sections
    sections.forEach(({ element, title }) => {
      if (topStuck.includes(title) || bottomStuck.includes(title)) return;

      const rect = element.getBoundingClientRect();
      const sectionTop = rect.top + 45;

      title.style.position = 'fixed';
      title.style.top = `${sectionTop}px`;
      title.style.bottom = '';
    });
  }

  window.addEventListener('scroll', onScroll);
  window.addEventListener('resize', onScroll);
  window.addEventListener('load', onScroll);
});
