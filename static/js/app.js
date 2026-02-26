function greet() {
    const name = document.getElementById('nameInput').value;
    const responseDiv = document.getElementById('response');
    
    fetch(`/api/hello?name=${encodeURIComponent(name)}`)
        .then(response => response.json())
        .then(data => {
            responseDiv.textContent = data.message;
            responseDiv.style.color = '#667eea';
        })
        .catch(error => {
            console.error('Error:', error);
            responseDiv.textContent = 'Error calling API';
            responseDiv.style.color = '#dc3545';
        });
}

// Allow Enter key to trigger greet
document.addEventListener('DOMContentLoaded', function() {
    const input = document.getElementById('nameInput');
    if (input) {
        input.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                greet();
            }
        });
    }
});
