function toggleCollapsible(button) {
    const content = button.nextElementSibling;
    content.classList.toggle('open');
    const arrow = button.querySelector('span');
    arrow.innerHTML = content.classList.contains('open') ? '▲' : '▼';
}