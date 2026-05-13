document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('form');
    const loader = document.createElement('div');
    
    loader.className = 'loader';
    loader.innerText = 'Analyzing Resume... Please wait.';
    form.appendChild(loader);

    form.addEventListener('submit', function() {
        const button = form.querySelector('button');
        button.style.display = 'none';
        loader.style.display = 'block';
    });
});