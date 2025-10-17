
    // Optional: Change button text when toggled
    const checkbox = document.getElementById('toggleBtn');
    const label = document.querySelector('label[for="toggleBtn"]');

    checkbox.addEventListener('change', () => {
      if (checkbox.checked) {
        label.textContent = 'Sale ✅';
        label.classList.remove('btn-outline-primary');
        label.classList.add('btn-primary');
      } else {
        label.textContent = 'Sale';
        label.classList.remove('btn-primary');
        label.classList.add('btn-outline-primary');
      }
    });
