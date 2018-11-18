function toggleMenu() {
    var el = document.getElementById("navigation");
    if (el.className === 'hidden') {
        el.className = '';
    } else {
        el.className = 'hidden';
    }
}
